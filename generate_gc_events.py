import csv
from datetime import datetime, timedelta

# Start date (today)
start_date = datetime.today()

# Event templates per day
events_template = [
    {
        "subject": "Job Interview – {company}",
        "start_hour": 9,
        "duration_hours": 1.5,
        "description": "{company} interview for {role}. Responsibilities: {details}.",
        "location": "{city}",
    },
    {
        "subject": "Job Interview – {company}",
        "start_hour": 12,
        "duration_hours": 1.5,
        "description": "{company} interview for {role}. Responsibilities: {details}.",
        "location": "{city}",
    },
    {
        "subject": "Gym Workout – {workout_type}",
        "start_hour": 15,
        "duration_hours": 1.5,
        "description": "{description}",
        "location": "{city} Gym",
    },
    {
        "subject": "AI Automation Project Work",
        "start_hour": 17,
        "duration_hours": 2,
        "description": "Work on n8n workflow for Google Calendar automation, testing event creation and triggers.",
        "location": "Home Office, {city}",
    },
    {
        "subject": "Social – {activity}",
        "start_hour": 20,
        "duration_hours": 2,
        "description": "{description}",
        "location": "{city}",
    },
]

# Day-specific data
daily_data = [
    {
        "city": "Canberra, ACT, Australia",
        "companies": [
            (
                "Quantum AI Solutions",
                "AI Engineer",
                "developing ML models for automation, integrating AI workflows, collaborating with R&D team. Required: Python, TensorFlow, experience with AI pipelines.",
            ),
            (
                "RoboTech Innovations",
                "Robotics Software Developer",
                "building autonomous agent software, computer vision integration, real-time data processing. Required: ROS, C++, Python.",
            ),
        ],
        "gym": (
            "Strength & Conditioning",
            "Full-body workout focusing on strength, conditioning, and mobility. Includes compound lifts, cardio, and core exercises.",
        ),
        "social": (
            "Networking Dinner with Peers",
            "Dinner meetup with tech and AI community for networking and idea sharing.",
        ),
    },
    {
        "city": "Sydney, NSW, Australia",
        "companies": [
            (
                "NeuralNet Labs",
                "Machine Learning Engineer",
                "building neural networks for predictive analytics, optimizing ML pipelines. Skills: PyTorch, Python, cloud ML services.",
            ),
            (
                "Synapse Robotics",
                "Robotics Software Engineer",
                "automation scripts, autonomous agent integration, sensor data processing. Skills: ROS, Python, C++.",
            ),
        ],
        "gym": (
            "HIIT & Cardio",
            "High-intensity interval training and cardio session to boost endurance and energy.",
        ),
        "social": (
            "Movie Night with Friends",
            "Relaxing movie night with friends to unwind after a busy day.",
        ),
    },
    {
        "city": "Melbourne, VIC, Australia",
        "companies": [
            (
                "AI Horizon",
                "AI Research Engineer",
                "NLP model development, automated data pipelines, AI research implementation. Required: Python, NLP, ML experience.",
            ),
            (
                "CyberTech Solutions",
                "Cybersecurity Automation Engineer",
                "building AI-based security monitoring, incident automation, threat detection.",
            ),
        ],
        "gym": (
            "Functional Training",
            "Functional training session with bodyweight and free weight exercises to improve flexibility and strength.",
        ),
        "social": (
            "Coffee Meetup with Colleagues",
            "Casual coffee meetup to discuss projects and networking.",
        ),
    },
    {
        "city": "Brisbane, QLD, Australia",
        "companies": [
            (
                "DeepVision Tech",
                "Computer Vision Engineer",
                "image processing, object detection models, real-time analytics.",
            ),
            (
                "Automata Labs",
                "Robotics AI Developer",
                "AI algorithms for autonomous robots, workflow automation, sensor integration.",
            ),
        ],
        "gym": (
            "Strength & Mobility",
            "Strength and mobility workout focusing on compound lifts, stretching, and recovery.",
        ),
        "social": (
            "Dinner with Friends",
            "Dinner at a local restaurant to catch up with friends and relax.",
        ),
    },
]

# CSV header
csv_header = [
    "Subject",
    "Start Date",
    "Start Time",
    "End Date",
    "End Time",
    "Description",
    "Location",
]

# Create CSV file
with open("mock_calendar_events.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(csv_header)

    for day_offset, data in enumerate(daily_data):
        day_date = start_date + timedelta(days=day_offset)
        for i, event in enumerate(events_template):
            # Fill dynamic values
            if i < 2:  # Job interviews
                company, role, details = data["companies"][i]
                subject = event["subject"].format(company=company)
                description = event["description"].format(
                    company=company, role=role, details=details
                )
            elif i == 2:  # Gym
                workout, workout_desc = data["gym"]
                subject = event["subject"].format(workout_type=workout)
                description = workout_desc
            elif i == 4:  # Social
                activity, activity_desc = data["social"]
                subject = event["subject"].format(activity=activity)
                description = activity_desc
            else:  # AI work session
                subject = event["subject"]
                description = event["description"]

            location = event["location"].format(city=data["city"])

            start_time = datetime(
                day_date.year, day_date.month, day_date.day, event["start_hour"], 0
            )
            end_time = start_time + timedelta(hours=event["duration_hours"])

            writer.writerow(
                [
                    subject,
                    start_time.strftime("%Y-%m-%d"),
                    start_time.strftime("%I:%M %p"),
                    end_time.strftime("%Y-%m-%d"),
                    end_time.strftime("%I:%M %p"),
                    description,
                    location,
                ]
            )

print("CSV file 'mock_calendar_events.csv' has been generated successfully.")
