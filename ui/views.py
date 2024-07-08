from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    print('success')
    data = 'success'
    return render(request, 'index.html', {'context':data} )
