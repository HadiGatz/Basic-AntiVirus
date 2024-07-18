import requests

url = 'https://www.virustotal.com/api/v3/files'

API_KEY = "d6970bf852d449af239cc1e7026f11ecdf69c5189ff6451c173068ef6e311c9c"

headers = {
    "x-apikey": API_KEY
}
headers3 = {
    "accept" : "application/json"
}

file = open(input("Enter your file name: "), "rb")

def check_if_corrupted():
    try:
        file.read()
    except:
        print("The file is corrupt.")

response = requests.post(url, files={'file': file}, headers=headers)

if response.status_code == 200:
    print("File successfully uploaded and scanned.")
    scan_results = dict(response.json())
    scan_url = scan_results['data']['links']['self']
    analysis = requests.get(url=scan_url, headers=headers)  
    print(analysis.json())
else:
    print("Error")
