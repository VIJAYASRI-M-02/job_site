from flask import Flask, render_template,jsonify

app = Flask(__name__)

jobs=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Chennai, India',
    'salary':'15LPA'
  },
  {
    'id':2,
    'title':'Frontend developer',
    'location':'Remote',
    'salary':'10LPA'
  },
  {
    'id':3,
    'title':'Backend Developer',
    'location':'Mumbai, India',
    'salary':'12LPA'
  },
  {
    'id':4,
    'title':'Software development engineer',
    'location':'Bangalore, India',
    'salary':'18LPA'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=jobs)
  
@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port='3000')
