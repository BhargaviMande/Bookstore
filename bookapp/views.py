from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def adding(request):
    return render(request,'add_book.html')
def cart(request):
    return render(request,'add_book.html')
def requested(request):
    return render(request,'add_book.html')
def view_books(request):
    return render(request,'add_book.html')

