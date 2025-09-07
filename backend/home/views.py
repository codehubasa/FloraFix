from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')  # or 'home/index.html' if it's inside a folder
# def scheme_view(request):
#     return render(request, 'scheme.html')
