import requests,os
from bs4 import BeautifulSoup

print('''
_________                        __           __________        .__              
\_   ___ \_______ ___.__._______/  |_  ____   \______   \_______|__| ____  ____  
/    \  \/\_  __ <   |  |\____ \   __\/  _ \   |     ___/\_  __ \  |/ ___\/ __ \ 
\     \____|  | \/\___  ||  |_> >  | (  <_> )  |    |     |  | \/  \  \__\  ___/ 
 \______  /|__|   / ____||   __/|__|  \____/   |____|     |__|  |__|\___  >___  >
        \/        \/     |__|                                           \/    \/ 
''')

fuck = requests.get('https://ablocks.dw.am/exchange/upbit')
shit = BeautifulSoup(fuck.content, 'html.parser')

while True :

    b = input('알아볼 암호화폐를 입력하세요.(BTC,ETH,DOGE) : ')

    if b == 'BTC' :
        print('비트코인 시세 : '+ shit.find_all('td', class_="text-right")[6].text)
    if b == 'ETH' :
        print('이더리움 시세 : ' + shit.find_all('td', class_="text-right")[15].text)
    if b == 'DOGE' :
        print('도지코인 시세 : ' + shit.find_all('td', class_="text-right")[60].text)

    
        

        
        
        
