from django.shortcuts import redirect, render
from django.http import HttpResponse

from lists.models import Item
# Create your views here.

def home_page(request):
    """ домашняя страница """
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/один-единственный-список-в-мире/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def view_list(request):
    """ представление списка """
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})