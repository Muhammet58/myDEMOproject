from django.urls import path
from . import views

#http://127.0.0.1:8000/    ==> views içindeki index fonksiyonu çalışır
#http://127.0.0.1:8000/blog  ==> views içindeki blog fonksiyonu çalışır
#http://127.0.0.1:8000/blog/3  ==> views içindeki blog_details fonksiyonu çalışır


urlpatterns = [
    path("",views.index),                           #http://127.0.0.1:8000/
    path("blog",views.blog),                        #http://127.0.0.1:8000/blog
    path("blog/<int:id>",views.blog_details),       #http://127.0.0.1:8000/blog/3

]