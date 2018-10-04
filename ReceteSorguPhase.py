from  LoginPhase import ITSLogin

class ITSReceteSorgu():
    def __init__(self, client):
        self.client = client
        self.login = ITSLogin(client)
        self.account_login = False

    def Login(self):
        self.login.Login()
        if self.login.is_login:
            self.account_login = True

    def isLogon(self):
        response = self.client.get("/Account/IsLogon")
        if response.text == "true":
            self.log_success("Kullanici iceride" + "\n")
            self.account_login = True
        else:
            self.log_error("Kullanici disarida, Status code: " + str(response.status_code) + "\n")
            self.account_login = False

    def recete(self):
        response = self.client.get("/urun/recete_sorgulama")
        if not response.ok:
            self.log_error("recete failed, Status code: " + str(response.status_code) + "\n")
        else:
            self.log_success("recete success" + "\n")
            #self.write_html(response.text)

    def recete_sorgu(self):
        varibles = {"_pres_record_number": ""}
        response = self.client.get("/Product/GetPrescriptionList", params=varibles, allow_redirects= True )
        if response.ok:
            self.log_success("recete sorgu success" + "\n")
            self.write_html(response.text)
        else:
            self.log_error("recete sorgu error, Status code: " + str(response.status_code) + "\n")


    def log_error(self, message):
        with open("ErrorLog.txt", "a") as file:
            file.write(message)
        pass

    def log_success(self, response):
        with open("SuccessLog.txt", "a") as file:
            file.write(response)
        pass

    def write_html(self, text):
        with open("htmls.html", "w") as file:
            file.write(text)
        pass