from django.http import HttpResponse

def setcookie(request):
    response = HttpResponse("Cookie has been set")
    response.set_cookie('user', 'Krish', max_age=3600)  
    return response

def getcookie(request):
    user = request.COOKIES.get('user')
    return HttpResponse(f"User is {user}")

def deletecookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('user')
    return response

def ses(request):
    request.session['fav_color'] = 'blue'
    return HttpResponse("Session data set")

def getses(request):
    fav_color = request.session.get('fav_color', 'No favorite color set')
    return HttpResponse(f"Favorite color is {fav_color}")
