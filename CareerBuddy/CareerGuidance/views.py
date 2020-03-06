from django.shortcuts import render

# Create your views here.
def HomePage(request):
    print("Printed in views.Homepage")
    return render(request,'CareerGuidance/HomePage.html')

def InputForm(request):
    print("Printed in views.InputForm")
    return render(request,'CareerGuidance/InputForm.html')

def Output(request):
    print("Printed in views.Output")
    return render(request,'CareerGuidance/Output.html') 