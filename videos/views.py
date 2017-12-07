from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
import random


def home(request):
    return HttpResponse('<h1>Welcome Home</h1>')

class HomeView(View):
    def get(self,request, *args, **kwargs):
        number = str(random.randint(100,1000))
        #text = "<h1>Welcome</h1>"
        #text += '<h3>랜덤숫자</h3>['+number+']
        #return HttpResponse('<h1>Welcome Class Home ['+number+']!!!</h1>')
        context = {
               "name" : "John"
        }

        context = {
                "name" : "John",
                "number" : number,
                "present" : "<ul><li>내용1</li><li>내용2</li><li>내용3</li></ul>"
        }


        return render(request, "home.html", context)