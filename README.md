# Job Search Web Scraper
![Screenshot 2024-09-12 155319](https://github.com/user-attachments/assets/e29be221-b264-4514-b00d-030d2e4989ad)  ![Screenshot 2024-09-12 152502](https://github.com/user-attachments/assets/df4ff05b-574d-4e12-b5e2-1754524ec63b)

Flask Link: https://replit.com/@orane5050/Python#main.py

This is a Web Application with Python and Flask. This helps users to search and export remote jobs from "RemoteOK".

## What Used in the Project
- **Python**: Used to utilize Requests and BeatifulSoup packages to scrape the information from a website.
- **Flask**: Used to implement a simple Framework server because it only contains simple functions not using the database.
  
## Features:
### Web Scraping with Requests and BeautifulSoup:
1) Utilizes the "requests" library to request HTTP to RemoteOK's job listing pages.
2) Uses BeautifulSoup for parsing the HTML content and extracting relevant job details.
3) Use "requests.get(url, headers={"User-Agent":...)" at "remoteok.py" to prevent the server from blocking the request

### Export to CSV:
Allows users to export the fetched job listings to a CSV file.

### Data Storage:
Stores fetched job listings in memory (dictionary db) to avoid repeated API calls when searching for the same keyword within a session.

## Challenges & Future Improvements

### Challenges:

Had difficulty when the request was rejected by the WebSite. So, when I sent the request, I used the header as 'User-Agent' so that the WebSite thinks that I'm a user not just scraping information from it.

### Future Improvements:

Implement the same service but also include a LinkedIn website. Now, even if I use the User-Agent header for the request, it rejects the request.
