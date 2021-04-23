from django.shortcuts import render

# Create your views here.

def home(request):
   m=''
   if request.method =='POST':
      email = request.POST['email']
      number = request.POST['number1']
      msg = request.POST['message']
      m = 'done'
      
   context = {
         'm':m, 
      }
   return render(request,'mysiteapp/samo.html',context)
