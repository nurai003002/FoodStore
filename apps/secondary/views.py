from django.shortcuts import render
from apps.base.models import Settings
from apps.secondary import models
from apps.telegram_bot.views import get_text
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.contacts.models import Bron
# Create your views here.
def about(request):
    settings = Settings.objects.latest('id')
    slide = models.Slide.objects.latest('id')
    achievement = models.Achievement.objects.latest('id')
    bakery = models.Bakery.objects.all()
    discount = models.Discount.objects.all()
    clients = models.Clients.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    slideabout = models.SlideAbout.objects.latest('id')
    menu = models.Menu.objects.all()
    categories = models.Category.objects.all()
    big_category = models.BigCategory.objects.all()
    news = models.News.objects.all()
    
    return render(request, 'about.html', locals())

def menu(request):
    settings = Settings.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    slideabout = models.SlideAbout.objects.latest('id')
    big_categories = models.BigCategory.objects.all()
    categories = models.Category.objects.all()
    menu = models.Menu.objects.all()
    news = models.News.objects.all()
    return render(request, 'menu.html', locals())


def shop(request):
    settings = Settings.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    slideabout = models.SlideAbout.objects.latest('id')
    news = models.News.objects.all()

    food = models.ShopFood.objects.all()

    paginator = Paginator(food, 8)
    page = request.GET.get('page')

    try:
        food = paginator.page(page)
    except PageNotAnInteger:
        food = paginator.page(1)
    except EmptyPage:
        food = paginator.page(paginator.num_pages)
    return render(request, 'shop.html', locals())


def reservation(request):
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
    slideabout = models.SlideAbout.objects.latest('id') 
    news = models.News.objects.all()

    if request.method=="POST":
        if 'bron_form' in request.POST:
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            date = request.POST.get('date')
            page_contact = Bron.objects.create(fullname=fullname, email=email, phone=phone,message=message,date=date)
            if page_contact:
                get_text(f"""
                Оставлена заявка на Брон 🔐 
                         
Имя пользователя:  {fullname}
Почта: {email}
Номер телефона: {phone}
Дата: {date}
Сообщение: {message}

""")


    return render(request, 'reservation.html', locals())

def cart(request):
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
    slideabout = models.SlideAbout.objects.latest('id') 
    news = models.News.objects.all()
    

    return render(request, 'cart.html', locals())


def details(request, id):   
    settings = Settings.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    slideabout = models.SlideAbout.objects.latest('id')
    
    news = models.News.objects.all()
    food_detail = models.ShopFood.objects.get(id=id)

    return render(request, 'shop-details.html', locals())


def blog_details(request, id):   
    menu = models.Menu.objects.all()
    settings = Settings.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    slideabout = models.SlideAbout.objects.latest('id')
    food = models.ShopFood.objects.all()
    news_blog = models.News.objects.get(id=id)
    news = models.News.objects.all()
    # comment = models.Review.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_comment = request.POST.get('comment')

        new_comment = models.Review(name=name, email=email, comment=user_comment)
        new_comment.save()

        news_blog.comments.add(new_comment)

    return render(request, 'blog-details.html', locals())


def wishlist(request):
    settings = Settings.objects.latest('id')
    post = models.Post.objects.all()
    allfood = models.AllFood.objects.all()
    lastpost = models.LastPost.objects.latest('id')
    slideabout = models.SlideAbout.objects.latest('id')
    food = models.ShopFood.objects.all()

    news = models.News.objects.all()

    return render(request, 'wishlist.html', locals())