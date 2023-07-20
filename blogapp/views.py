from django.shortcuts import render
from .models import Blogs, Category

"""data = {
    'blogs': [
        {
            'id': 1,
            'title': 'web programlama kursu',
            'image': '1.png',
            'is_active': True,
            'is_blog': False,
            'is_home': True,
            'description': "Bu kurs ile çok kısa sürede web programlamayı öğreneceksiniz. bu kurs web programlamanın temellerini size kısa sürede öğretir",
        },
        {
            'id': 2,
            'title': 'pyhon-django kursu ?',
            'image': '2.png',
            'is_active': True,
            'is_blog': False,
            'is_home': True,
            'description': 'Bu kurs ile python programlama dilinin bir kütüphanesi olan django ile web programlamayı öğreniceksiniz.'
        },
        {
            'id': 3,
            'title': 'bootstrap nedir ?',
            'image': '3.png',
            'is_active': True,
            'is_blog': False,
            'is_home': True,
            'description': 'Bootstrap açık kaynak kodlu, web sayfaları veya uygulamaları geliştirmek için kullanılabilecek araçlar bütünü ve önyüz çatısıdır. '
        }, 
        {
            'id': 4,
            'title': 'Java programlama kursu',
            'image': '4.png',
            'is_active': True,
            'is_blog': True,
            'is_home': False,
            'description': 'Bu kurs ile java programlama dilinin temellerini kısa sürede öğreniceksiniz. '
        },
        {
            'id': 5,
            'title': 'Flutter ile mobil uygulama yapma',
            'image': '5.png',
            'is_active': True,
            'is_blog': True,
            'is_home': False,
            'description': 'Bu kurs size flutter ile mobil uygulama yapmayı öğretir'
        }
    ]
}"""

def index(request):
    context = {
        "blogs": Blogs.objects.all(),
        "category": Category.objects.all()
    }
    return render(request, "blogapp/index.html", context)

def blog(request):
    context = {
        "blogs": Blogs.objects.filter(is_blog=True),
        "category":Category.objects.all()
    }
    return render(request, "blogapp/blogs.html", context)

def blog_details(request, slug):
    #blogs = data['blogs']
    #selectedBlog = None

    #for blog in blogs:
    #    if blog['id'] == id:
    #        selectedBlog = blog

    #blogs = data['blogs']
    #selectedBlog = [blog for blog in blogs if blog['id'] == id][0]

    data = {
        "blog": Blogs.objects.get(slug=slug),
    }
    return render(request, "blogapp/blog-details.html", data)


def blogs_by_category(request, slug):
    data = {
        "blogs": Category.objects.get(slug=slug).blogs_set.all(),
        #"blogs": Blogs.objects.filter(categories__slug=slug),
        "category": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blogapp/blogs.html", data)



#def url1(request):
#    return HttpResponse("Ana sayfa")
#
#def url2(request):
#    return HttpResponse("Blog sayfası")
#
#def url3(request,id):
#    return HttpResponse(f"Blog detayı : {id}")
