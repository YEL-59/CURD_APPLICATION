from django.shortcuts import redirect, render
from student.models import *
# Create your views here.
def all_students(request ,*args, **kwargs):
    if request.method == "GET":
        std = Students.objects.all()
        context = {
            'student': std
        }
        return render(request, 'index.html', context)
    elif request.method == "POST":
        Name = request.POST['name']
        Varsity_id = request.POST['Vid']
        Blood_group = request.POST['bgrp']
        phone_number = request.POST['phn']
        Email = request.POST['email']

        Students.objects.create(name=Name, varsity_id=Varsity_id, blood_group=Blood_group, phone=phone_number, email=Email )
    return redirect('/home')

def edit_delet(request, action, sid):
    if action == 'delete':
        selected_student = Students.objects.get(id=sid)
        selected_student.delete()
    if action == 'edit':
        if request.method == "GET":
            selected_student = Students.objects.get(id=sid)
            context = {
                'student': selected_student
            }
            return render(request, 'edit.html', context)
        elif request.method == 'POST':

            Name1 = request.POST['name']
            Varsity_id1 = request.POST['Vid']
            Blood_group1 = request.POST['bgrp']
            phone_number1 = request.POST['phn']
            Email1 = request.POST['email']

            selected_student = Students.objects.get(id=sid)

            selected_student.name = Name1
            selected_student.varsity_id = Varsity_id1
            selected_student.blood_group = Blood_group1
            selected_student.phone = phone_number1
            selected_student.email = Email1

            selected_student.save()








    return redirect('/home')


def show(request, *args, **kwargs):
    if request.method == "GET":
        query = Students.objects.all()
        context = {
            "object": query
        }
        return render(request, 'show.html', context)

    #return redirect('/home')
def search(request,*args, **kwargs):
    if request.method == "GET":
        return render(request, "search.html")
    elif request.method == "POST":
        name = request.POST['search']

        value = Students.objects.get(name=name)

        context = {
            "std": value
        }
        return render(request, "search.html", context)
