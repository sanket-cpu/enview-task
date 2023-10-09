from flask import Flask , render_template, url_for ,request, jsonify,redirect, flash
from event import events
from alerts import simulate_event_generation
from alerts import *
import logging as log
app = Flask(__name__)
log.basicConfig(filename= "file.log")
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/details" , methods = ['POST'])
def details():
    vehicle_id = request.form['id']
    matching_events = [event for event in events if event['vehicle_id'] == int(vehicle_id)]
    if matching_events:
        return render_template("details.html" , value = vehicle_id)
    else:
        return "<h1> Vehicle does not exist in DB </h1>" 


@app.route("/alerts/<int:vehicle_id>" , methods = ["GET"])
def notify(vehicle_id):
    #return "<h1> No Data available yet . Check back later!  </h1>" 
    log.warning("notify started")
    log.warning(str(request.form["vehicle_id"]))
    alert = simulate_event_generation(int(request.form["vehicle_id"]),30 )
    log.warning("hello" + str(alert))
    return render_template('alertnotify.html', vehicle_id=request.form["id"], alerts=alert)


"""@app.route('/check_vehicle', methods=['POST'])
def check_vehicle():
        vehicle_id = request.form.get('id')
        matching_events = [event for event in events if event['vehicle_id'] == int(vehicle_id)]
        if matching_events:
            return jsonify({"message: vehicle exists"})
    # Check if the vehicle_id exists in events
    
        else:
            return jsonify({"message": "Vehicle does not exist in events data."})

"""
    
if __name__ == "__main__":
    app.run(debug = True)