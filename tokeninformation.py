import json
import requests

def temizle():
   print("\n" * 100)
   baslangic
print('''


████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ██╗███╗░░██╗███████╗░█████╗░
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██║████╗░██║██╔════╝██╔══██╗
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║██╔██╗██║█████╗░░██║░░██║
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║██║╚████║██╔══╝░░██║░░██║
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ██║██║░╚███║██║░░░░░╚█████╔╝
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░


█▄▄ █▄█   █▄░█ █ █▄▀ █▀█ █▄░█   █▀█ █▀▀   █▀▄ █ █▀ ▄▀█ █▀ ▀█▀
█▄█ ░█░   █░▀█ █ █░█ █▄█ █░▀█   █▄█ █▀░   █▄▀ █ ▄█ █▀█ ▄█ ░█░
''')
istek = requests.Session()
token = input("Token giriniz: ")
agent = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }


print('''
 [1] : Token Info
 [çık] : Çıkış
 [temizle] : Terminal'i temizle.
''')

def tokeninfo():
   baglanti = istek.get('https://canary.discord.com/api/v6/users/@me', headers=agent, timeout=10)
   response = json.loads(baglanti.content)

   if baglanti.status_code == 403:
      print("Girmiş olduğunuz token hatalı.")
      baslangic()
   elif baglanti.status_code == 401:
      print("Girmiş olduğunuz token hatalı.")
      baslangic()
   else:
      print(token + " doğrulandı.")
      infotk = f'''\n   Kullanıcı Adı: {response['username']}#{response['discriminator']}   ID: {response['id']}\n   Eposta: {response['email']}   Telefon: {response['phone']}\n   Ülke(Dil): {response['locale']}\n'''
      print(infotk)
      baslangic()




def baslangic():
   girdi = input("Komut: ")
   if girdi == "çık":
      print("Görüşmek üzere!")
      exit()
   elif girdi == "temizle":
      temizle()
   elif girdi == "1":
      tokeninfo()
      baslangic()
   else:
      print("Üzgünüm, komut bulunamadı!")
      baslangic()

baslangic()