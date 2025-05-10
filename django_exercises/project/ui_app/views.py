from django.shortcuts import render

# Create your views here.

def show_pretty_ui(request):
    return render(request, 'pretty_ui.html')