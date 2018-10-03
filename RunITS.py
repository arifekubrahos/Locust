from locust.clients import HttpSession
from LoginPhase import ITSLogin
from UrunSorguPhase import  ITSUrunSorgu

client = HttpSession('http://localhost:55018')
app = ITSUrunSorgu(client)
app.isLogon()
