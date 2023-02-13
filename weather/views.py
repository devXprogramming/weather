from django.shortcuts import render, redirect
import json
import urllib

# Create your views here.



def home(request):
    if request.method=="POST":

        try:
            userInput = request.POST.get('userInput')

            apiKey = "593114135eaf0b3ba55ed528bdda7e46"

            url = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={userInput}&appid={apiKey}')
            
            res = json.load(url)
            print(res)


            data = {
                'city': userInput,
                'temperature': res['main']['temp'],
                'pressure': res['main']['pressure'],
                'humidity': res['main']['humidity'],
                'sealevel': res['main']['sea_level'],
                'timezone': res['timezone'],
                'country': res['sys']['country'],
                'description': res['weather'][0]['description'],
                'mode': res['weather'][0]['main'],
                'icon': res['weather'][0]['icon'],
            }
        except:
            show = {
                'city': userInput,
            }
            return redirect( '/invalid/', {'show':show})
    else:
        data = {
            'city':None,
            'weather': None,
        }

    return render(request,'index.html', {'data':data})

def invalid(request):
    return render(request,'error.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == 'admin@gmail.com' and password == 'admin':
            return redirect('home/')

    return render(request, 'login.html')