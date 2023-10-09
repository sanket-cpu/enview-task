from datetime import datetime, timedelta
from collections import defaultdict
from event import events
from itertools import count
import random
import time
import logging as log

log.basicConfig(filename="file1.log")
from ruleengine import *
# Use a counter to generate unique IDs
alert_id_counter = count()

# Function to generate a unique alert ID
def generate_unique_alert_id():
    return f"alert_{next(alert_id_counter)}"
# Define the alert history to keep track of generated alerts
alert_history = defaultdict(dict)

# Function to generate an alert
def generate_alert(vehicle_id, location_type):
    # Add your logic to generate an alert here
    # You can create an alert object with a unique ID and timestamp
    alert = {
        "alert_id": generate_unique_alert_id(),
        "timestamp": datetime.utcnow(),
        "vehicle_id": vehicle_id,
        "location_type": location_type,
    }
    return alert

evt = []
def simulate_event_generation(vehicle_id, duration_minutes):
    log.warning("simulate_event_generation started")
    start_time = datetime.utcnow()
    generated_alerts = []  # Collect generated alerts here

    while (datetime.utcnow() - start_time).total_seconds() < duration_minutes * 60:
        location_type = random.choice(location_types)
        is_driving_safe = random.choice([True, False])
        event = {
            "timestamp": datetime.utcnow(),
            "is_driving_safe": is_driving_safe,
            "vehicle_id": vehicle_id,
            "location_type": location_type,
        }
        evt.append(event)

        if check_rule_conditions(vehicle_id, location_type, evt):
            alert = generate_alert(vehicle_id, location_type)
           # print(alert)
            generated_alerts.append(alert)  # Collect generated alerts
            time.sleep(15)
        
    log.warning("simulate_event_generation ended")
   # print(generated_alerts)
    return generated_alerts 
# Example location types (replace this with your location types)
location_types = ["highway", "city_center", "commercial", "residential"]

# Use a counter to generate unique IDs
alert_id_counter = count()

# Example vehicle ID (replace this with the entered vehicle ID)
vehicle_id = 1

# Simulate event generation for 30 seconds
#simulate_event_generation(vehicle_id, 30 )