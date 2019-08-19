# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:00:58 2019

@author: Xuan Yeh
"""
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import re
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *

f = open("rank2017.txt", 'w',encoding = 'utf8')
driver = webdriver.Chrome(r'C:\Users\samue\Anaconda3\Scripts\chromedriver.exe')
wait = WebDriverWait( driver, 10 )

subjects=['mathematics','physics','chemistry','earth-sciences','geography','ecology','oceanography',
'atmospheric-science','mechanical-engineering','electrical-electronic-engineering','automation-control',
'telecommunication-engineering','instruments-science-technology','biomedical-engineering','computer-science-engineering',
'civil-engineering','chemical-engineering','materials-science-engineering','nanoscience-nanotechnology',
'energy-science-engineering','environmental-science-engineering','water-resources','food-science-technology',
'biotechnology','aerospace-engineering','marine-ocean-engineering','transportation-science-technology',
'remote-sensing','mining-mineral-engineering','metallurgical-engineering','biological-sciences','human-biological-sciences',
'agricultural-sciences','veterinary-sciences','clinical-medicine','public-health','dentistry-oral-sciences',
'nursing','medical-technology','pharmacy-pharmaceutical-sciences','economics','statistics','law','political-sciences',
'sociology','education','communication','psychology','business-administration','finance','management',
'public-administration','hospitality-tourism-management','library-information-science']


for subject in subjects:
    url ='http://www.shanghairanking.com/Shanghairanking-Subject-Rankings-2017/%s.html'%(str(subject))
    #http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/mathematics.html
    #http://www.shanghairanking.com/Shanghairanking-Subject-Rankings-2018/mathematics.html
    #http://www.shanghairanking.com/Shanghairanking-Subject-Rankings-2017/mathematics.html
    driver.get(url)
    source = driver.page_source
    soup = bs(source, 'lxml')
    f.write('2017'+'$'+str(subject)+'$')
    f.write('\n') 
    odd= soup.find_all('tr',{"class":"bgfd"})
    even= soup.find_all('tr',{"class":"bgf5"})
    page_detail=[]
    lo=len(odd)
    le=len(even)
    l=min(lo,le)
    for x in range(l):
        page_detail.append(odd[x])
        page_detail.append(even[x])
    if(lo>l):
        tmp=lo-l
        page_detail.append(odd[-1])
    time.sleep(1)
    for pd in page_detail:
        detail= pd.find_all('td')
        nation= detail.pop(2)
        pic= nation.find('img')['src']
        f.write(pic+'$')
        for i in detail:
            f.write(i.text+'$')
        f.write('\n')    
    
    
driver.close()
f.close()