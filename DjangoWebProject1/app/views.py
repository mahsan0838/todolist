"""
Definition of views.
"""

###################  APP  #####################

from cgitb import text
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse, HttpResponseRedirect
from main.models import ToDoList, Item
from .forms import CreateNewList

# create views here



def index(response, id):
    ls= ToDoList.objects.get(id=id)
    
    if ls in response.user.todolist.all():
        if response.method=="POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id))=="clicked":
                        item.complete=True
                    else:
                        item.complete=False
                    item.save()
            elif response.POST.get("newItem"):
                txt = response.POST.get("new")
                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")
        return render(response, "main/list.html", {"ls":ls})
    return render(response, "main/view.html", {})

def home(response):
     return render(response, "main/home.html", {"name":"test"})

def create(response):
    if response.method=="POST":
        form= CreateNewList(response.POST)
        
        if form.is_valid():
            n= form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()      
    return render(response, "main/create.html", {"form":form})


def view(response):
    return render(response, "main/view.html", {})

# def home(request):
#     """Renders the home page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/index.html',
#         {
#             'title':'Home Page',
#             'year':datetime.now().year,
#         }
#     )

# def contact(request):
#     """Renders the contact page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/contact.html',
#         {
#             'title':'Contact yo mama',
#             'message':'Your contact page.',
#             'year':datetime.now().year,
#         }
#     )

# def about(request):
#     """Renders the about page."""
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/about.html',
#         {
#             'title':'About',
#             'message':'Your application description page.',
#             'year':datetime.now().year,
#         }
#     )
