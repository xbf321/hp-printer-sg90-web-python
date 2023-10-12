from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "<p>Hello, World!23</p>"

@app.route('/reboot')
def reboot():
  return "reboot"
