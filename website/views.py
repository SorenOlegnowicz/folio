from django.shortcuts import render, render_to_response

def homepage(request):
    context = {}
    return render_to_response('webpage.html', context)
