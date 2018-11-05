import datetime, json
from LocustITS.Helpers.Log import LogFile

class ITSLogin():
    def __init__(self,client):
        self.is_login = False
        self.client = client

    def Login(self):

        self.client.cookies.clear()
        variables={"_email":"admin@tiga.com.tr", "_password":"123qwe"}
        name = "KULLANICI GİRİŞİ"
        with self.client.post("/Account/Login", params=variables, allow_redirects=True, name= name, catch_response=True) as response:

            json_result = json.loads(response.text)
            if json_result["Success"] == False:
                response.failure("Login failed")
                LogFile.log_error(message = datetime.datetime.now()+"\nLogin failed, Status Code: "+ response.status_code+"\n")
            else:
                self.is_login =True
                response.success()

    def Logout(self):
        name= "KULLANICI ÇIKIŞI"
        self.client.get("/Account/Logout", name=name, allow_redirects=True)
