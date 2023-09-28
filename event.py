
#event.py

import random 
from datetime import datetime
import pytz

location_types = ["highway", "residential", "commercial", "city_center"]
ist_time = pytz.timezone("Asia/Kolkata")

# Sample event data for five vehicles with random location types
events = [
    {
        "timestamp":  datetime.now(ist_time),
        "is_driving_safe": True,
        "vehicle_id": 1,
        "location_type": random.choice(location_types)
    },
    {
        "timestamp": datetime.now(ist_time),
        "is_driving_safe": True,
        "vehicle_id": 2,
        "location_type": random.choice(location_types)
    },
    {
        "timestamp": datetime.now(ist_time),
        "is_driving_safe": True,
        "vehicle_id": 3,
        "location_type": random.choice(location_types)
    },
    {
        "timestamp": datetime.now(ist_time),
        "is_driving_safe": True,
        "vehicle_id": 4,
        "location_type": random.choice(location_types)
    },
    {
        "timestamp": datetime.now(ist_time),
        "is_driving_safe": True,
        "vehicle_id": 5,
        "location_type": random.choice(location_types)
    },
    # Add more events for other vehicles
]
