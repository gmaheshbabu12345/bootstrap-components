from django.shortcuts import render

# Create your views here.
def component1(request):
    return render(request,'component1.html')