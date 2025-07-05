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
