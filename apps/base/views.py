from django.shortcuts import render
from apps.base.models import Settings
from apps.secondary import models

def index(request):
    settings = Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    achievement = models.Achievement.objects.latest('id')
    bakery = models.Bakery.objects.all()
    menu = models.Menu.objects.all()
    categories = models.Category.objects.all()
    discount = models.Discount.objects.all()
    clients = models.Clients.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    return render(request, 'base/index.html', locals())


def contacts(request):
    settings = Settings.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    slideabout = models.SlideAbout.objects.latest('id')
    return render(request, 'contact.html', locals())

