import requests
from django.shortcuts import redirect, render
from datetime import datetime
import calendar
from .models import todo



# Create your views here.



# Create date, month, year var => pass into 'context'
def get_datetime():
    current_dateTime = datetime.now()
    date = current_dateTime.date().day
    month = calendar.month_name[current_dateTime.date().month]
    year = current_dateTime.date().year
    date_time = {
        "date": date,
        "month": month,
        "year": year,
    }   
    return date_time

def index(request): 
    # declaring constant
    API_KEY = '547f59cb0b0f0159fa10a20b4e68c8a5'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    # Initialize 'context' dict
    date_time = get_datetime()
    context = {
        'date_time': date_time,
    }
    try:
        task_final = retrieve_todo()
        context['todos'] = task_final
    except UnboundLocalError:
        pass

    # logic for handling request
    if request.method == 'POST':
        if request.POST.get('city1'):
            city1 = request.POST['city1']
            city1 = city1.title()
            # try and except to handle KeyError Exception
            try: 
                weather_data1 = fetch_weather(city1, API_KEY, current_weather_url)
                context = {
                    'date_time': date_time, 
                    'weather_data1': weather_data1
                }
                # return render(request, 'personal_page_app/index.html', context)
            except KeyError:
                context = {
                'date_time': date_time,
                'error_bool': True
                }
                # return render(request, 'personal_page_app/index.html', context)
            
        # to do list - add new todo
        if request.POST.get('todo'):
            task = todo.objects.create()
            content1 = request.POST['todo']
            task.content = content1
            task.save()
        try:
            task_final = retrieve_todo()
            context['todos'] = task_final
        except UnboundLocalError:
            pass

        # render page
        return render(request, 'personal_page_app/index.html', context)
    else:
        return render(request, 'personal_page_app/index.html', context)
        
def retrieve_todo():
    task_content = list(todo.objects.values_list('content', flat=True))
    task_status = list(todo.objects.values_list('status', flat=True))
    task_final = []
    for content, status in zip(task_content, task_status):
        temp = [content, status]
        task_final.append(temp)
    return task_final

def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    weather_data = {
        'city': city,
        'temp': int(round(response['main']['temp'] - 273.15, 0)), # temp is in Kelvin "-273.15" to switch to Celsius
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon']
    }
    return weather_data

def social_login_spotify(request):
    """Redirects the user to the Spotify login page."""
    return redirect('social:begin', 'spotify')
