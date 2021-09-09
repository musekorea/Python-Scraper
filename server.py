from flask import Flask, render_template, request



app = Flask("JobScrapper")

@app.route("/")
def root():
  return render_template("index.html")

@app.route("/search")
def search():
  query = request.args.get("word")
  return render_template("scrap.html", query=query, cat="moya")

app.run(host="127.0.0.1", port=8080)