#!/bin/bash

echo -e "\n___________________________________________________________\n"
echo  " Extra Tools For RunRabbit!         BY: black-hot-pepper"
echo -e "___________________________________________________________\n"

echo -e "\e[1;34mType the URL of the website below:\e[0m"
read -p "> " url
echo -e "\n\e[1;34mOnly type the website name domain below:\e[0m"
read -p "> " domain

echo -e "\n\e[1;34mDoing for\e[0m" $domain
#curl
echo -e "\n\e[1;34m__________HTML Insider Information:\e[0m"
curl -V -H $url


#nikto_scanning
echo -e "\n\e[1;34m__________Nikto Scanning:\e[0m"
echo "PORT 20"
nikto -h $domain -port 20
echo "PORT 21"
nikto -h $domain -port 21
echo "PORT 43"
nikto -h $domain -port 43
echo "PORT 53"
nikto -h $domain -port 53
echo "PORT 80"
nikto -h $domain -port 80
echo "PORT 3124"
nikto -h $domain -port 3124
echo "PORT 8080"
nikto -h $domain -port 8080

#dirb
echo -e "\n\e[1;34m__________Extra Informations:\e[0m"
dnsenum $domain


#sub_domains
echo -e "\n\e[1;34m__________Sub Domains:\e[0m"
dnsenum --enum $url
