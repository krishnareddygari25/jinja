from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this is the jinja printing tags'
    d={'printing':data}
    return render(request,'data_render',context=d)


def login(request):
    d={'username':'Anusha'}
    return render(request,'login.html')
