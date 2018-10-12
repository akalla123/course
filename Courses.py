
# coding: utf-8

# In[9]:


import requests
import webbrowser
import bs4
import re
from bs4 import BeautifulSoup, SoupStrainer
string = "files"
soups = []
p1 = requests.get('https://www.stevens.edu/school-business/masters-programs/mba/stevens-mba/curriculum-and-concentrations')
soup = bs4.BeautifulSoup(p1.text, 'lxml')
soups.append(soup)

p2 = requests.get('https://www.stevens.edu/school-business/masters-programs/business-intelligence-analytics/curriculum-overview')
soup = bs4.BeautifulSoup(p2.text, 'lxml')
soups.append(soup)

p3 = requests.get('https://www.stevens.edu/school-business/masters-programs/management/curriculum-overview')
soup = bs4.BeautifulSoup(p3.text, 'lxml')
soups.append(soup)

p4 = requests.get('https://www.stevens.edu/school-business/masters-programs/mba/analytics-mba/curriculum')
soup = bs4.BeautifulSoup(p4.text, 'lxml')
soups.append(soup)

p5 = requests.get('https://www.stevens.edu/school-business/masters-programs/enterprise-project-management/curriculum-overview')
soup = bs4.BeautifulSoup(p5.text, 'lxml')
soups.append(soup)

p6 = requests.get('https://www.stevens.edu/school-business/masters-programs/network-communication-management-services/curriculum-overview')
soup = bs4.BeautifulSoup(p6.text, 'lxml')
soups.append(soup)

p7 = requests.get('https://www.stevens.edu/school-business/masters-programs/mba/executive-mba-emba/curriculum-overview')
soup = bs4.BeautifulSoup(p7.text, 'lxml')
soups.append(soup)

p8 = requests.get('https://www.stevens.edu/school-business/masters-programs/finance/curriculum-overview')
soup = bs4.BeautifulSoup(p8.text, 'lxml')
soups.append(soup)

p9 = requests.get('https://www.stevens.edu/school-business/masters-programs/information-systems/curriculum-overview')
soup = bs4.BeautifulSoup(p9.text, 'lxml')
soups.append(soup)

p10 = requests.get('https://www.stevens.edu/school-business/masters-programs/technology-management/curriculum-overview')
soup = bs4.BeautifulSoup(p10.text, 'lxml')
soups.append(soup)



b = input("Select your course: ")



tm_all_courses = []
li = []
bia_li = []
mis_li = []
b = b.split()
if b[0] == "EMT" and b[1] == "677":
    print("No Course description available ")
    
elif b[0] == "EMT" or b[0] == "BIA" or b[0] =="TM":
    b = '%20'.join(b)
elif b[0] == "MGT" and b[1] == "609":
    b = "Mgt609"
elif b[0] == "FIN" and b[1] ==  "615":
    b = "MGT615"
elif b[0] == "FIN" and b[1] == "510":
    b = "".join(b)
elif b[0] == "FE":
    b = "".join(b)
elif b[0] == "FIN" and b[1] == "629":
    b = "".join(b)
elif b[0] == "FIN":
    b = "MGT" + b[1]
else:
    b = ''.join(b)
#print(b)
for i in range(len(soups)):
    for link in soups[i].find_all("a", href=True):
        li.append(link['href'])
for i in range(len(li)):
    if string in li[i]:
        mis_li.append(li[i])
#print(mis_li)
for i in range(len(mis_li)):
    if b in mis_li[i]:
        webbrowser.open(mis_li[i])
        
        
# Check for exceptions and change the link

