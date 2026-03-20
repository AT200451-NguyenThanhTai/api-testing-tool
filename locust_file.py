from locust import HttpUser, task

class UserBehavior(HttpUser):

    @task
    def get_tests(self):
        self.client.get("/public/v2/users")

    @task
    def post_tests(self):
        data = {
            "id" : "8399239",
            "name": "Darshwana Panicker",
            "email": "darshwana_panicker@hills.example",
            "gender": "male",
            "status": "inactive"
        }

        self.client.post("/public/v2/users", json=data)
        