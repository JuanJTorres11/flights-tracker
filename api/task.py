from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task
def retrieveData():
    return "TODO"