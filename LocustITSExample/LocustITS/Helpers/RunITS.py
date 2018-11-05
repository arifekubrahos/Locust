from locust.clients import HttpSession
from LocustITS.Phases.LoginPhase import ITSLogin
from LocustITS.Phases.UrunSorguPhase import ITSUrunSorgu
from LocustITS.Phases.ReceteSorguPhase import ITSReceteSorgu

client = HttpSession('http://localhost:55001')

app = ITSUrunSorgu(client)
app.Login()
app.gtin_sn()