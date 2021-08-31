import requests
from bs4 import BeautifulSoup

indeed_URL = "https://www.indeed.com/jobs?q=python&limit=50"

def extract_last_page():
  indeed_res = requests.get(indeed_URL)
  indeed_soup = BeautifulSoup(indeed_res.text,"lxml")
  pagination = indeed_soup.find("div", attrs={"class":"pagination"})
  pages = pagination.findAll("a")
  pageSpans = []
  for page in pages[0:-1]:
    pageSpans.append(int(page.string))
  last_page = pageSpans[-1]
  return last_page

def extract_jobs():
  last_page=extract_last_page()
  for page in range(0,last_page):
    result = requests.get(indeed_URL+f"&start={page*50}")
    print(f"page{page+1}",result.ok)
    if result.ok==False:
      print("No more Pages")
      return
    
