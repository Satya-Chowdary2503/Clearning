"""CLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from quiz import views
from django.contrib.auth import views as g

urlpatterns = [
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="ct"),
    path('rg/',views.register,name="reg"),
    path('pf/',views.profile,name="prf"),
    path('upf/',views.updf,name="upfe"),
    path('lg/',g.LoginView.as_view(template_name="html/login.html"),name="lgn"),
    path('lgg/',g.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
    path('st/',views.start,name="strt"),
    path('intr/',views.intro,name="int"),
    path('str/',views.structer,name="struct"),
    path('car/',views.char,name="ca"),
     path('con/',views.constants,name="co"),
    path('oper/',views.operators,name="op"),
    path('lop/',views.loops,name="lo"),
    path('arr/',views.array,name="ar"),
    path('coc/',views.conc,name="con"),
    path('',views.examonline),
]
