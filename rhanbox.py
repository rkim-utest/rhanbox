import requests
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
APPLAUSE_API_KEY = ""
API_URL = "http://api-dev.applause.com/atom/exec"

def mk_params(pars):
  pars["apikey"] = APPLAUSE_API_KEY
  return pars

@app.route("/companies/<company_id>")
def hello(company_id):
  r = requests.get(API_URL, params=mk_params({"company_id": company_id}))
  res =  r.json()
  return render_template('testing.html', res=res)

if __name__ == "__main__":
  app.debug = True
  app.run()
