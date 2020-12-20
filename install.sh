#!/bin/bash
sleep 1s
clear
echo -e "\e[1;32m -+-+-+-+-+-+-+-+-+ Subscribe to my channel -+-+-+-+-+-+-+-+"
echo -e "-+-+-+-+-+ https://youtube.com/c/TechwithDharanish -+-+-+-+-+-+\e[0m"
echo -e "\e[1;32m Installing requirements\e[0m"
sleep 1s
pkg install python
pip install requests && pip install mechanize && pip install json && pip install bs4
pip install beautifulsoup4 && pip install pytube && pip install phonenumbers
sleep 1s
echo -e "\e[1;32m <<━ ━ ━ ━  run ' python tracksploit.py ' ━ ━ ━ ━>>\e[0m"
