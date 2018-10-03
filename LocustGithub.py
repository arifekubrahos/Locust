from locust import TaskSet, Locust, HttpLocust, task


def login(l):
    l.client.post("/Account/Login",{"_email":"", "_password":""},  allow_redirects = True)

def logout(l):
    l.client.get("/Account/Logout", allow_redirects=True)

def urun(l):
    name="/urun_sorgulama"
    l.client.get("/urun", name=name)

def urun_sorgulama(l):
    isLogon_response= l.client.get("/Account/IsLogon")
    values= {"gtin":"", "sn":""} #buraya üretilen gtin-sn yazılacak
    if(isLogon_response.status_code == 200):
        sorgu_response = l.client.get("/Product/GetProductDetail", params=values, allow_redirects=True)

class MyTaskSet(TaskSet):
    tasks = {login: 2, urun:1, urun_sorgulama:1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class UrunTaskSet(TaskSet):
    tasks = {urun:1, urun_sorgulama:1 }

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000