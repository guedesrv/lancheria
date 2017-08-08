from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def add(request):
	print('oi')
	print(request.POST)
	return render(request, 'web/index.html')