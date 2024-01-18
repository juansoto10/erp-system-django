"""Production app views"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Dashboard
@login_required(login_url='user-login')
def dashboard(request):
    
    # all_records = Record.objects.all()
    
    # context = {'records': all_records}
    
    return render(request, 'production/dashboard.html')

