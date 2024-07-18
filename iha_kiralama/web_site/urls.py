from django.urls import path
from . import views
#http://127.0.0.1:8000/ ==>  homepage
#http://127.0.0.1:8000/index ==> homepage
#http://127.0.0.1:8000/web_site ==>web_site
#http://127.0.0.1:8000/web_site/3 ==>web_site_details


urlpatterns=[
    path("",views.index, name="home"),
    path("index",views.index),
    path("website",views.website, name="website"),
    path("website/<int:id>",views.website_details, name="website_details"),
#int:id yazılmasının nedeni sabit bir değer olmaması değişken olmasıdır

]