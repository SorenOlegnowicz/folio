from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from reportlab.pdfgen import canvas

from .models import Contact


def homepage(request):
    context = {}
    if request.POST:
        Contact.objects.create(name=request.POST['name'], email=request.POST['email'], message=request.POST['message'])
    return render_to_response('webpage.html', context, context_instance=RequestContext(request))

def pdf_views(request):
    context = {}
    return render_to_response('pdf.html', context, context_instance=RequestContext(request))


# Not thread safe
# def pdf_view(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
#     p = canvas.Canvas(response)
#
#     p.showPage()
#     p.save()
#     return response
