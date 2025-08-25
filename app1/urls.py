from django.urls import path
from . import views

urlpatterns=[
    path('members/', views.members, name='members' ),
    path('afsal',views.afsal, name='afsal'),
    path('',views.index, name="index"),
    path('user_login/',views.user_login, name="user_login"),
    path('signup/',views.signup,name="signup"),
    path('shop/',views.shop,name="shop"),
    path('services/',views.services,name="services"),
    path('contactus/',views.contactus,name="contactus"),
    path('checkout/',views.checkout,name="checkout"),
    path('cart/',views.cart,name="cart"),
    path('singleproduct/<int:id>/',views.singleproduct,name="singleproduct"),
    path('thankyou/',views.thankyou,name="thankyou"),
    path('about/',views.about,name="about"),
    path('single1/',views.single1,name="single1"),

]