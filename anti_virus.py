import requests
import time
from termcolor import colored


url = 'https://www.virustotal.com/api/v3/files'

API_KEY = "d6970bf852d449af239cc1e7026f11ecdf69c5189ff6451c173068ef6e311c9c"

headers = {
    "x-apikey": API_KEY
}

def get_user_file():
    while True:
      try: 
          file = open(input("Enter your file name: "), "rb")
          return file
      except FileNotFoundError:
          print("Your file was not found.\nTry again.")


file = get_user_file()

def check_if_corrupted():
    try:
        file.read()
    except:
        print("The file is corrupt.")

def scan_file(file):
    response = requests.post(url, files={'file': file}, headers=headers)
    return response

def retrieve_scan_results(url):
    analysis = requests.get(url=url, headers=headers)
    return analysis

def print_analysis_results(analysis):
    print(colored("Your file was checked by 70+ Anti-Virus softwares.", "green"))
    print("------------------------------------------")
    for x, y in analysis.items():
        if y > 0:
            print(x, colored(y, "red"))
        elif y == 0:
            print(x, colored(y, "green"))
        time.sleep(1)
    print("------------------------------------------")
    print("Thank you for using our service.")

response = scan_file(file)

if response.status_code == 200:
    print("File successfully uploaded and scanned.")
    scan_results = dict(response.json())
    scan_url = scan_results['data']['links']['self']
    analysis = retrieve_scan_results(scan_url) 
    print_analysis_results(analysis.json()['data']['attributes']['stats'])
else:
    print(f"Error {response.status_code}")
