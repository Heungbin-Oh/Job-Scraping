import requests
from bs4 import BeautifulSoup

all_jobs = []

#Set the job data list to DB
def set_job(jobs):
    for job in jobs:
        title = job.find("h2").text
        company = job.find("h3").text
        region = job.find("div", class_="location").text
        url = job.find("a")["href"]

        job_data = {
            "title": title,
            "company": company,
            "region": region,
            "link": f"https://remoteok.com{url}"
        }
        all_jobs.append(job_data)


def extract_remoteok_jobs(keyword):
    print(f"Scrapping {keyword}...")
    url = f"https://remoteok.com/remote-{keyword}-jobs"

    #requests: Python library used for making HTTP requests to websites

    #header reprents the user agent which means who the client is
    #or from which browser the client is
    #to prevent the server from blocking the request
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        })
    #make a parsed tree structure of HTML/XML documents for Python
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("table", id="jobsboard").find_all(
        "td", class_="company position company_and_position")[1:]

    set_job(jobs)
    return all_jobs
