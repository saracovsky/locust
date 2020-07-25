from locust import HttpLocust, TaskSet, task, between

class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.post("/user/1/link-storage", {
            "shortUrl": "google",
            "longUrl": "https://www.google.com.tr",
            "daysToBeAllive":1
        })

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/about/")


class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    wait_time = between(5, 15)