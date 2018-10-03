from locust.clients import HttpSession
from LoginPhase import ITSLogin
from UrunSorguPhase import  ITSUrunSorgu
client = HttpSession('http://localhost:55018')
app = ITSUrunSorgu(client)
app.isLogon()
app.urun()
app.isLogon()
app.gtin_sn()
app.isLogon()
app.get_urun_hareketleri()
app.isLogon()
app.get_stakeholder()