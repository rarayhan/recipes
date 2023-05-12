from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
def search_recipes(request):
    query = request.GET.get('query')
    recipes = Recipe.objects.filter(title__icontains=query)
    return render(request, 'search.html', {'recipes': recipes})
def save_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    request.user.userprofile.favorite_recipes.add(recipe)
    return redirect('recipe_details', recipe_id=recipe_id)

