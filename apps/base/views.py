from django.shortcuts import render
from apps.base.models import Settings
from apps.secondary import models
from apps.contacts.models import Contacts,Bron
from apps.telegram_bot.views import get_text

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


    if request.method=="POST":
        if 'contact_form' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            page_contact = Contacts.objects.create(name=name, email=email, subject=subject, message=message)
            if page_contact:
                get_text(f"""
                Оставлена заявка на обратный звонок 📞
                         
Имя пользователя:  {name}
Почта: {email}
Тема: {subject}
Сообщение: {message}

""")
                
    return render(request, 'contact.html', locals())


