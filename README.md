Job Search Web Scraper
Flask Link: https://replit.com/@orane5050/Python#main.py

○ Overall: This project is a web application with Flask. This allows users to search and export remote jobs from "RemoteOK".

○ Main features:

1. Web Scraping with Requests and BeautifulSoup:
    1) Utilizes the "requests" library to request HTTP to RemoteOK's job listing pages.
    2) Uses BeautifulSoup for parsing the HTML content and extracting relevant job details.
    3) Use "requests.get(url, headers={"User-Agent":...)" at "remoteok.py" to prevent the server from blocking the request

2. Export to CSV:

    1) Allows users to export the fetched job listings to a CSV file.

3. Data Storage:

    1) Stores fetched job listings in memory (dictionary db) to avoid repeated API calls when searching for the same keyword within a session.
