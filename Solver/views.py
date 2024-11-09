from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *



def get_all_carr(request):
    tasks = User.objects.all()
    return render(request,"list_u.html",context={"object_list":tasks})


def get_by_id(request,pk):
    tasks  = User.objects.filter(id=pk).first()
    if tasks:
        return render(request,"detail_u.html",context={"object":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
def add(request):
    if request.method == "POST":
        form  = Tasksform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("list_u")
    else:
        form = Tasksform()
    return render(request,"create_u.html", context={"form":form})



def update(request,pk):
    tasks  = User.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Tasksform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("list_u")
        else:
            form = Tasksform(instance=tasks)
            
        return render(request,"update_u.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
def delete(request,pk):
    tasks =  User.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("list_u")
        else:
            return render(request,"delete_u.html",context={"object":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
    
def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())

# Category  



def get_all_carr1(request):
    tasks = Category.objects.all()
    return render(request,"list_c.html",context={"object_list":tasks})


def get_by_id1(request,pk):
    tasks  = Category.objects.filter(id=pk).first()
    if tasks:
        return render(request,"detail_c.html",context={"object":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
def add1(request):
    if request.method == "POST":
        form  = Taksform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("list_c")
    else:
        form = Taksform()
    return render(request,"create_c.html", context={"form":form})



def update1(request,pk):
    tasks  = Category.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Taksform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("list_c")
        else:
            form = Taksform(instance=tasks)
            
        return render(request,"update_c.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
def delete1(request,pk):
    tasks =  Category.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("list_c")
        else:
            return render(request,"delete_c.html",context={"object":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
    
# Talant




def get_all_carr11(request):
    tasks = Talant.objects.all()
    return render(request,"list_m.html",context={"object_list":tasks})


def get_by_id11(request,pk):
    tasks  = Talant.objects.filter(id=pk).first()
    if tasks:
        return render(request,"detail_m.html",context={"object":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
def add11(request):
    if request.method == "POST":
        form  = Takform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("list_m")
    else:
        form = Takform()
    return render(request,"create_m.html", context={"form":form})



def update11(request,pk):
    tasks  = Talant.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Takform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("list_m")
        else:
            form = Takform(instance=tasks)
            
        return render(request,"update_m.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
def delete11(request,pk):
    tasks =  Talant.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("list_m")
        else:
            return render(request,"delete_m.html",context={"object":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>") 
    
    
    
# Aplication 
def get_all_carr111(request):
    tasks = Aplication.objects.all()
    return render(request,"list_o.html",context={"object_list":tasks})


def get_by_id111(request,pk):
    tasks  = Aplication.objects.filter(id=pk).first()
    if tasks:
        return render(request,"detail_o.html",context={"object":tasks})
    else:
        return HttpResponse("Tasks object not found")
    
    
def add111(request):
    if request.method == "POST":
        form  = Taform(request.POST,request.FILES )
        if form .is_valid():
            form.save()
            return redirect("list_o")
    else:
        form = Taform()
    return render(request,"create_o.html", context={"form":form})



def update111(request,pk):
    tasks  = Aplication.objects.filter(id=pk).first()   
    if tasks:
        if request.method == "POST":
            form  = Taform(request.POST,request.FILES, instance=tasks)
            if form .is_valid():
                form.save()
                return redirect("list_o")
        else:
            form = Taform(instance=tasks)
            
        return render(request,"update_o.html", context={"form":form})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>")
    
    
    
def delete111(request,pk):
    tasks =  Aplication.objects.filter(id = pk).first()
    if tasks:
        if request.method == "POST":
            tasks.delete()
            return redirect("list_o")
        else:
            return render(request,"delete_o.html",context={"object":tasks})
    else:
        return HttpResponse("<h2>Tasks object not found id- ro dar bolo vorid kuned</h2>") 