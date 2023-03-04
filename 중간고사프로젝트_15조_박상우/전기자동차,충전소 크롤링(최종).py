import urllib.request
import os
import matplotlib as mpl
import sys
import datetime, time
import pandas as pd
import matplotlib.pyplot as plt
import requests
import xmltodict, json
import numpy as np
import matplotlib
from numpy.random import randn
from matplotlib import font_manager, rc


ServiceKey="vnqz8NaLxQYvByG6QFkCQO2OEx5FpEMPHFntNI8E3k0ouqtT7ukRZJ9gLA49H9Suu403UaesyhoN3VDr0rzZ0w%3D%3D"


def getRequestUrl(url):
    req=urllib.request.Request(url)
    try:
        response=urllib.request.urlopen(req)
        if response.getcode()==200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')

    except Exception as e:
        print(e)
        print("[%s] Error URL : %s" %(datetime.datetime.now(),url))
        return None
    

def getElectronicStatsItem(pageNo,numOfRows,addr):
    service_url="http://openapi.kepco.co.kr/service/EvInfoServiceV2/getEvSearchList"

    parameters = "?_type=json&serviceKey=" + ServiceKey
    parameters += "&pageNo=" + pageNo
    parameters += "&numOfRows=" + numOfRows
    parameters += "&addr=" + urllib.parse.quote(addr)

    url = service_url + parameters
    retData=getRequestUrl(url)
    
    
    if(retData==None):
        return None

    else:
        print("수집이 완료되었습니다.")
        return json.loads(retData)
     


def main():
    print(" << 전기차 충전소를 조회합니다.>> ")
    addr=input("시/도를 입력하세요 ( ex)서울특별시 / 경기도 / 전라남도...) : ")
    numOfRows=input("데이터를 몇 개 수집할까요? ( MAX를 수집 = 1000 ) : ")
    pageNo= "1"
    
    result=getElectronicStatsItem(pageNo,numOfRows,addr)
    data=pd.DataFrame(result['response']['body']['items']['item'])

    li=['addr','chargeTp','cpNm','csId','csNm']
    data.loc[:,li]

    data[li].to_csv('./%s_전기차충전소.csv' % (addr) ,index=False, encoding='cp949')
    

    df = pd.DataFrame()
    import platform
    print(platform.system()) # 플랫폼 확인
    # Window
    if platform.system() == 'Windows':
        matplotlib.rc('font', family='Malgun Gothic')

    elif platform.system() == 'Darwin': # Mac
        matplotlib.rc('font', family='AppleGothic')

    else: #linux
        matplotlib.rc('font', family='NanumGothic')

    # 그래프에 마이너스 표시가 되도록 변경
    matplotlib.rcParams['axes.unicode_minus'] = False

    #지역
    df['area'] = ['부산','대구','대전','광주','경기','강원','경북','경남','충북','충남','전북','전남','세종','서울','인천','울산','제주']*3

    df['count'] =[1567,6605,1334,1447,6383,1377,2001,2107,1199,1127,997,1974,394,9564,1284,847,15549,3216,11313,2555,2464,11750,2445,4051,3626,2412,2841,1841,3326,903,14952,2598,1447,18178,4320,12468,3338,3046,17197,3091,5400,5003,3319,4252,2906,4576,1076,20997,4204,2142,20699,]

    df['date'] = ['2018-12-31']*17 + ['2019-12-31']*17 + ['2020-08-31']*17 ## 날짜

    ## 3개 데이터 분리
    a_df = df.query('date =="2018-12-31"') 
    a_count = a_df['count']
    area = a_df['area']
     
    b_df = df.query('date =="2019-12-31"')
    b_count = b_df['count']
     
    c_df = df.query('date =="2020-08-31"')
    c_count = c_df['count']
     
    fig = plt.figure(figsize=(8,8)) ## 캔버스 생성
    fig.set_facecolor('white') ## 캔버스 색상 설정
    ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성
     
    ax.plot(area,a_count,marker='o',label='2018-12-31') ## 선그래프 생성
    ax.plot(area,b_count,marker='o',label='2019-12-31') 
    ax.plot(area,c_count,marker='o',label='2020-08-31')

    font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
    mpl.rc('font', family=font_name)

    ax.legend() ## 범례

    plt.title('지역별 전기차 수',fontsize=20) ## 타이틀 설정

    #plt.show()

    url2="https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002313189&fileDetailSn=1&dataNm=%ED%95%9C%EA%B5%AD%EC%A0%84%EB%A0%A5%EA%B3%B5%EC%82%AC_%EC%A7%80%EC%97%AD%EB%B3%84%20%EC%A0%84%EA%B8%B0%EC%B0%A8%20%EC%B6%A9%EC%A0%84%EC%86%8C%20%ED%98%84%ED%99%A9%EC%A0%95%EB%B3%B4_20201008"
    
    #df=open('충전소.csv')
    df=pd.read_csv(url2, index_col='지역', encoding='euc-kr')

    city_df=df.loc[['강원도','경기도','경상남도','경상북도','광주광역시','대구광역시','대전광역시','부산광역시','서울특별시','세종특별자치시','울산광역시','인천광역시','전라남도','전라북도','제주특별자치도','충청남도','충청북도']]


    font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
    mpl.rc('font', family=font_name)

    ax = city_df.plot(kind='bar', title='충전소', figsize=(8, 4), legend=True, fontsize=7)
    ax.set_xlabel('지역별', fontsize=12)          # x축 정보 표시
    ax.set_ylabel('충전소 수', fontsize=12)     # y축 정보 표시
    ax.legend(['2016','2017','2018','2019','2020'], fontsize=12)    # 범례 지정

    plt.show()
    
if __name__=='__main__':
    main()
