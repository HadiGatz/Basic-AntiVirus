import requests

url = 'https://www.virustotal.com/api/v3/files'

API_KEY = ""

headers = {
    "x-apikey": API_KEY
}

file = open(input("Enter your file name: "))

def check_if_corrupted():
    try:
        file.read()
    except:
        print("The file is corrupt.")

response = requests.get(url, files={'file': file}, headers=headers)

if response.status_code == 200:
    print("File successfully uploaded and scanned.")
    scan_results = response.json()
    print(scan_results)  
else:
    print("Error")
