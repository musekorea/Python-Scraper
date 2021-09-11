from types import DynamicClassAttribute
from flask import Flask, render_template, request, redirect, url_for
from stack import extract_job_stack
from indeed import extract_job_indeed
import os

app = Flask("JobScrapper")

def dated_url_for(endpoint, **values):
  if endpoint == 'static':
    filename = values.get('filename', None)
    if filename:
      file_path = os.path.join(app.root_path,endpoint, filename)
      values['q'] = int(os.stat(file_path).st_mtime)
  return url_for(endpoint, **values)

@app.context_processor
def override_url_for():
  return dict(url_for=dated_url_for)


@app.route("/")
def root():
  print(request)
  return render_template("index.html")

db = {}

@app.route("/search")
def search():
  query = request.args.get("word")
  if query:
    print(request)
    query = query.lower()
    if db.get(query):
      jobs = db.get(query)
    else:
      indeed_jobs = extract_job_indeed(query)
      stack_jobs = extract_job_stack(query)
      jobs = indeed_jobs+stack_jobs
      db[query]=jobs
  else:
    return redirect("/")
  return render_template("scrap.html", query=query, searchNum=len(jobs), jobs=jobs)

app.run(host="127.0.0.1", port=5050, )