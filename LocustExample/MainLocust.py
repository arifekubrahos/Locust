from locust import HttpLocust, TaskSet
from bs4 import BeautifulSoup
import random

auth_token = ""


def login(self):
    response = self.client.get("/login")
    pq = BeautifulSoup(response.text)
    text = pq.find('input', attrs={'name': 'authenticity_token'}).get('value')
    global auth_token
    auth_token = text


def login_post(self):
    global auth_token
    self.client.post("/session", {"commit": "Sign in",
                                  "utf8": "✓",
                                  "authenticity_token": auth_token,
                                  "login": "arife.hos@tigalab.com",
                                  "password": "arife.hos.1"})


def repositories(self):
    self.client.get("/testtiga?tab=repositories")


def profile(self):
    self.client.get("/testtiga")


def getuser(self):
    text =["/erfdf","/arifekubrahos"]
    response = self.client.get(random.choice(text), catch_response=True)
    if not response.ok:
        response.failure("Get user fail")


def logout(self):
    response = self.client.get("/logout")
    pq = BeautifulSoup(response.text)
    text = pq.find('input', attrs={'name': 'authenticity_token'}).get('value')
    global auth_token
    auth_token = text


def logout_post(self):
    global auth_token
    self.client.post("/logout", {"utf8": "✓",
                                "authenticity_token": auth_token })


class UserBehavior(TaskSet):
    tasks = {repositories: 2, profile: 1, getuser:1}

    def on_start(self):
        login(self)
        login_post(self)

    def on_stop(self):
        logout(self)
        logout_post(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000