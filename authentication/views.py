from django.shortcuts import render

# Create your views here.
def add_user(request):
    return render(request, "authentication/addUser.html")

def view_users(request):
    return render(request, "authentication/viewUsers.html")
