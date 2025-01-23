from django.shortcuts import render

def frontpage(request):
    return render(request,'core/frontpage.html')
    
def sobre(request):
    return render(request,'core/sobre.html')