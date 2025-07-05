Subdomain Enumeration Tool

-A Python-based tool to perform subdomain enumeration using multithreading and HTTP requests. It scan the target domain.

PREREQUISITES
- DNS basics = Understand what subdomains are (e.g., api.youtube.com)
- Python syntax	= Writing loops, functions, file I/O
- requests module =	To make HTTP GET requests
- Threading in Python	= To speed up subdomain checks
- Exception handling	= To prevent crashes on invalid subdomains

Features
- Loads subdomains from `subdomains.txt`
- Uses threads to check subdomain availability
- Saves discovered subdomains to `discovered_subdomains.txt`

 Requirements
- Python 3
- `requests` library

PROJECT FILE STRUCTURE

-your_project_folder
-subdomain_enumerator.py
-subdomains.txt
-discovered_subdomains.txt  ← created after running script

PROJECT FILES

-subdomain_enumerator.py = main script
-subdomains.txt = list of subdomains to check
-discovered_subdomains.txt = output (active subdomains)

STEP-BY-STEP SOLUTION:

STEP 1: Prepare Your Files
-Create a file named subdomains.txt in the same folder.
[Subdomain_TXT_file](https://github.com/user-attachments/assets/b8ac92fa-df8a-49d7-80a1-284c18254e4a)

STEP 2: Install Required Python Module
-Open your terminal or command prompt and run:
pip install requests

STEP 3: Write the Script
-Create a file called subdomain_enumerator.py,and paste the following code:
import requests
import threading

domain = 'Google.com'

# Read potential subdomains
with open('subdomain.txt') as file:
    subdomains = file.read().splitlines()

discovered_subdomains = []
lock = threading.Lock()

def check_subdomain(subdomain):
    url = f'http://{subdomain}.{domain}'
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print("[+] Discovered subdomain:", url)
            with lock:
                discovered_subdomains.append(url)
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        print(f"[!] Timeout trying: {url}")

# Start threads
threads = []
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Save results to file
with open("discovered_subdomains.txt", 'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

print("\n✔️ Enumeration completed. Results saved to 'discovered_subdomains.txt'")

[Subdomain_tool_code_python](https://github.com/user-attachments/assets/2c01c736-e218-4451-8daf-32fa8076510d)


STEP 4: Run the Script
-In the terminal, run:
python subdomain_enumerator.py
[Terminal_output](https://github.com/user-attachments/assets/27708736-cfdb-484b-92ab-729fcb63c021)

STEP 5: Discovered_subdomains txt file after running the script[OUTPUT]
[Output](https://github.com/user-attachments/assets/a1338569-0987-4ecc-95ce-5e71a4889d22)

Project created by Devki Prajapati.
