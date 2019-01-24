from django.shortcuts import render
import random
import requests
import bs4

# Create your views here.
def index(request):
    return render(request,'index.html')

#Template Variables    
def dinner(request):
    menu = ["족발","햄버거","치킨","초밥"]
    pick = random.choice(menu)
    return render(request,'dinner.html',{'dinner': pick})
    
#Variable routing
def hello(request,name):
    name=name
    return render(request,'hello.html', {'name':name})
    
def food(request):
    response = requests.get('http://www.op.gg/summoner/userName=태전동하얀콩').text
    soup = bs4.BeautifulSoup(response, 'html.parser')
    # keyword= soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(1) > div > div.Content > div.KDA > div.KDARatio > span')
    kda= soup.select('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList > div:nth-child(9)')
    print(kda)
    return render(request,'food.html')
    
def throw(request):
    return render(request,'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request,'catch.html',{'message':message})

# Form 외부로 요청
def naver(request):
    return render(request,'naver.html')
    
def bootstrap(request):
    return render(request,'bootstrap.html')