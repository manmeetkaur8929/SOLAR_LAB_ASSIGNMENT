from django.http import HttpResponse, JsonResponse
import requests

def country_info(request, country):
    
    if country == None:
        return HttpResponse("No Country Found")

    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url).json()
    data = {}
    print(response)
    # return HttpResponse("Help")
    return JsonResponse(response,safe=False)

def home(request, country):
    html = "<html><body> Hi this is website by manmeet kaur </body></html>" 
    return HttpResponse(html)
