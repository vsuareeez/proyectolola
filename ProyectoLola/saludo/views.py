from django.shortcuts import render,HttpResponse
from .models import Details
def saludo(request):
    data = request.POST.get('name')
    try:
        datos = data
        extraccionsql = Details.objects.get(id=datos)
        data = (extraccionsql.name,extraccionsql.type)
    except:
        data = data
    print(data)
    return render(request, 'index.html',{'data':data})
