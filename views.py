from django.shortcuts import render
from django.http import HttpResponse
from .form import wishlist
def login(request):
    form=wishlist()
    if request.method=='POST':
        form=wishlist(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'raj/login.html',context)
def home(request):
    form = wishlist()
    if request.method == 'POST':
        form = wishlist(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'raj/home.html', context)
def booking(request):
    form = wishlist()
    if request.method == 'POST':
        form = wishlist(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'raj/booking.html', context)
def confirm(request):
    form = wishlist()
    if request.method == 'POST':
        form = wishlist(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'raj/confirm.html', context)