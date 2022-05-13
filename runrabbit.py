import time
import requests
import urllib.request
import whois
import re
import socket
import Url91


print("o================================================================================================================o \n")
#Please, don't touch the banner below, thank you! (Por favor, não mecha no banner, obrigado!)
time.sleep(0.2)
print("  \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m      \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m    \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m  \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m")
time.sleep(0.2)
print("  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m\033[0;36;44m  \033[m  \033[0;36;44m  \033[m      \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m")
time.sleep(0.1)
print("  \033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m\033[0;36;44m  \033[m      \033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m  \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m    \033[0;36;44m  \033[m           By: black-hot-pepper")
time.sleep(0.1)
print("  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m\033[0;36;44m  \033[m      \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m        \033[0;36;47m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;47m  \033[m")
time.sleep(0.1)
print("  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m  \033[0;36;44m  \033[m    \033[0;36;44m  \033[m      \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m  \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m\033[0;36;44m  \033[m\033[0;36;44m  \033[m    \033[0;36;44m  \033[m    \033[0;36;44m  \033[m \n")
time.sleep(0.1)
#Banner's end... (Fim do banner)
print("o===============================================o Run Rabbit o===================================================o \n")

key = "master-key-00100606"
while key == "master-key-00100606":

    help_banner = '\033[0;36mRun 'runrabbit --run --complete' to start or 'runrabbit --run --help' to see the options...\033[m'
    complete_option = 'runrabbit --run --complete'#
    help_option = 'runrabbit --run --help' # 
    simple_port_option = 'runrabbit --run --port' #
    complete_port_option = 'runrabbit --run --ports'
    whois_option = 'runrabbit --run --whois'
    mail_option = 'runrabbit --run --mail'
    
    print(help_banner)
    
    #

    var_start = str(input('\033[0;34m[*] \033[m'))
    if var_start.lower() == help_option:
        print("\n")
        print("Execute: runrabbit --run <options>")
        print("OPTIONS")
        print("     --help               See the help menu")
        print("     --complete           Run the programm with all options")
        print("     --port               Run the program with a port scanner for a specific port")
        print("     --ports              Run the program with a port scanner for all ports")
        print("     --whois              Run the program with a whois scanner")
        print("     --mail               Run the program with a mail scanner \n")
        print("Just use the command with one options...")
    elif var_start.lower() == complete_option:
        time.sleep(0.1)
        print("\033[0;36mLoading...\033[m \n")
        time.sleep(1.2)

        #Domain definition (Definição do domínio)
        print("\033[0;36mType the domain's name:\033[m")
        print("Example: \033[0;33mwww.google.com, www.yahoo.com...\033[m")
        var_domain = input("\033[0;34m[*] \033[m")
        print("\n")
        time.sleep(2.5)

        #Domain http definition (Definição do http do domínio)
        print("\033[0;36mChoose the HTTP type...\033[m")
        print("  | Hyper Text Transfer Protocol Secure     \033[0;36mHTTPS\033[m - (1) |")
        print("  | Hyper Text Transfer Protocol            \033[0;36mHTTP\033[m  - (2) |")
        var_http_definition = int(input("\033[0;34m[*] \033[m"))
        print("\n")

        #Http or https (Http ou https)
        if var_http_definition == 1:

            web_source_https = ("https://{}".format(var_domain))
            print("\033[0;34mScanning\033[m")

            print("\033[0;36mLooking for IP address...\033[m")
            time.sleep(1.6)
            ip_https = socket.gethostbyname(var_domain)

            print("\n\033[0;36mLooking for HTML...\033[m")
            time.sleep(1.6)
            pag_https = Url91.content(web_source_https)
            text_https = pag_https.decode("utf8")

            print("\n\033[0;36mLooking for ports...\033[m")
            time.sleep(1.6)
            ports = [7,20,21,22,23,25,43,53,69,80,123,161,162,179,318,389,411,412,443,465,500,513,546,547,563,636,873,989,990,993,995,1194,1241,2049,3124,3128,4333,5004,5005,5500,5800,6665,6679,6697,8000,8080,33434]
            var = var_domain
            time.sleep(1)

            
            print("\n\033[0;36mLooking for whois...\033[m")
            time.sleep(1.6)
            consult_https = whois.whois(var_domain)
            print("\n\033[0;36mLooking for MAILS...\033[m")
            time.sleep(1.6)

            #Done! (Feito!)
            print("\n\033[0;32mScanning complete!\033[m")
            time.sleep(3)
            print("\033[0;34mRunning on screen...\033[m")
            time.sleep(3)
            print("\n")
            print("\033[0;34mo=============o IP Address o============o\033[m")
            time.sleep(0.5)
            print(ip_https)
            print("\n")
            print("\033[0;34mo================o HTML o===============o\033[m")
            time.sleep(0.5)
            print(text_https)
            print("\n")
            print("\033[0;34mo================o PORTS o==============o\033[m")
            time.sleep(0.5)
            print("\033[1;34mScanning ports in {}, please be patient...\033[m".format(var))
            time.sleep(3)
            for p0rt in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(1)
                code = client.connect_ex((var, p0rt))
                if code == 0:
                    time.sleep(2)
                    print("Trying:", "Port", p0rt)
                    print("Situation: \033[1;32mOPEN\033[m \n")
                else:
                    pass
            print("\n")
            print("\033[0;34mo================o WOIS o===============o\033[m")
            time.sleep(0.5)
            print(consult_https.text)
            print("\n")
            print("\033[0;34mo================o MAILS o==============o\033[m")
            time.sleep(0.5)
            def GetEmailBySite(SiteList):
                for i in SiteList:
                    DataSite = requests.get(i)
                    ReturnRegex = re.findall(f'[\w\.-]+@[\w\\.-]+\.\w+',DataSite.text)
                    if ReturnRegex:
                        return(list(set(ReturnRegex)))
                    else:
                        return "\033[1;31mFailed to find emails!\033[m"

            sites = [web_source_https]
            cont_x=0
            try:
                for x in sites:
                    mails = (GetEmailBySite([x]))
                    if (mails != "None" or mails != None):
                        print("\033[1;34mScanning external mails, wait a second...\033[m")
                        time.sleep(0.1)
                        print("Mail:", mails)
                    cont_x = cont_x+1
            except:
                print(x)
                pass

            print("\n")
        else:
            web_source_http = ("http://{}".format(var_domain))
            print("\033[0;34mScanning \033[m")

            print("\033[0;36mLooking for IP address...\033[m")
            time.sleep(1.6)
            ip_http = socket.gethostbyname(var_domain)

            print("\n\033[0;36mLooking for HTML...\033[m")
            time.sleep(1.6)
            pag_http = Url91.content(web_source_http)
            text_http = pag_http.decode("utf8")

            print("\n\033[0;36mLooking for ports...\033[m")
            time.sleep(1.6)
            ports = [7,20,21,22,23,25,43,53,69,80,123,161,162,179,318,389,411,412,443,465,500,513,546,547,563,636,873,989,990,993,995,1194,1241,2049,3124,3128,4333,5004,5005,5500,5800,6665,6679,6697,8000,8080,33434]
            var = var_domain
            time.sleep(1)

            
            print("\n\033[0;36mLooking for whois...\033[m")
            time.sleep(1.6)
            consult_http = whois.whois(var_domain)
            print("\n\033[0;36mLooking for MAILS...\033[m")
            time.sleep(1.6)

            #Done! (Feito!)
            print("\n\033[0;32mScanning complete!\033[m")
            time.sleep(3)
            print("\033[0;34mRunning on screen...\033[m")
            time.sleep(3)
            print("\n")
            print("\033[0;34mo=============o IP Address o============o\033[m")
            time.sleep(0.5)
            print(ip_http)
            print("\n")
            print("\033[0;34mo================o HTML o===============o\033[m")
            time.sleep(0.5)
            print(text_http)
            print("\n")
            print("\033[0;34mo================o PORTS o==============o\033[m")
            time.sleep(0.5)
            print("\033[1;34mScanning ports in {}, please be patient...\033[m".format(var))
            time.sleep(3)
            for p0rt in ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(1)
                code = client.connect_ex((var, p0rt))
                if code == 0:
                    time.sleep(2)
                    print("Trying:", "Port", p0rt)
                    print("Situation: \033[1;32mOPEN\033[m \n")
                else:
                    pass
            print("\n")
            print("\033[0;34mo================o WOIS o===============o\033[m")
            time.sleep(0.5)
            print(consult_http.text)
            print("\n")
            print("\033[0;34mo================o MAILS o==============o\033[m")
            time.sleep(0.5)
            def GetEmailBySite(SiteList):
                for i in SiteList:
                    DataSite = requests.get(i)
                    ReturnRegex = re.findall(f'[\w\.-]+@[\w\\.-]+\.\w+',DataSite.text)
                    if ReturnRegex:
                        return(list(set(ReturnRegex)))
                    else:
                        return "\033[1;31mFailed to find emails!\033[m"

            sites = [web_source_http]
            cont_x=0
            try:
                for x in sites:
                    mails = (GetEmailBySite([x]))
                    if (mails != "None" or mails != None):
                        print("\033[1;34mScanning external mails, wait a second...\033[m")
                        time.sleep(0.1)
                        print("Mail:", mails)
                    cont_x = cont_x+1
            except:
                print(x)
                pass          
    elif var_start.lower() == simple_port_option:
        time.sleep(0.1)
        print("\033[0;36mLoading...\033[m \n")
        time.sleep(1.2)

        var_dec_port = int(input("\033[0;34m[*]\033[m Which port do you want?: "))
        print("Only type the domain of the website! ")
        print("Example: \033[0;33mwww.google.com, www.yahoo.com...\033[m")
        var = str(input("\033[0;34m[*]\033[m "))
        time.sleep(1)
        print("\033[1;34mScanning port {}, please be patient...\033[m".format(var_dec_port))
        time.sleep(1)
        print("Done! \n")
        
        varend = [var_dec_port]
        for p0rt in varend:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(5)
            code = client.connect_ex((var, p0rt))
            if code == 0:
                time.sleep(2)
                print("Port:", p0rt)
                print("Situation: \033[1;32mOPEN\033[m \n")
            else:
                print(f"Trying port: {p0rt}")
                print("Situation: \033[0;31mClosed\033[m")
    elif var_start.lower() == complete_port_option:
        time.sleep(0.1)
        print("\033[0;36mLoading...\033[m \n")
        time.sleep(1.2)

        print("Only type the domain of the website! ")
        print("Example: \033[0;33mwww.google.com, www.yahoo.com...\033[m")
        var = str(input("\033[0;34m[*]\033[m "))
        ports = [7,20,21,22,23,25,43,53,69,80,123,161,162,179,318,389,411,412,443,465,500,513,546,547,563,636,873,989,990,993,995,1194,1241,2049,3124,3128,4333,5004,5005,5500,5800,6665,6679,6697,8000,8080,33434]
        print("\033[1;34mScanning ports in {}, please be patient...\033[m".format(var))
        time.sleep(2)
        print("Done! \n")
        
        for po0rt in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1)
            code = client.connect_ex((var, po0rt))
            if code == 0:
                time.sleep(2)
                print("Trying:", "Port", po0rt)
                print("Situation: \033[1;32mOPEN\033[m \n")
    elif var_start.lower() == whois_option:
        time.sleep(0.1)
        print("\033[0;36mLoading...\033[m \n")
        time.sleep(1.2)

        print("Only type the domain of the website! ")
        print("Example: \033[0;33mwww.google.com, www.yahoo.com...\033[m")
        var = str(input("\033[0;34m[*]\033[m "))
        print("\033[1;34mScanning whois for {}, please be patient...\033[m".format(var))
        time.sleep(2)
        print("Done! \n")

        consult = whois.whois(var)
        print(consult.text)
    elif var_start.lower() == mail_option:
        time.sleep(0.1)
        print("\033[0;36mLoading...\033[m \n")
        time.sleep(1.2)

        #Domain definition (Definição do domínio)
        print("\033[0;36mType the domain's name:\033[m")
        print("Example: \033[0;33mwww.google.com, www.yahoo.com...\033[m")
        var_domain = input("\033[0;34m[*] \033[m")
        print("\n")
        time.sleep(1.5)

        #Domain http definition (Definição do http do domínio)
        print("\033[0;36mChoose the HTTP type...\033[m")
        print("  | Hyper Text Transfer Protocol Secure     \033[0;36mHTTPS\033[m - (1) |")
        print("  | Hyper Text Transfer Protocol            \033[0;36mHTTP\033[m  - (2) |")
        var_http_definition = int(input("\033[0;34m[*] \033[m"))
        print("\n")

        if var_http_definition == 1:
            time.sleep(0.1)
            print("\033[0;36mLoading...\033[m \n")
            time.sleep(1.2)
            web_source_https = "https://{}".format(var_domain)
            def GetEmailBySite(SiteList):
                for i in SiteList:
                    DataSite = requests.get(i)
                    ReturnRegex = re.findall(f'[\w\.-]+@[\w\\.-]+\.\w+',DataSite.text)
                    if ReturnRegex:
                        return(list(set(ReturnRegex)))
                    else:
                        return "\033[1;31mFailed to find emails!\033[m"

            sites = [web_source_https]
            cont_x=0
            try:
                for x in sites:
                    mails = (GetEmailBySite([x]))
                    if (mails != "None" or mails != None):
                        print("\033[1;34mScanning external mails, wait a second...\033[m")
                        time.sleep(0.1)
                        print("Mail:", mails)
                    cont_x = cont_x+1
            except:
                print(x)
                pass
        else:
            time.sleep(0.1)
            print("\033[0;36mLoading...\033[m \n")
            time.sleep(1.2)
            web_source_http = "http://{}".format(var_domain)
            def GetEmailBySite(SiteList):
                for i in SiteList:
                    DataSite = requests.get(i)
                    ReturnRegex = re.findall(f'[\w\.-]+@[\w\\.-]+\.\w+',DataSite.text)
                    if ReturnRegex:
                        return(list(set(ReturnRegex)))
                    else:
                        return "\033[1;31mFailed to find emails!\033[m"
                    
            sites = [web_source_http]
            cont_x=0
            try:
                for x in sites:
                    mails = (GetEmailBySite([x]))
                    if (mails != "None" or mails != None):
                        print("\033[1;34mScanning external mails, wait a second...\033[m")
                        time.sleep(0.1)
                        print("Mail:", mails)
                    cont_x = cont_x+1
            except:
                print(x)
                pass
    else:
        print("\033[0;31mError! Type 'runrabbit --run --help' to see the help menu...\033[m")

else:
    print("\033[0;31mCode error! Check the key in the main script to run it well!  \033[m")
    print("\033[0;31mThe key needs to be 'master-key-00100606'...  \033[m")
