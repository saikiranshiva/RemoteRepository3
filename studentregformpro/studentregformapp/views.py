from django.shortcuts import render
from .models import StudentData
def studentreg_view(request):
    if request.method=="POST":
        roll=request.POST.get('roll','')
        sname=request.POST.get('sname','')
        mobile=request.POST.get('mobile','')
        fee=request.POST.get('fee','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        dod=request.POST.get('dod','')
        gender=request.POST.get('gender','')
        course=request.POST.get('course','')
        institute=request.POST.get('institute','')
        data=StudentData(
            roll_number=roll,
            student_name=sname,
            mobile_number=mobile,
            fee=fee,
            email=email,
            address=address,
            dateofbirth=dod,
            gender=gender,
            courses=course,
            institute_name=institute
        )
        data.save()

        return render(request,'studentregform.html')
    return render(request,'studentregform.html')


