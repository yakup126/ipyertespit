import geoip2.database
import subprocess
import os
from colorama import Fore,Style
os.system("clear")


print(Fore.RED+"""
 ___ ____    ___ ____ _____ ___ _   _ ____    _    ____      _  _____ ___
|_ _|  _ \  |_ _/ ___|_   _|_ _| | | | __ )  / \  |  _ \    / \|_   _|_ _|
 | || |_) |  | |\___ \ | |  | || |_| |  _ \ / _ \ | |_) |  / _ \ | |  | |
 | ||  __/   | | ___) || |  | ||  _  | |_) / ___ \|  _ <  / ___ \| |  | |
|___|_|     |___|____/ |_| |___|_| |_|____/_/   \_\_| \_\/_/   \_\_| |___|
""")


print(Style.RESET_ALL)

print("Bu Program Yakup Eroglu Tarafından Yazılmıstır.\nDB Her Salı Güncellenmektedir. Yasa Dışı Kullanım Yasaktır")
ip=input("IPV4 Adresi Girin: ")

client = geoip2.database.Reader('GeoLite2-City.mmdb')

response=client.city(ip)
Ulke=response.country.name
Sehir=response.city.name
postcode=response.postal.code
x=response.location.latitude
y=response.location.longitude
a=response.subdivisions.most_specific.name
print(f"""
Ulke:      {Ulke}
Sehir:     {Sehir}
Posta Kodu:{postcode}
Spesifik ad:{a}
Kordinatlar:{x},{y}

""")
