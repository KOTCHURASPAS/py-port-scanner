host = "kochura.ru"
first_port = 20
last_port = 21
file_dir = "C:/Users/KOTCHURASPAS/Desktop/SCANNER/"

import socket, colorama, os, time, datetime
os.system('cls')
colorama.init()
ip = socket.gethostbyname(host)
today = time.time()
date = datetime.datetime.fromtimestamp(today)
log_file = open(f"{file_dir}{date:%Y-%m-%d_%H-%M-%S}_{ip}.log", "w")

print(colorama.Fore.YELLOW + "==============================")
log_file.write("==============================\n")
print(colorama.Fore.YELLOW + f"Дата: {date:%Y-%m-%d %H:%M:%S}")
log_file.write(f"Дата: {date:%Y-%m-%d %H:%M:%S}\n")
print(colorama.Fore.YELLOW + f"Хост: {host}")
log_file.write(f"Хост: {host}\n")
print(colorama.Fore.YELLOW + f"IP для сканирования: {ip}")
log_file.write(f"IP для сканирования: {ip}\n")
print(colorama.Fore.YELLOW + "==============================")
log_file.write("==============================\n")

def scan_port(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    if client.connect_ex((ip, port)):
        print(colorama.Fore.RED + f"Порт {port} закрыт. ({ip}:{port})")
        log_file.write(f"Порт {port} закрыт. ({ip}:{port}) \n")
    else:
        print(colorama.Fore.GREEN + f"Порт {port} открыт. ({ip}:{port})")
        log_file.write(f"Порт {port} открыт. ({ip}:{port}) \n")

for i in range(first_port, last_port + 1):
    scan_port(ip, i)
    
print(colorama.Fore.MAGENTA + "Code by #KOTCHURASPAS")
log_file.write("Code by #KOTCHURASPAS\n")