
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def signup(request):
    return render(request, 'myapp/signup.html')

def login_view(request):
    return render(request, 'myapp/login.html')

def matching_view(request):
    return render(request, 'myapp/matching.html')

def community(request):
    return render(request, 'myapp/community.html')

def content(request):
    return render(request, 'myapp/content.html')

def company(request):
    return render(request, 'myapp/company.html')

def custom(request):
    return render(request, 'myapp/custom.html')

def price(request):
    return render(request, 'myapp/price.html')

def shop_detail_page(request):
    return render(request, 'myapp/shop-detail.html')  # หรือชื่อไฟล์ template ที่ถูกต้อง

