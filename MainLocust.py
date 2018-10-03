from LoginPhase import ITSLogin
from UrunSorguPhase import ITSUrunSorgu, ITSLogin
from locust import TaskSet, task,HttpLocust, seq_task
class UrunTask(TaskSet):

    def on_start(self):
        self.urun = ITSUrunSorgu(self.client)

    @task(2)
    def login(self):
        self.urun.Login()

    @task(1)
    def urun_sorgu(self):
        self.urun.isLogon()
        if self.urun.account_login:
            self.urun.urun()
        else:
            self.urun.Login()


    @task(1)
    def urun_sorgu_gtin_sn(self):

        if self.urun.account_login:
            self.urun.gtin_sn()
        else:
            self.urun.isLogon()


    @task(1)
    def urun_sorgu_urun_hareketleri(self):

        if self.urun.account_login:
            self.urun.get_urun_hareketleri()
        else:
            self.urun.isLogon()


    @task(1)
    def urun_sorgu_get_stakeholder(self):

        if self.urun.account_login:
            self.urun.get_stakeholder()
        else:
            self.urun.isLogon()


class MyLocust(HttpLocust):
    task_set = UrunTask
    min_wait = 5000
    max_wait = 15000