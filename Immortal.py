# Replit automatically turns a server to sleep after one hour of no
# activity, this is a utility function that connects the server with a
# monitoring service "uptimerobot.com" that pings the server every 5 minutes
# to keep it awake
from flask import Flask
from threading import Thread

app = Flask(')')

@app.route('/')
def home():
  return 'I am immortal!'

def run():
  app.run(host='0.0.0.0', port=8080)

def Immortal():
  t = Thread(target = run)
  t.start()