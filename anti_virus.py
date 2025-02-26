import os
import requests
from termcolor import colored

url = 'https://www.virustotal.com/api/v3/files'
API_KEY = ""

headers = {
    "x-apikey": API_KEY
}

global report

# getting the user's file via the terminal
def get_user_file():
    while True:
        try: 
            file_path = input("Enter your file name: ")
            file = open(file_path, "rb")
            return file, file_path
        except FileNotFoundError:
            print("Your file was not found.\nTry again.")

# checks if the file is corrupted, returns False if not
def check_if_corrupted(file):
    try:
        with open(file, "rb") as data:
            data.read()
        return False
    except:
        print("The file is corrupt.")
        return True

# requests a scan on a file from the API
def scan_file(file):
    response = requests.post(url, files={'file': file}, headers=headers)
    return response

# retrieves the scan results from the API
def retrieve_scan_results(scan_url):
    analysis = requests.get(url=scan_url, headers=headers)
    return analysis

# prints the scan results to the terminal
def print_analysis_results(analysis):
    global report
    report = '''Your file was checked by 70+ Anti-Virus softwares.
    Be aware of "malicious" and "suspicious" - those are stats
    that show you viruses/suspicion on viruses in your
    file.
    ----------------------------------------'''
    print(colored("Your file was checked by 70+ Anti-Virus softwares.", "green"))
    print("------------------------------------------\n")
    for x, y in analysis.items():
        if y > 0:
            print(x, colored(y, "red"))
        elif y == 0:
            print(x, colored(y, "green"))
        report += f"{x} : {y}\n"
    print("------------------------------------------")
    print("Thank you for using our service.")
    return analysis

# performs an analysis on a directory. this function is recursive
def full_analysis_directory(directory, target_directory):
    for item in os.listdir(directory):
        current_path = os.path.join(directory, item) 
        if os.path.isfile(current_path):
            full_analysis(current_path, target_directory)
        elif os.path.isdir(current_path):
            full_analysis_directory(current_path, target_directory)

# exports the analysis to a .txt file
def export_analysis(directory, analysis, file_name):
    split_tup = os.path.splitext(os.path.basename(file_name))  
    file_placement = os.path.join(directory, f"{split_tup[0]}-analysis.txt")
    with open(file_placement, "w") as f:
        f.write(report)

# full analysis on a file
def full_analysis(file_path, target_directory):
    if not check_if_corrupted(file_path):
        with open(file_path, "rb") as file:
            response = scan_file(file)
            if response.status_code == 200:
                scan_results = response.json()
                scan_url = scan_results['data']['links']['self']
                analysis = retrieve_scan_results(scan_url)
                if analysis.status_code == 200:
                    analysis_results = analysis.json()['data']['attributes']['stats']
                    print_analysis_results(analysis_results)
                    export_analysis(target_directory, analysis_results, file_path)
                else:
                    print("Failed to retrieve analysis results.")
            else:
                print("Failed to scan the file.")

if __name__ == "__main__":
    file, file_path = get_user_file()
    target_directory = input("Enter the directory to save the analysis report: ")
    full_analysis(file_path, target_directory)
