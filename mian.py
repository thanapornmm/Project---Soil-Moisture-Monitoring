from flask import Flask, jsonify, render_template
import requests
 
app = Flask(__name__)
server_ip = "http://172.20.10.2:3000/data"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/thingspeak")
def thingspeak():
    headers = {'Accept': 'application/json'}
    #https://thingspeak.com/channels/12397/feed.json
    url = "https://thingspeak.com/channels/12397/field/4.json?results=20"
    r = requests.get(url, headers=headers)
    return r.json();

@app.route("/nodemcu/last")
def nodemcu():
    headers = {'Accept': 'application/json'}
    r = requests.get(server_ip+'/sensors?_sort=id&_order=desc&_limit=1', headers=headers)
    return r.json();



if __name__ == "_main_":
    app.run(host='172.20.10.2', debug=True)