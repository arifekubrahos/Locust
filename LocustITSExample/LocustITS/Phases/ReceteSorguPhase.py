from LocustITS.Phases.LoginPhase import ITSLogin
from LocustITS.Helpers.Log import LogFile
from LocustITS.Helpers.GenerateConstantValues import ITSConstantValues
from bs4 import BeautifulSoup


class ITSReceteSorgu():
    def __init__(self, client):
        self.client = client
        self.login = ITSLogin(client)
        self.account_login = False
        self.log_file = LogFile()
        self.constant_value = ITSConstantValues()

    def Login(self):
        self.login.Login()
        if self.login.is_login:
            self.account_login = True

    def isLogon(self):
        name= "Kullanıcı içeride mi?"
        response = self.client.get("/Account/IsLogon", name= name)
        if response.text == "true":
            self.account_login = True
        else:
            LogFile.log_error(message= "Kullanici disarida, Status code: " + response.status_code + "\n")
            self.account_login = False

    def recete(self):
        name= "Reçete sorgulama sayfası"
        response = self.client.get("/urun/recete_sorgulama", name= name)
        if not response.ok:
            LogFile.log_error( message= "recete failed, Status code: " + response.status_code + "\n")
            response.failure("recete failed: Failure")

    def recete_sorgu(self):
        variables = self.constant_value.create_pres_id()
        name="Reçete sorgusu"
        response = self.client.get("/Product/GetPrescriptionList", params=variables, name=name, allow_redirects= True )
        soup = BeautifulSoup(response.text)
        test = soup.find_all("td", class_="dataTables_empty")
        if len(test) >= 1:
            LogFile.log_error(message="recete detail error, Status code: " + response.status_code + "\n")
            response.failure("recete detail: Failure")


    def recete_detail(self):
        variables = self.constant_value.create_notification_id()
        name="Reçete detayı sayfası"
        response= self.client.get("/Product/PrescriptionDetail", name= name, params=variables, allow_redirects=True)
        if not response.ok:
            LogFile.log_error(message="recete sorgu error, Status code: " + response.status_code + "\n")

