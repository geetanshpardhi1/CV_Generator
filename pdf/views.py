from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import io,os
import pdfkit

# Create your views here.
def form(request):
    if request.method == "POST":
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        degree = request.POST.get('degree',"")
        school = request.POST.get('school',"")
        about = request.POST.get('summary',"")
        university = request.POST.get('university',"")
        previous_work = request.POST.get('exp',"")
        skills = request.POST.get('skills',"")
        
        f = Profile(name=name,email=email,phone=phone,degree=degree,school=school,summary=about,university=university,previous_work=previous_work,skills=skills)
        f.save()           
    return render(request,'pdf/form.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/cv.html')
    html = template.render({'cv':user_profile})
    options ={
        'page-size':'Letter',
        'encoding':"UTF-8",
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] ='attachment'
    filename = "resume.pdf"
    return response
