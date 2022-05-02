from django.shortcuts import render, redirect
from .models import Person
# Create your views here.


def list_person (request):
    persons=Person.objects.all()
    context = {'persons': persons}
    return render(request, 'index.html', context)

def create_person(request):
    name = request.POST["name"]
    surname = request.POST["surname"]
    age = request.POST["age"]
    person=Person(name=name, surname=surname, age=age)
    person.save()  
    return  redirect('/persona/') 

def delete_person(request, id):
    person= Person.objects.get(id=id)
    person.delete()
    return  redirect('/persona/') 