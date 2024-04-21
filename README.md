# WeCare-API
WeCare is an uber-like platform for healthcare practioners where people in need of health care attention/services can get access a pool of health care specialists of different kind.

As someone in need of an medical related consultation, you will be able to go the platform, browse through a list of highly vetted health care specialist, filter them by the type of need you have and be able to book an appointment with your choice specialist.

After booking an appointment, the health care specialist will receive your request and;-
- Approve it for the day you requested,
- Reschedule it to another day and request for your consent before confirming it.
- Decline the appointment request.


Health care specialists will be listed with;-
- Their hourly consulation rates.
- Their respective patient feedback and Rating.
- Availability days for high performant specialists.


# Components of the platform
- Backend Web Service.
- Admin Dashboard.
- Specialist App (Mobile & Web).
- Patient App (Mobile & Web).


# Technologies
- Backend
    - Python
    - Django REST

- Admin Dashboard
    - NextJs

- Patient App
    - NextJs
    - React Native

- Specialist/Doctor App
    - NextJs
    - React Native

- Database
    - PostgreSQL
    - CockroachDB (For specialisted payments management)
    - Redis (For caching)

- Messaging & Queuing
    - Celery
    - RabbitMQ (on CloudAMQP for testing)

- Containerization
    - Docker
    - Kubernetes (When microservices will be adopted)


# How to run the backend
## 1. Without Docker 
It is assumed that you have Python installed on your computer, if not, download it here <link>https://www.python.org/downloads/</link>

#### Creating project directory
To create a project directory, 
```sql
mkdir WeCareBackend
```
Then Change directory in the project directory
```sql
cd WeCareBackend
```
#### Creating virtual environment
Then create a virtual environment
```sql
python3 -m venv venv
```
Then, Activate the virtual environment
```sql
source venv/bin/activate
```

#### Cloning the project
Clone the repository from github
```sql
git clone git@github.com:ndambopaul/WeCare-API.git
```
or 
```sql
git clone https://github.com/ndambopaul/WeCare-API.git
```

#### Running the project 
After that, change directory to the repository cloned
```sql
cd WeCare-API
```

Then Install dependencies
```sql
pip install -r requirements.txt
```

Finally, run the project
```sql
python manage.py runserver
```

Access the API documentation at 
```sql
http://localhost:8000/docs
```