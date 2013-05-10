from django.shortcuts import render
from modeling.forms import *

def wemEP_view(request):
    if request.method == 'POST':
        form = wemEP_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            return render(request, 'wemEP.html', {'form': form, 
                                                  'results': 
                                                  'Results go here!'})
    else:
        form = wemEP_form()
    return render(request, 'wemEP.html', {'form': form})

def wemMR_view(request):
    if request.method == 'POST':
        form = wemMR_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            return render(request, 'wemMR.html', {'form': form, 
                                                  'results': 
                                                  'Results go here!'})
    else:
        form = wemMR_form()
    return render(request, 'wemMR.html', {'form': form})
