from django.shortcuts import render

#render(request, template file, context)

def service_list(request):
	return render(request, 'service/service_list.html')
