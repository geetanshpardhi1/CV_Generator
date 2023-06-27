from django.shortcuts import render
from .models import Profile

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
    return render(request,'pdf/cv.html',{'cv': user_profile})