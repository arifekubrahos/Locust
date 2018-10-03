import datetime, json

class ITSLogin():
    def __init__(self,client):
        self.is_login = False
        self.client = client

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


    def log_error(self, message):
        with open("ErrorLog.txt", "a") as file:
            file.write(message )
        pass

    def log_success(self, response):
        with open("SuccessLog.txt","a") as file:
            file.write(response)
        pass
