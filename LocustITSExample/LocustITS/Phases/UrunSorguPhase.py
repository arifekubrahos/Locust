from LocustITS.Phases.LoginPhase import ITSLogin
from LocustITS.Helpers.GenerateConstantValues import ITSConstantValues
from LocustITS.Helpers.Log import LogFile
from bs4 import BeautifulSoup


class ITSUrunSorgu():
    def __init__(self, client):
        self.client = client
        self.login = ITSLogin(client)
        self.account_login = False
        self.LogFile = LogFile()
        self.constant_values = ITSConstantValues()

    def Login(self):
        self.login.Login()
        if self.login.is_login:
            self.account_login = True

    def isLogon(self):
        name = "Kullanıcı içeride mi?"
        with self.client.get("/Account/IsLogon", name=name, catch_response=True) as response:
            if response.content == b"false":
                LogFile.log_error(message= "Kullanici disarida, Status code: " + response.status_code + "\n")
                self.account_login = False
                response.failure("Kullanıcı içeride mi? Failure")
            else:
                self.account_login = True
                response.success()

    def urun(self):
        name = "Ürün sorgulama sayfası"
        response = self.client.get("/urun/urun_sorgulama", name= name)
        if not response.ok:
            LogFile.log_error(message="Urun sorgu sayfasi /GET, Status code:%d" %response.status_code + "\n")


    def gtin_sn(self):
        variables =self.constant_values.create_gtin_sn()
        name = "Ürün sorgusu"
        with self.client.get("/Product/GetProductDetail", params=variables, name=name, catch_response=True) as response:
            #response handle
            soup = BeautifulSoup(response.text)
            test = soup.find_all("div", class_="note note-danger")
            print (len(test))
            if len(test) >= 1:
                LogFile.log_error(message="Urun sorgu with gtin and sn, Status code: %d" % response.status_code + "\n")
                response.failure("Urun sorgu with gtin and sn: Failure")


    def get_urun_hareketleri(self):
        variables = self.constant_values.create_gtin_sn()
        name= "Ürün hareketleri"
        response = self.client.get("/Product/GetOperationList", params=variables, name=name)
        if not response.ok:
            LogFile.log_error(message = "urun hareketleri failed, Status code: %d"%response.status_code+ "\n")
            response.failure("No data")

    def get_stakeholder(self):
        variables = self.constant_values.create_gln()
        name ="Paydaş bilgileri pop-up"
        response = self.client.post("/Stakeholder/GetStakeholder",name=name,params=variables)
        soup = BeautifulSoup(response.text)
        test = soup.find_all("div", class_="error")
        if len(test) >= 1:
            LogFile.log_error(message= "Getstakeholder failed, Status code: %d" % response.status_code + "\n")
            response.failure("GetStakeholder: Failure")

    def get_drug(self):
        variables= self.constant_values.create_gtin()
        name = "İlaç bilgileri pop-up"
        response = self.client.post("/Drug/GetDrug", name=name, params=variables)
        soup = BeautifulSoup(response.text)
        test = soup.find_all("div", class_="error")
        if len(test) >= 1:
            LogFile.log_error(message = "Getdrug failed, Status code: %d"% response.status_code+ "\n")
            response.failure("Getdrug: Failure")


