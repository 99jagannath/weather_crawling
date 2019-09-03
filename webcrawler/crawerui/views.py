from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import time
import urllib,csv,os,datetime,urllib.request,re,sys,requests
# Create your views here.
def index(request):
    return render(request,'index.html')
def result(request):
    place = request.POST['place']
    date = request.POST['date']
    type = request.POST['type']
    
    
    
    url = 'https://weather.com/en-IN/search/enhancedlocalsearch?where='+place+'&loctypes=1/4/5/9/11/13/19/21/1000/1001/1003/&from=hdr'
    #print(urlobj)
    thispage = requests.get(url)
    
    prevsoup = BeautifulSoup(thispage.content,'html.parser')
    q=[]
    for a in prevsoup.select('.styles__itemLink__23h5a'):
        q.append(a['href'])
    if len(q)==0:
        urlobj='https://weather.com/en-IN/weather/today/l/INXX0024:1:IN'
    else:
        urlobj=q[0]    
    
       
    # urlobj='https://weather.com/en-IN/weather/today/l/INXX0024:1:IN'
    thepage = requests.get(urlobj)
    
    soup = BeautifulSoup(thepage.content, 'html.parser')
    #print(thepage.text)
    #print(soup)
    
    for i in soup.select('.styles__navigationItem__2faNj'):
        #print(i['href'][])
        j=i['href']
        i=i['href'].split('/')
        if i[3]==type and type=='today':
            newurl='https://weather.com'+j
            newpage = requests.get(newurl)
            newsoup=BeautifulSoup(newpage.content,'html.parser')
            #print(newsoup.select('tr'))
            heading_list=[]
            content_list=[]
            contentss=[]
            for data in newsoup.select('tr'):
                heading_list.append( data.find_all('th'))
                content_list.append(data.find_all('td'))
            contentss.append(heading_list)
            contentss.append(content_list)
            contents=[]
            
            for i in contentss:
                for j in i:
                    
                    
                    contents.append(j)

                

            
            
        if i[3]==type and type=='hourbyhour':
            newurl='https://weather.com'+j
            newpage = requests.get(newurl)
            newsoup=BeautifulSoup(newpage.content,'html.parser')
            #print(newsoup.select('tr'))
           
            list=[]
            for data in newsoup.select('tr'):
                list.append(data)
            contents=[]  
            c=1
            for cols in list:
                contents.append(list[c].find_all('span')) 
                c=c+1 
                if c==8:
                    break
            #print(contents)
        if i[3]==type and type=='5day':
            newurl='https://weather.com'+j
            newpage = requests.get(newurl)
            newsoup=BeautifulSoup(newpage.content,'html.parser')
            #print(newsoup.select('tr'))
            
            list=[]
            for data in newsoup.select('tr'):
                list.append(data)
            contents=[]  
            c=1
            
            for cols in list:
                contents.append(list[c].find_all('span')) 
                c=c+1 
                if(c==6):
                    break
                
            #print(contents)
        if i[3]==type and type=='10day':
            newurl='https://weather.com'+j
            newpage = requests.get(newurl)
            newsoup=BeautifulSoup(newpage.content,'html.parser')
            #print(newsoup.select('tr'))
            
            list=[]
            for data in newsoup.select('tr'):
                list.append(data)
               
            contents=[]  
            c=1
            
            for cols in list:
                contents.append(list[c].find_all('span')) 
                c=c+1 
                if(c==11):
                    break
                
            #print(contents)
        if i[3]==type and type=='weekend':
            newurl='https://weather.com'+j
            newpage = requests.get(newurl)
            newsoup=BeautifulSoup(newpage.content,'html.parser')
            #print(newsoup.select('tr'))
            
            list=[]
            for data in newsoup.select('.wx-weather__day'):
                list.append(data)
            contents=[]  
            c=1
            
            for cols in list:
                contents.append(list[c].find_all('span')) 
                c=c+1 
                if(c==6):
                    break
                
            #print(contents)
    
        if i[3]==type and type=='monthly':
            newurl='https://weather.com'+j 
            newpage = requests.get(newurl)
            newsoup=BeautifulSoup(newpage.content,'html.parser')
            #print(newsoup.select('tr'))
            
            list=[]
            for data in newsoup.select('.forecast-monthly__day-info__content'):
                list.append(data)   
            contents=[]  
            c=0
            
            for cols in list:
                contents.append(list[c].find_all('span')) 
                c=c+1
                
            #print(contents)                  
    
    
    return render(request,'result.html',{'place':place,'date':date,'type':type,'contents':contents})    
