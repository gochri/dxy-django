from django.shortcuts import render
from sentimentanalysis.models import Epidemic
from sentimentanalysis.models import China
import json
# Create your views here.
def D3Analytics(request):
	print("test")
	china_list = China.objects.all()
	print(type(china_list))
	print(china_list)
	#for i in range(1,35):
	#	print(china_list[i])	
	Lis = list(china_list)
	#for i in Lis:
		#print(i)
		#print(type(i))
		#print(Lis(1))
	context={
		'china_list':china_list,
		#'List': json.dumps(List),
		}
	return render(request, 'D3XAnalytics.html', context)

def DXYAnalytics(request):
	epidemic_list = Epidemic.objects.all()
	print(type(epidemic_list))
	print(epidemic_list)

	# 分页算法
	perpage = 10
	maxPage = int((len(epidemic_list) - 1) / perpage + 1)

	page = request.GET.get('page')
	try:
		page = int(page)
	except:
		page = 1
	if page > maxPage:
		page = 1
	elif page <= 0:
		page = maxPage

	minIndex = (page - 1) * perpage
	maxIndex = page * perpage

	if maxIndex > len(epidemic_list):
		maxIndex = len(epidemic_list)

	epidemic_list = epidemic_list[minIndex : maxIndex]

	context={
		'epidemic_list':epidemic_list,
		'page': page,
		'message': '疫情数据',
		}
	return render(request, 'DXYAnalytics.html', context)