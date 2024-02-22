from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
    
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        # redundent serverside validation
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # Delete all value of session 
            # del request.session["tasks"]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    
    # if its not POST by default its GET
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
