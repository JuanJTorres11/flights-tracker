from celery import Celery
import requests
from .services import logic

app = Celery('tasks', broker='redis://localhost')

#@app.task
def retrieve_data():
    r = requests.get("https://raw.githubusercontent.com/Skyscanner/full-stack-recruitment-test/main/public/flights.json")
    data = r.json()
    return logic.add_flights(data)