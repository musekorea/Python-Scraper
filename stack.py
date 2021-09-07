import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python+pg="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"}


def get_last_pages():
  results = requests.get(URL, headers=headers)
  soup = BeautifulSoup(results.text, "lxml")
  pages = soup.find_all("a",{"class":"s-pagination--item"})
  last_page = pages[-2].get_text().strip()
  return int(last_page)

def get_jobs():
  for page in range(0,1):
    results = requests.get(URL+f"{page}", headers=headers)
    results.raise_for_status()
    print(f'page={page}',results.status_code)
    soup = BeautifulSoup(results.text, "lxml")
    jobs = soup.find_all("div", {"class":"d-flex"})
    for job in jobs:
      titles = job.find("a", {"class":["s-link","stretched-link"]})
      companies = job.find("h3", {"class":"fc-black-700"})
      
      if titles==None:
        continue
      else:
        title = titles.get_text()
        link = "https://stackoverflow.com/"+titles["href"].strip()
      if companies==None:
        continue
      else:
        company = companies.find("span").get_text().strip()
        location = companies.find("span", {"class":"fc-black-500"}).get_text().strip()
      
      print(company, title, link, location)
      print("=="*40)
    
    

get_jobs()


