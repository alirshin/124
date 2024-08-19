# python
def get_apartment_info():
    village = {
        "1": {
            "124": {
                "1": {
                    "Location " : "33.379583423052594, 52.369688268548494",
                    "کد پستی" : " 90000000003",
                    "شماره بدنه کنتور برق" : " 3000000009",
                    "شناسه پرداخت قبض برق" : " 60000000002",
                    "شماره اشتراک برق" : " 9500000000003",
                    "لینک پرداخت اینترنتی قبض برق" : "https://bargheman.com/home",
                    "شماره بدنه کنتور گاز" : " 60000000000004",
                    "شناسه پرداخت قبض گاز" : " 600000000001",
                    "شماره اشتراک کنتور گاز" : " 600000000000001",
                    "link web  gaz: " : "https://ebill.tehrangasco.ir/",
                },
                # دیگر واحدهای واحد شماره ۱
                # ...
            },
            # دیگر واحد‌های زون شماره ۱
            # ...
        },
        # دیگر زون‌ها
        # ...
    }
    # درخواست شماره زون از کاربر

_------------------------+++--------🤣🤣🤣🤣🤣🤣❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗



import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')
print('      _______ _      __________________       _______ _______ _______ _______\n'
'     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )\n'
'     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |\n'
'     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |\n'
'     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |\n'
'     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |\n'
'     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |\n'
'     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)\n')
print ("[+] 关于脚本:")
print ("[-] 你能获取Warp+有限流量.")
print ("[-] 版本: 4.0.0")
print ("--------")
print ("[+] 此脚本的作者：ALIILAPRO") 
print ("[-] SITE: aliilapro.github.io") 
print ("[-] TELEGRAM: aliilapro")
print ("--------")
referrer = input("[#] Enter the WARP+ ID:")
def genString(stringLength):
        try:
                letters = string.ascii_letters + string.digits
                return ''.join(random.choice(letters) for i in range(stringLength))
        except Exception as error:
                print(error)                    
def digitString(stringLength):
        try:
                digit = string.digits
                return ''.join((random.choice(digit) for i in range(stringLength)))    
        except Exception as error:
                print(error)        
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
        try:
                install_id = genString(22)
                body = {"key": "{}=".format(genString(43)),
                                "install_id": install_id,
                                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                                "referrer": referrer,
                                "warp_enabled": False,
                                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                                "type": "Android",
                                "locale": "es_ES"}
                data = json.dumps(body).encode('utf8')
                headers = {'Content-Type': 'application/json; charset=UTF-8',
                                        'Host': 'api.cloudflareclient.com',
                                        'Connection': 'Keep-Alive',
                                        'Accept-Encoding': 'gzip',
                                        'User-Agent': 'okhttp/3.12.1'
                                        }
                req         = urllib.request.Request(url, data, headers)
                response    = urllib.request.urlopen(req)
                status_code = response.getcode()        
                return status_code
        except Exception as error:
                print(error)        

g = 0
b = 0
while True:
        result = run()
        if result == 200:
                g = g + 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
                print("")
                animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
                for i in range(len(animation)):
                        time.sleep(0.5)
                        sys.stdout.write("\r[+] Preparing... " + animation[i % len(animation)])
                        sys.stdout.flush()
                print(f"\n[-] 使用 ID: {referrer}")    
                print(f"[:)] {g} GB 已经成功增加到你的warp+账号中.")
                print(f"[#] Total: {g} Good {b} Bad")
                print("[*] 18秒后, 一个新的增加warp+流量的请求将会发送, 退出脚本请按ctrl+c.")
                time.sleep(18)
        else:
                b = b + 1
                os.system('cls' if os.name == 'nt' else 'clear')
                print("")
                print("                  WARP-PLUS-CLOUDFLARE (script)" + " By ALIILAPRO")
                print("")
                print("[:(] 错误，正在连接服务中.")
                print(f"[#] Total: {g} Good {b} Bad")        