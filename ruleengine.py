from datetime import datetime, timedelta
from collections import defaultdict
from event import events
from itertools import count
import random
import time
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

# Function to check if the rule conditions are met
def check_rule_conditions(vehicle_id, location_type, events):
    # Define the rule conditions based on location_type
    rule_conditions = {
        "highway": 4,
        "city_center": 3,
        "commercial": 2,
        "residential": 1,
    }
    
    # Check if an alert has already been generated in the last 5 minutes
    last_alert_time = alert_history[vehicle_id].get(location_type)
    if last_alert_time and (datetime.utcnow() - last_alert_time) < timedelta(minutes=5):
        return False
    
    # Check if there are at least X *events in the past 5 minutes* where is_driving_safe is false
    recent_events = [event for event in events if event['vehicle_id'] == vehicle_id and event['location_type'] == location_type]
    unsafe_events = [event for event in recent_events if not event['is_driving_safe']]
    
    return len(unsafe_events) >= rule_conditions[location_type]
