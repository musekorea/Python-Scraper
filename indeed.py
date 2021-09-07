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

def seek_jobs():
  last_page=extract_last_page()
  soups=[]
  for page in range(0,last_page):
    result = requests.get(indeed_URL+f"&start={page*50}")
    print(f"page{page+1}",result.ok)
    soup = BeautifulSoup(result.text, "lxml")
    soups.append(soup)
    if result.ok==False:
      print("No more Pages")
      return
  return soups

def extract_job_indeed():
  soups = seek_jobs()
  jobs = []    
  for soup in soups:      
    results = soup.find_all("a",  {"class":["tapItem","fs-unmask","result"]})
    for result in results:
      job_title = result.find("h2", {"class":"jobTitle"}).find("span")
      if job_title.has_attr("title"):
        job_title = job_title["title"]
      else:
        continue
      companies= result.find("span",{"class":"companyName"}).string
      location=result.find("div", {"class":"companyLocation"}).get_text()
      if result["href"].startswith("/rc"):
        link = result["href"]
        
      else:
        continue
      jobs.append({"title":job_title, "company":companies, "location":location, "link":"https://www.indeed.com"+link})
      
  return jobs