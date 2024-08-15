
from bs4 import BeautifulSoup
import cloudscraper
from datetime import datetime
import requests
import json




a = datetime.now()
simdi=datetime.ctime(a)

with open("app.json","r") as jsn :
    data= json.load(jsn)
def send_msg(text):
    token = data["bottoken"]
    chat_id = data["chatid"]
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
    results = requests.get(url_req)
    print(results.json())



def scraperkodları():
    scraper = cloudscraper.create_scraper()
    url = "https://www.turkhackteam.org/forumlar/-/index.rss"
    r = scraper.get(url)
    soup = BeautifulSoup(r.content,"xml")
    sonuc=soup.find_all("item")

    for i in range(len(sonuc)):
        deger=sonuc[i]
        title = deger.find('title').text
        link = deger.find('link').text
        tarih=deger.find("pubDate").text
        tarih_str=tarih
        donusum=datetime.strptime(tarih_str, "%a, %d %b %Y %H:%M:%S %z")
        sonhal=donusum.strftime("%a %b %d %H:%M:%S %Y")

        if sonhal ==simdi:
            message=f"Konu Başlığı: {title}\nLink: {link}\nTarih: {tarih}\n Durum: Yeni Konu"
            send_msg(message)
        else:
            message=f"Konu Başlığı: {title}\nLink: {link}\nTarih: {tarih}\n Durum: Eski Konuya yeni mesaj" 
            send_msg(message) 


scraperkodları()