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

def extract_job(soup):
  results = soup.find_all("td", {"class":"resultContent"})
    
  for result in results:
    job_title = result.find("h2", {"class":"jobTitle"}).find("span")
    if job_title.has_attr("title"):
      job_title = job_title["title"]
    else:
      continue
    companies= result.find("span",{"class":"companyName"}).string
    print(job_title,"-",companies)
    
  return

def seek_jobs():
  last_page=extract_last_page()
  for page in range(0,last_page):
    result = requests.get(indeed_URL+f"&start={page*50}")
    print(f"page{page+1}",result.ok)
    soup = BeautifulSoup(result.text, "lxml")
    extract_job(soup)  
    if result.ok==False:
      print("No more Pages")
      return
    
