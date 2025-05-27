from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # import views ทั้งหมด

urlpatterns = [
    path('', views.index, name='home'),  # root path
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('matching/', views.matching_view, name='matching'),
    path('community/', views.community, name='community'),
    path('content/', views.content, name='content'),
    path('company/', views.company, name='company'),
    path('custom/', views.custom, name='custom'),
    path('price/', views.price, name='price'),
    path('shop-detail/', views.shop_detail_page, name='shop-detail'),  # อย่าลืมสร้างฟังก์ชันนี้ใน views.py
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
