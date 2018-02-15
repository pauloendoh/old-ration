from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone

from users.forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import ItemForm, UserItemForm
from .models import Item, User_Item


def index(request):
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        if request.GET.get('order') == 'rating':
            user_items = User_Item.objects.filter(user=user).order_by('-rating')
        else:
            user_items = User_Item.objects.filter(user=user).order_by('-interest')
        return render(request, 'index.html', {'user_items': user_items})
    else:
        return redirect('login')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'login,html', )


def users_data(request):
    users = User.objects.all()
    return render(request, 'users_data.html', {'users': users})


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.created_on = timezone.now()
            post.type = form.cleaned_data['type'].upper()
            post.save()
            return redirect('items')
    return render(request, 'create_item.html', {'form': ItemForm})


def items(request):
    items = Item.objects.all()
    if request.GET.get('order') == 'rating':
        items = items.order_by('-avg_rating')
    else:
        items = items.order_by('-avg_interest')
    return render(request, 'items.html', {'items': items})


def show_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user.is_authenticated:
        if User.objects.filter(id=request.user.id)>0 :
            user = User.objects.filter(id=request.user.id)
            if User_Item.objects.filter(item=item, user=user).count() > 0:
                user_item = User_Item.objects.filter(item=item, user=request.user).first()
                return render(request, 'item.html', {'item': item, 'user_item': user_item})

    return render(request, 'item.html', {'item': item})


def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES, instance=item )
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.created_on = timezone.now()
            item.type = form.cleaned_data['type'].upper()
            item.save()
            return redirect('items')
    return render(request, 'edit_item.html', {'form': ItemForm, 'item': item})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user == item.created_by:
        item.delete()
    return redirect('items')


def user_item(request, item_id):
    if request.method == 'POST':
        form = UserItemForm(request.POST)
        if form.is_valid():
            user_item = form.save(commit=False)
            user_item.user = request.user
            user_item.item = Item.objects.get(id=item_id)
            if User_Item.objects.filter(user=user_item.user, item=user_item.item).count() > 0:
                user_item = User_Item.objects.filter(user=user_item.user, item=user_item.item).first()
                user_item.rating = form.cleaned_data['rating']
                user_item.interest = form.cleaned_data['interest']
            user_item.save()
            user_item.item.calc_average()
    return redirect('/item/' + item_id)

def search(request):
    query = request.GET.get('q')
    items = Item.objects.filter(title__icontains = query)
    return render(request, 'search.html', {'items':items, 'query':query})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


def update_interaction(request):

    data = {
        'teste': 'Testando123'
    }

    if request.method == 'POST':
        rating = request.POST.get('rating')
        interest = request.POST.get('interest')
        user_id = request.POST.get('user_id')
        item_id = request.POST.get('item_id')

        user = User.objects.get(id=user_id)
        item = Item.objects.get(id=item_id)


        form = UserItemForm(request.POST)
        if form.is_valid():
            user_item = form.save(commit=False)
            user_item.user = user
            user_item.item = item
            if User_Item.objects.filter(user=user_item.user, item=user_item.item).count() > 0:
                user_item = User_Item.objects.filter(user=user_item.user, item=user_item.item).first()
                user_item.rating = rating
                user_item.interest = interest
            user_item.save()
            user_item.item.calc_average()



        return JsonResponse(data)






