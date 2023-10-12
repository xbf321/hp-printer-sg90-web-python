from flask import Flask
import configparser

# https://docs.python.org/3/library/configparser.html
config = configparser.ConfigParser()
configFilePath = 'config.ini'

app = Flask(__name__)

@app.route('/')
def index():
  config.set('DEFAULT', 'end_angle', '15')
  with open(configFilePath, 'w') as configfile:
    config.write(configfile)
  return "<p>Hello, World!23</p>"

@app.route('/reboot')
def reboot():
  return "reboot"
