from django.urls import path 
from . import views 

urlpatterns = [
	path("goodslist", view = views.goodslist,name = "goods_list"),
	path("testdb", view = views.testdb,name = "testdb"),
]