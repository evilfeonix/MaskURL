import os, sys, time
from datetime import datetime

try:
    import requests
    from colorama import Fore
except:
    print("""
     __  __   v[1.0]  _    _   _ ____  _     
    |  \/  | __ _ ___| | _| | | |  _ \| |
    | |\/| |/ _` / __| |/ / | | | |_) | |
    | |  | | (_| \__ \   <| |_| |  _ <| |___
    |_|  |_|\__,_|___/_|\_\\\___/|_| \_\_____|
              www.evilfeonix.com                         
    """)
    print('\033[31m [!] Some Libraries are missing!')
    print('\033[36m [●] Installing missing Libraries...\033[0m')
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('clear || cls')



def mask_url(service, original_url, alias=None, api_key=None):
    try:
        hit_count = open('cookies','r')
        hit_count = hit_count.readlines().strip()
        hit = hit_count[0] if hit_count[0] else 0
        date = hit_count[1] if hit_count[1] else str(datetime.now())[:10]
        if int(hit) == int('3') and date == str(datetime.now())[:10]:
            date = str(datetime.now())[:10]
            add = open('cookies','a')
            add.write(data)
            return f"{Fore.RED}You have reach Your limit for using this tool Today!,\n\tPlease Try Again Tomorrow.{Fore.WHITE}\n"
    except:pass

    try:
        if service == 'bitly':
            if not api_key:
                return f"{Fore.RED}Bitly API key is required!{Fore.WHITE}\n"
            url = "https://api-ssl.bitly.com/v4/shorten"
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {"long_url": original_url}
            if alias:
                payload["custom_bitlink"] = alias
            response = requests.post(url, json=payload, headers=headers)
            hit += 1
            add = open('cookies','w')
            add.write(hit)
        
        elif service == 'tinyurl':
            url = "https://api.tinyurl.com/create"
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {"url": original_url}
            if alias:
                payload["alias"] = alias
            response = requests.post(url, json=payload, headers=headers)
            hit += 1
            add = open('cookies','w')
            add.write(hit)
        
        elif service == 'shortly':
            url = "https://shortly_api_service_url/shorten"  # Replace with Shortly's actual API URL
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {"url": original_url}
            if alias:
                payload["alias"] = alias
            response = requests.post(url, json=payload, headers=headers)
            hit += 1
            add = open('cookies','w')
            add.write(hit)
        
        else:
            return f"{Fore.RED}Invalid service! Choose from 'bitly', 'tinyurl', or 'shortly'.{Fore.WHITE}\n"
        
        if response.status_code == 200:
            return f"{Fore.GREEN}{response.json().get('link', 'Error: No link returned!')}{Fore.WHITE}\n"
        else:
            return f"{Fore.RED}Error: {response.status_code} - {response.text}{Fore.WHITE}\n"

    except Exception as e:
        return f"{Fore.RED}An error occurred: {e}{Fore.WHITE}\n"

if __name__ == "__main__":
    os.system('clear || cls')
    print("""
     __  __   v[1.0]  _    _   _ ____  _     
    |  \/  | __ _ ___| | _| | | |  _ \| |
    | |\/| |/ _` / __| |/ / | | | |_) | |
    | |  | | (_| \__ \   <| |_| |  _ <| |___
    |_|  |_|\__,_|___/_|\_\\\___/|_| \_\_____|
              www.evilfeonix.com                         
    """)
    service = input(f"{Fore.CYAN}[+] Choose a service (bitly, tinyurl, shortly):{Fore.WHITE} ").strip().lower()
    original_url = input(f"{Fore.CYAN}[+] Enter the URL to shorten:{Fore.WHITE} ").strip()
    alias = input(f"{Fore.CYAN}[+] Enter a custom alias (optional):{Fore.WHITE} ").strip()
    api_key = input(f"{Fore.CYAN}[+] Enter your API key (if required):{Fore.WHITE} ").strip()
    
    maskedURL = mask_url(service, original_url, alias if alias else None, api_key if api_key else None)
    time.sleep(3)
    print(f"{Fore.CYAN}Shortened URL: {maskedURL}")
