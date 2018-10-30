from locust.clients import HttpSession
from LoginPhase import ITSLogin
from UrunSorguPhase import  ITSUrunSorgu
from ReceteSorguPhase import ITSReceteSorgu

client = HttpSession('http://localhost:55017')

app = ITSUrunSorgu(client)
app.Login()
app.gtin_sn()