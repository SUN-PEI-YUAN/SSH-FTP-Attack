from socket import * 
import sys, time
from datetime import datetime

host = ''
max_port = 65535
min_port = 1

def scan_host(host, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
         
        code = s.connect_ex((host, port))

        if code == 0:
            r_code = code
            s.close()
    except Exception as e:
        pass

    return r_code

try:
    host = input("[*] 輸入欲掃瞄之主機: ")
except KeyboardInterrupt:
    print("\n\n[*] 取消掃描！")
    print("[*] 程式結束執行！")
    sys.exit(1)

hostip = gethostbyname(host)
print("\n[*] Host: %s IP: %s" % (host, hostip))
print("[*] 掃瞄於 %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
    try:
        response = scan_host(host, port)

        if response == 0:
            print("[*] Port %d: Open" % port)
    except Exception as e:
        pass

stop_time = datetime.now()
totalTimeDuration = stop_time - start_time
print("\n[*] Scanning Finished At %s ..." % (time.strftime("%H:%M:%S")))
print("[*] Scanning Duration: %s ..." % totalTimeDuration)
print("[*] 掃瞄完畢 !")
