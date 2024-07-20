#packages
from flask import Flask, render_template, request, redirect, send_file

#extractors
from extractors.remoteok import extract_remoteok_jobs

#file
from file import save_to_file

#A simple framework for building WEB applications.
app = Flask("JobScrapper")


#Home page
@app.route("/")
def home():
  return render_template("home.html")


db = {}


#Search page
@app.route("/search")
def search():
  #get the keyword from the query string so that we can use it in the url
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword in db:
    jobs = db[keyword]
  else:
    jobs = extract_remoteok_jobs(keyword)
    db[keyword] = jobs

  return render_template("search.html", keyword=keyword, jobs=jobs)


#Exporting CSV file
@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)


#Start the server
#Give debug mode to do automatic reloading when I change the code
app.run("0.0.0.0", debug=True)
