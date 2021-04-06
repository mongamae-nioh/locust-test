import time
import json
from locust import HttpUser, task, between, events

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    def on_start(self):
        response = self.client.post("/", json={"email":"******", "password":"******"})

    @task(3)
    def home(self):
        response = self.client.request("GET", "/home")
        print("Response status code:", response.status_code)
        print("Response url:", response.url)

    @task(1)
    def display_image(self):
        response = self.client.request("GET", "/image")
        print("Response status code:", response.status_code)
        print("Response url:", response.url)

# ここへPOSTなど

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")
