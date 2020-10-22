from flask import Flask, render_template, request, redirect
from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs

app = Flask("Flask_Scrapper")

db = {}

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
    word = word.lower()
    fromDb = db.get(word)
    if fromDb:
      jobs = fromDb
    else:
      indeed_jobs = get_indeed_jobs(word)
      so_jobs = get_so_jobs(word)
      jobs = indeed_jobs + so_jobs
      db[word] = jobs
  #else
    #return redirect("/")
  return render_template("report.html", keyword=word, cntResults=len(jobs))

#직접 html코드 사용 가능
# def home():
#   return "<h1>Job Search</h1>\
#   <form><input placeholder='find the jobs' required /><button>Search</button>"

#dynamic url
# @app.route("/<username>")
# def show_name(username):
#   return f"Hello {username}"

app.run(host="0.0.0.0")