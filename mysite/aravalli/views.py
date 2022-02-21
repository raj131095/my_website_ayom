from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UploadImageForm
from .models import User,Create_Shop,UploadedImage,Watchlist,Comment
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from django.views.generic import TemplateView, ListView
from django.db.models import Q
# Create your views here.
def index(request):
    # Authenticated users view their inbox
    if request.user.is_authenticated:
        shop= Create_Shop.objects.all()
        users=request.user
        return render(request, "aravalli/index.html",{'constant':shop, 'users':users})

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))
def home_page(request):
    # Authenticated users view their inbox
    if request.user.is_authenticated:
        shop= Create_Shop.objects.all()
        users=request.user
        return render(request, "aravalli/index.html",{'constant':shop, 'users':users})

    # Everyone else is prompted to sign in
    else:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "aravalli/login.html", {
                "message": "Invalid email or password."

            })
    else:
        return render(request, "aravalli/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]
        first_name=request.POST.get('first_name')
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "aravalli/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, first_name, password)
            
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "aravalli/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "aravalli/register.html")

## shop 
@login_required
def create(request):
    if request.user.username:
        shop=Create_Shop.objects.all()
        users=request.user
    return render(request, "aravalli/createshop.html", {
         'constant':shop,
         'users':users
     }     )

@login_required
def submit(request):
    tasks=Create_Shop.objects.all()
    users=request.user
    if request.method=="POST":
        owner= request.POST['owner']
        shopname=request.POST['shopname']
        shopadd1=request.POST['shopadd1']
        shopadd2=request.POST["shopadd2"]
        latitude=request.POST["latitude"]
        longitude=request.POST["longitude"]
        contactno=request.POST["contactno"]
        altcontact=request.POST["altcontact"]
        opentime=request.POST["opentime"]
        website=request.POST['website']
        closetime=request.POST['closetime']
        describe=request.POST['describe']
        task=Create_Shop.objects.create(
            owner=owner,
            shopname=shopname,
            shopadd1=shopadd1,
            shopadd2=shopadd2,
            latitude=latitude,
            longitude=longitude,
            contactno=contactno,
            altcontact=altcontact,
            opentime=opentime,
            closetime=closetime,
            website=website,
            describe=describe,
            users=request.user,
        )
        return render(request, "aravalli/success.html", {
            'items':tasks,
            'users':request.user,
          })
    else:
          return redirect('index')

@login_required
def profilepage(request,pk):
    if request.user.username:
        data=Create_Shop.objects.get(pk=pk)
        shop= Create_Shop.objects.all()
        users=request.user
        form=UploadImageForm()
        img=UploadedImage.objects.filter(owner=data)

        queryset = img.order_by('-id').annotate(replies=Count('image') - 1)
        
    return render(request, "aravalli/profilepage.html",{
        'data': data,
        'users':users,
        'constant':shop,
        'form':form,
        'image':queryset,
    })

@login_required
def shopdata(request):
    if request.user.username:
        
        shop=Create_Shop.objects.all()
        users=request.user
    return render(request, 'aravalli/layout.html', {'constant': shop,
    'users':users,})

def Active_list(request):
     img=UploadedImage.objects.all()
     
     shop= Create_Shop.objects.all()
     users=request.user
     queryset = img.order_by('-id').annotate(replies=Count('image') - 1)
     page = request.GET.get('page', 1)

     paginator = Paginator(queryset, 20)

     
     try:
         image = paginator.page(page)
     except PageNotAnInteger:
         image = paginator.page(1) 
     except EmptyPage:
         image = paginator.page(paginator.num_pages)
     return render(request, "aravalli/activelist.html",{
        'users':users,
        'constant':shop,
        'image':image,
    })

@login_required
def upload_image(request,pk):
    board=Create_Shop.objects.get(pk=pk)
    img=UploadedImage.objects.filter(name=board)

    if request.method == 'POST':
        pieces= request.POST['pieces']
        offer=request.POST['offer']
        form = UploadImageForm(request.POST, request.FILES) 
        if form.is_valid(): 
                topic = form.save(commit=False)
                topic.pieces=pieces
                topic.offer=offer
                topic.owner = board
                topic.shopname= board.shopname
                topic.name= board.owner
                topic.shopadd1=board.shopadd1
                topic.shopadd2=board.shopadd2
                topic.latitude=board.latitude
                topic.longitude=board.longitude
                topic.contactno=board.contactno
                topic.altcontact=board.altcontact
                topic.website=board.website
                topic.opentime=board.opentime
                topic.closetime=board.closetime
                topic.describe=board.describe
                topic.save()
                return redirect('profilepage', pk=board.pk) 
    else: 
        form = HotelForm() 
    return render(request, 'aravalli/profilepage.html', {'form' : form})
    
def Details(request,pk):
    shop= Create_Shop.objects.all()
    users=request.user
    form=UploadImageForm()
    img=UploadedImage.objects.get(pk=pk)
    try:
        item = UploadedImage.objects.get(pk=pk)
    except:
        return redirect('index')
    try:
        comments = Comment.objects.filter(image=item)
    except:
        comments = None
    if request.user.username:
        try:
            if Watchlist.objects.get(user=request.user.username,pk=pk):
                added=True
        except:
            added = False
        try:
            l = UploadedImage.objects.get(pk=pk)
            if l.name == request.user.username :
                name=True
            else:
                name=False
        except:
            return redirect('activelist')
    else:
        added=False
        name=False
    try:
        w = Watchlist.objects.filter(user=request.user.username)
        wcount=len(w)
    except:
        wcount=None
    return render(request,"aravalli/detail.html",{
        "i":item,
        "error":request.COOKIES.get('error'),
        "errorgreen":request.COOKIES.get('errorgreen'),
        "comments":comments,
        "added":added,
        "wcount":wcount,
        'owner':name,
        'users':users,
        'constant':shop,
        'form':form,
        'images':img,
    })

@login_required
def Delete_profile(request,pk,):
    if request.user.username:
        imgss=UploadedImage.objects.get(pk=pk)
        imgss.delete()
        
        shop= Create_Shop.objects.all()
        users=request.user
        form=UploadImageForm()
        return redirect ('deletepage')

    return render(request, "aravalli/delete.html",{
        'users':users,
        'constant':shop,
        'form':form,
    })

@login_required
def Delete(request):
    shop=Create_Shop.objects.all()
    users=request.user
    return render(request, "aravalli/delete.html",
    {
    'constant':shop,
    'users':users,
    })
    

## this is for the watch list from now
@login_required
def addwatchlist(request,pk):
    if request.user.username:
        img=UploadedImage.objects.get(pk=pk)
        w = Watchlist()
        w.user = request.user.username
        w.image = img
        w.save()
        return redirect('details',pk=pk)
    else:
        return redirect('activelist')

@login_required
def removewatchlist(request,pk):
    if request.user.username:
        img=UploadedImage.objects.get(pk=pk)
        w =Watchlist.objects.filter(user=request.user.username,image=img)
        w.delete()
        return redirect('details',pk=pk)
    else:
        return redirect('activelist')

@login_required
def watchlistpage(request,username):
    if request.user.username:
        shop= Create_Shop.objects.all()
        users=request.user
        try:
            w = Watchlist.objects.filter(user=username)
            items = []
            for i in w:
                items.append(UploadedImage.objects.get(title=i.image))
                
            try:
                w = Watchlist.objects.filter(user=request.user.username)
                wcount=len(w)
            except:
                wcount=None
            return render(request,"aravalli/watchlistpage.html",{
                "watch":w,
                "items":items,
                'constant':shop,
                "wcount":wcount,
                'users':users,
                
            })
        except:
            try:
                w = Watchlist.objects.filter(user=request.user.username)
                wcount=len(w)
            except:
                wcount=None
            return render(request,"aravalli/watchlistpage.html",{
                "items":None,
                'constant':shop,
                "wcount":wcount,
                'users':users,
            })
    else:
        return redirect('activelist')


def cmntsubmit(request,pk):
    if request.method == "POST":
        now = datetime.now()
        dt = now.strftime(" %d %B %Y %X ")
        c = Comment()
        c.comment = request.POST.get('comment')
        c.user = request.user.username
        c.time = dt
        c.image= UploadedImage.objects.get(pk=pk)
        c.save()
        return redirect('details',pk=pk)
    else :
        return redirect('activelist')


class SearchResultsView(ListView):
    model = UploadedImage
    template_name = 'aravalli/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        image= UploadedImage.objects.filter(Q(image__icontains=query)|Q(title__icontains=query)|Q(shopname__icontains=query)|Q(name__icontains=query)|Q(shopadd1__icontains=query))
        object_list=image.order_by('-id').annotate(replies=Count('image') - 1)
        return object_list

def UserName(request,pk):
    img=UploadedImage.objects.get(pk=pk)
    comments=Comment.objects.filter(image=img)
    user=User.objects.filter(username=comments)
    return render(request, "aravalli/detail.html", {
        'userss':user
    })

def AboutUs(request):
    # Authenticated users view their inbox
        shop= Create_Shop.objects.all()
        users=request.user
        return render(request, "aravalli/aboutus.html", {'constant':shop, 'users':users})
