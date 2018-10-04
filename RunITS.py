from locust.clients import HttpSession
from LoginPhase import ITSLogin
from UrunSorguPhase import  ITSUrunSorgu
from ReceteSorguPhase import ITSReceteSorgu
client = HttpSession('http://localhost:55018')
app = ITSLogin(client)
app.Login()
app.Logout()