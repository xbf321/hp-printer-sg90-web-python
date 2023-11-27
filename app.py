from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
@app.route('/alive')
def index():
  return "Hello world"

@app.route('/go')
def go():
  subprocess.Popen(["./sg90s.py"])
  return "go"
