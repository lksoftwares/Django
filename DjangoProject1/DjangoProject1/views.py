from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForms

def home(request):

    # data={
    #     'title':'Home-Page',
    #     'homeData':' Welcome to  Home page of our  Website',
    #     'subjectList':['Php','java','python','Node'],
    #     'numbers':[90,67,54,67,43],
    #     'studDetails':[
    #         {'name':'Rahul','PhoneNo':908767},
    #         {'name':'Rihan','PhoneNo':908767},

    #     ]

    # }
    # return render(request,"index.html",data)
        return render(request,"web.html")

def about(request):

    data={
        'title':'Home-Page',
        'homeData':' Welcome to  Home page of our  Website',
        'subjectList':['Php','java','python','Node'],
        'numbers':[90,67,54,67,43],
        'studDetails':[
            {'name':'Rahul','PhoneNo':908767},
            {'name':'Rihan','PhoneNo':908767},

        ]

    }
    return render(request,"about.html",data)
def welcome(request):
    return HttpResponse("Welcome to our first view ")
def welcomeDynamic(request,id):
    return HttpResponse(id)
def userForm(request):
     fn=userForms()
     res=0
     data={'form':fn}
     try:
         if  request.method=='POST':
              a=int(request.POST.get('a'))
              b=int(request.POST.get('b'))
              res = a + b
              
              data={
                  'form':fn,
                   'output':res
              }
              print(res)
              url="/?output={}".format(res)
              return HttpResponseRedirect(url)
       
     except Exception as ex:     
          print(ex)
  
     return render(request,'userform.html',data)

def submitForm(request):
     res=0
     try:
         if  request.method=='POST':
              a=int(request.POST.get('a'))
              b=int(request.POST.get('b'))
              res = a + b
              
              return HttpResponse(res)
       
     except Exception as ex:     
          print(ex)
     
def calculator(request):
      if request.method=='POST':
            try:
                 c=''
                 n1=eval(request.POST.get('n1'))
                 n2=eval(request.POST.get('n2'))
                 opr=request.POST.get('Operation')
                 if opr=='+':
                      c=n1+n2
                      
                 elif opr=='-':
                      c=n1-n2    
                 elif opr=='*':
                      c=n1*n2   
                 elif opr=='/':
                      c=n1/n2         
                         
                 

            except Exception as e:
                      print("invalid input .....")
            print(c)          

            return render(request,'calculator.html',{'c':c})
      


    
       
   
def EvenOdd(request):
      if request.method=='POST':
            try:
                   c=''
                   n=eval(request.POST.get('n1'))
                   if n%2==0 :
                    c="EVEN NUMBER"
                   else:
                    c="ODD NUMBER"
            
                   print(c)
            except Exception as e:
                      print("invalid input .....")
                  

      return render(request,'calculator.html',{'c':c})