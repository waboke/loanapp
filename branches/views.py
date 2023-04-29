from django.shortcuts import render

# Create your views here.
def add_branche(request):
    return render(request, "branches/addBranch.html")

def view_branches(request):
    return render(request, "branches/viewBranches.html")

