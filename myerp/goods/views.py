from django.shortcuts import render
from django.http.response import JsonResponse
from goods.models import Test


# Create your views here.
def goodslist(request):
	goodslist = [
		{"id":1,"title":"配电柜", "num":5},
		{"id":1,"title":"配电柜", "num":5},
		{"id":1,"title":"配电柜", "num":5}
	]
	return JsonResponse(goodslist, safe=False)

def testdb(request):
	test1 = Test(name="jwjsjg")
	test1.save()
	pass