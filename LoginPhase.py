import datetime, json

class ITSLogin():
    def __init__(self,client):
        self.is_login = False
        self.client= client

    def Login(self):
        self.client.cookies.clear()
        variables={"_email":"", "_password":""}
        name = "/Login"
        response = self.client.post("/Account/Login",variables, allow_redirects=True, name= name)
        json_result = json.loads(response.text)
        if json_result["Success"] == False:
            self.log_error(str(datetime.datetime.now())+"\nLogin failed, Status Code: "+ str(response.status_code)+"\n")
        else:
            self.log_success(str(datetime.datetime.now())+"\nLogin success: "+response.text+"\n")
            self.is_login =True

    # def urun(self):
    #     name = "/urun/urun_sorgulama"
    #     response = self.client.get("/urun/urun_sorgulama", name=name)
    #     if not response.ok:
    #         self.log_error("Urun failed, Status code: "+ response.status_code,name)
    #     else:
    #         self.log_success("Urun success "+response.text)

    def log_error(self, message):
        with open("ErrorLog.txt", "a") as file:
            file.write(message )
        pass

    def log_success(self, response):
        with open("SuccessLog.txt","a") as file:
            file.write(response)
        pass
