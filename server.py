from flask import Flask, render_template, request, redirect
from stack import extract_job_stack
from indeed import extract_job_indeed



app = Flask("JobScrapper")

@app.route("/")
def root():
  return render_template("index.html")

@app.route("/search")
def search():
  query = request.args.get("word")
  if query:
    query = query.lower()
    indeed_jobs = extract_job_indeed(query)
    stack_jobs = extract_job_stack(query)
    print(indeed_jobs, stack_jobs)
    
  else:
    return redirect("/")
  return render_template("scrap.html", query=query)

app.run(host="127.0.0.1", port=8080)