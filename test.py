import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service#셀레니움 4부터 사용하기위한 클래스
# from webdriver_manager.chrome import ChromeDriverManager #셀레니움 4부터 사용하기위한 클래스
import time 
import datetime
import re
import random

def find_info():
    global Id
    Start_Ymd=datetime.datetime.now()
    year=Start_Ymd.year
    month=Start_Ymd.month-2
    day="01"
    Start_Ymd=str(year)+str(month)+day

    End_Ymd=datetime.datetime.now()
    year=End_Ymd.year
    month=End_Ymd.month
    day=End_Ymd.day

    if day<10:
        day="0"+str(day)
    else:
        day=str(day)

    End_Ymd=str(year)+str(month)+day


    url="https://www.lost112.go.kr/find/findDetail.do?"
    info=f"pageIndex=1&PRDT_CL_NM=&PRDT_CL_CD01=&PRDT_CL_CD02=&START_YMD={Start_Ymd}&END_YMD={End_Ymd}&PRDT_NM=&DEP_PLACE=&SITE=&PLACE_SE_CD=&FD_LCT_CD=&IN_NM=&MDCD=&SRNO=&IMEI_NO=&F_ATC_ID=&ATC_ID={Id}&FD_SN=1&MENU_NO="
    info=url+info
    
    return info



url='https://www.lost112.go.kr/find/findList.do'

option=webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging'])
# browser = webdriver.Chrome(options=option,service=Service(ChromeDriverManager().install()))
browser=webdriver.Chrome(options=option)
browser.maximize_window()# 전체화면



while(1):
    time.sleep(random.randint(1,3))# 트래픽 방지


    #같은 경로가 아닐경우 안에 파일경로를 입력해주어야한다.

    for temp in range(5):
        browser.get(url)# 주소안으로 접속
        Id=browser.find_elements(By.TAG_NAME,"tr")[temp+1]
        Id=Id.find_element(By.TAG_NAME,'a').text
        print(Id)
        browser.get(find_info())#새로운 유실물창 접속

        elem=browser.find_element(By.CLASS_NAME,"find_info").text

        arr=elem.split("\n")

        target1=re.compile("x")# 물품이름 타겟
        target2=re.compile("y")# 물품 분류 타겟

        if target2.search(arr[5])!='':# 물품분류가 맞는지 확인
            if target1.search(arr[0])!='': # 습득물 명이 맞는지 확인
                pass # 메일 함수 실행 및 전송
        time.sleep(random.randint(1,3))# 트래픽 방지









