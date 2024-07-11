from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

#instanciate, it does not create browser(headless=True).
#it creates only process 
browser = p.chromium.launch(headless=False)

#new page
page = browser.new_page()


class JobScraper:
    
    def __init__(self, keyword):
        self.keyword = keyword
        self.content = None
        self.jobs_db = []
        
    def get_content(self):
        url = f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position"
        page.goto(url)

        times = 4
        for _ in range(times):
            page.keyboard.down("End")
            time.sleep(1)

        self.content = page.content()
        
    def get_job_list(self):
        if self.content:
            soup = BeautifulSoup(self.content, "html.parser")

            jobs = soup.find_all("div", class_="JobCard_container__REty8")

            
            for job in jobs:
                link = f"https://www.wanted.co.kr{job.find('a')['href']}"
                title = job.find("strong", class_="JobCard_title__HBpZf").text
                company_name = job.find("span", class_="JobCard_companyName__N1YrF").text
                reward = job.find("span", class_="JobCard_reward__cNlG5").text
                
                job = {
                    "title":title,
                    "company_name": company_name, 
                    "reward": reward,
                    "link": link
                }
                self.jobs_db.append(job)
                print(self.jobs_db)
        else:
            print("Failed to save content to DB!")
    
    def save_to_csv(self):
        file = open(f"{self.keyword}_jobs.csv","w")
        writer = csv.writer(file)
        writer.writerow(
            [
                "Title",
                "Company",
                "Reward",
                "Link"
            ]
        )

        if self.jobs_db:
            print("Start Saving")
            for job in self.jobs_db:
                writer.writerow(job.values())
                
            file.close()
        else:
            print("Error: it does not have jobs_db!")
        
        
        
keywords = {
    "Java",
    "Python",
    "Nextjs"
}
for keyword in keywords:
    jobs = JobScraper(keyword)
    jobs.get_content()
    jobs.get_job_list()
    jobs.save_to_csv()
    
p.stop()