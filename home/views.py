from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')
# def scheme_view(request):
#     return render(request, 'scheme.html')
