from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return render(request,"blogapp/index.html")

def blog(request):
    return render(request,"blogapp/blogs.html")

def blog_details(request,id):
    return render(request,"blogapp/blog-details.html",{'id':id})






#def url1(request):
#    return HttpResponse("Ana sayfa")
#
#def url2(request):
#    return HttpResponse("Blog sayfası")
#
#def url3(request,id):
#    return HttpResponse(f"Blog detayı : {id}")
