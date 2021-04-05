import time
from locust import HttpUser, task, between, events

class WebUser(HttpUser):
    weight = 3
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        response = self.client.get("/")
        print(response.status_code)
#        print(response.text)

class MobileUser(HttpUser):
    weight = 1
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        response = self.client.get("/mobile")
        print(response.status_code)


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    print("A new test is starting")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    print("A new test is ending")

"""
    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username":"foo", "password":"bar"})
"""