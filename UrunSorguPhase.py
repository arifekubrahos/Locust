from LoginPhase import ITSLogin

class ITSUrunSorgu():
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

    def urun(self):
        response = self.client.get("/urun/urun_sorgulama")
        if not response.ok:
            self.log_error("Urun failed, Status code: "+ str(response.status_code)+ "\n")
        else:
            self.log_success("Urun success" +"\n")
            self.write_html(response.text)


    def gtin_sn(self):
        variables = {"gtin":"", "sn":"",
                     }
        response = self.client.get("/Product/GetProductDetail", params=variables, allow_redirects=True)
        if response.ok:
            self.log_success("Urun sorgu success"+ "\n")
            self.write_html(response.text)
        else:
            self.log_error("urun sorgu error, Status code: "+ str(response.status_code)+ "\n")

    def barkod(self):
        variables = {""}
        response = self.client.post("/Product/GetProductDetail", params=variables, allow_redirects=True)
        if response.ok:
            self.log_success("")
        else:
            self.log_error("")

    def get_urun_hareketleri(self):
        variables = {"gtin": "", "sn": ""}
        response = self.client.get("/Product/GetOperationList", params=variables, allow_redirects=True)
        if response.ok:
            self.log_success("urun hareketleri success "+"\n")
            self.write_html(response.text)
        else:
            self.log_error("urun hareketleri failed, Status code: "+ str(response.status_code)+ "\n")

    def get_stakeholder(self):
        variables = {"gln":""}
        response = self.client.post("/Stakeholder/GetStakeholder",params=variables)
        if response.ok:
            self.log_success("getstakeholder success " + "\n")
            self.write_html(response.text)
        else:
            self.log_error("getstakeholder failed, Status code: " + str(response.status_code) + "\n")


    def log_error(self, message):
        with open("ErrorLog.txt", "a") as file:
            file.write(message)
        pass

    def log_success(self, response):
        with open("SuccessLog.txt","a") as file:
            file.write(response)
        pass

    def write_html(self, text):
        with open("htmls.html", "w") as file:
            file.write(text)
        pass