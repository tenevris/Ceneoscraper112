import requests 


respons = requests.get('https://www.ceneo.pl/98318687#tab=reviews')
 
print(respons.text)