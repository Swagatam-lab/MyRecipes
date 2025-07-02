from django.shortcuts import render
from django.http import  HttpResponse



def home(request):


    peoples = [
        {'name':'Rohan Gupta','age':22},
        {'name':'Divya Sharma','age':24},
        {'name':'Anil Agrahari','age':53},
        {'name':'Rajesh Mishra','age':15}
    ]


    return render (request ,"home/index.html" , context={'peoples':peoples})


def success_page(request):
    return HttpResponse("<h1>Hey this is a success page.</h1>")