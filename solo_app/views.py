from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Menu_item, User
from .models import File
# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/success')

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    # messages.success(request, "You have successfully logged in!")
    return redirect('/success')

def logout(request):
    request.session.clear()
    messages.success(request, "You have successfully logged out!")
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'dashboard.html', context)

def view_profile(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # update user info
    to_update = User.objects.get(id=request.session['user_id'])
    # updates each field
    to_update.first_name = request.POST['first_name']
    to_update.last_name = request.POST['last_name']
    to_update.age = request.POST['age']
    to_update.address = request.POST['address']
    to_update.city = request.POST['city']
    to_update.state = request.POST['state']
    to_update.email = request.POST['email']
    to_update.save()

    return redirect('/success')

def delete_profile(request):
    to_delete = User.objects.get(id=request.session['user_id'])
    to_delete.delete()
    return redirect('/')

def view_menu(request):
    if 'user_id' not in request.session:
        return redirect('/')
    menu_items = Menu_item.objects.all()
    context = {
        "menu_items": menu_items
    }
    return render(request,'view-menu.html',context)

def share(request):
    if 'user_id' not in request.session:
        return redirect('/')
    images = File.objects.all()
    context = {
        "images": images
    }
    return render(request,'share.html',context)

def add_image(request):
    if request.method == "POST":
        new_file = File(file=request.FILES['image'])
        new_file.save()
        return redirect('/share')

# def delete_image(request):
#     to_delete = File.objects.get(request.FILES['images'])
#     to_delete.delete()
#     return redirect('/suggest-item')