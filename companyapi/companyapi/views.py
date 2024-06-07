

from django.http import HttpResponse, JsonResponse

def home_page(requests):
    print('home page requested')
    friends = ['Ankit', 'Sakshi', 'Gupta', 'Siri']
    # return HttpResponse("</h1>THIS  IS THE Home Page</h1>")
    return JsonResponse(friends, safe = False)



