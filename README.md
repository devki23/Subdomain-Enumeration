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

PROJECT FILES:<br>

<br>
-subdomain_enumerator.py = main script
<br>
-subdomains.txt = list of subdomains to check
<br>
-discovered_subdomains.txt = output (active subdomains)
<br>

STEP-BY-STEP SOLUTION:
<br>

STEP 1: Prepare Your Files
<br>
-Create a file named subdomains.txt in the same folder.
[Subdomain_TXT_file](https://github.com/user-attachments/assets/b8ac92fa-df8a-49d7-80a1-284c18254e4a)
<br>

STEP 2: Install Required Python Module
<br>
-Open your terminal or command prompt and run:
"pip install requests"
<br>


STEP 3: Write the Script
<br>
-Create a file called subdomain_enumerator.py,and use following code:
[Subdomain_tool_code_python](https://github.com/user-attachments/assets/2c01c736-e218-4451-8daf-32fa8076510d)
<br>


STEP 4: Run the Script
<br>
-In the terminal, run:
python subdomain_enumerator.py
[Terminal_output](https://github.com/user-attachments/assets/27708736-cfdb-484b-92ab-729fcb63c021)
<br>

STEP 5: Discovered_subdomains txt file after running the script[OUTPUT]
<br>
[Output](https://github.com/user-attachments/assets/a1338569-0987-4ecc-95ce-5e71a4889d22)
<br>

Project created by Devki Prajapati.
