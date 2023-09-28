## The Problem Statement 

The company has built a model that detects this behavior. The model is deployed in an IoT device on the vehicle. Every minute, the model emits a driving event with the following fields:

timestamp: ISO date time.
is_driving_safe: A boolean indicating whether the driving is safe.
vehicle_id: A unique ID associated with a vehicle.
location_type: One of the following values: highway, residential, commercial, city_center. More values may be added in the future.

The IoT device is connected to the internet and can make API calls to a cloud server.

# The Rule Engine
The customer wants to know if the driver is not driving safely but doesn't want to get alerted every time this happens; they are only interested in repeated speed violations. Speed violations in a residential area are considered more serious than those on a highway.

Therefore, a rule engine is required to aggregate and transform driving events into alerts that will be shown to the customer.

For this task, the rule is as follows:

Generate an alert if there are at least X events in the past 5 minutes where is_driving_safe is false. The value of X depends on the location_type:

highway requires at least 4 events.
city_center requires at least 3 events.
commercial requires at least 2 events.
residential requires at least 1 event.
Ensure that an alert hasn't already been generated in the past 5 minutes.

Evaluating this rule against a set of events is referred to as a run of the rule.

# The Task
Your task is to build a service that:

Accepts events from the IoT device.
Generates alerts based on the rule engine.
Provides APIs:
POST /event: The IoT device sends driving events to this endpoint.
GET /alert/{alert_id}: Responds with a single alert by ID.
You should store the events in a database (a simple in-memory data structure like a list is sufficient; you will not be evaluated on database integration). Every 5 minutes, there must be at least one run of the rule on the events received in the past five minutes. Alerts should be generated within a reasonable latency after the rule condition is met.

The mapping of location_type and alert thresholds should be stored in a table in the database and not hardcoded in the code.

# Evaluation Criteria
- Code clarity and readability.
- A working solution that can be run locally.
- Thoughtful design decisions considering user and developer experience.
- Choice of framework and database doesn't affect the evaluation.
- Alerts should be generated within a reasonable latency after the rule condition is met.






## Code description

- the folder consisting of *templates* has all the related html files for the application 
 -- this includes **index.html** the landing page where you have to enter the vehicle id.
 -- **details.html** checks whether the vehicle exists in the database
 -- **alertnotify.html** responds with a GET request displaying the alerts for the specified vehicle

- the other python files contain the core logic of the application 
 -- **alerts.py** is responsible for notifying the user for the alerts
 -- **ruleengine.py** governs the rules to generate the alert
 -- **app.py** contains the flask logic and the routing events for the application 