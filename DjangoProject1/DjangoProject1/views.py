from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForms
from services.models import Services
from newschanel.models import NewsChanel
from contact.models import contactModel
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.paginator import Paginator
def home(request):


        subject="Django Email"
        from_email="haseenrajput012@gmail.com"
        to="lalitkalra81@gmail.com"
        msg = "<p>This is an <strong>important</strong> message From Django Tutorial</p>"
        msg = EmailMultiAlternatives(subject, msg, from_email, [to]) 
        msg.content_subtype = 'html'
        msg.send()
     
       

#         send_mail(
#     "Testing Email",
#     "Here is the Testing Email Message.",
#     "haseenrajput012@gmail.com",
#     ["haseencomputer016@gmail.com"],
#     fail_silently=False,
# )
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
      c=''
      if request.method=='POST':
            try:
                 
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
      c=''
      if request.method=='POST':
            try:
                 if request.POST.get('n1')=="":
                           return render(request,'evenOdd.html',{'error':True})
                 n=eval(request.POST.get('n1'))
                 if n%2==0 :
                            c="EVEN NUMBER"
                 else:
                            c="ODD NUMBER"
                    
                 
            except Exception as e:
                      print("invalid input .....")
                  

      return render(request,'evenOdd.html',{'c':c})

                      
                    
def StudentMarks(request):
    sum = 0
    per='%'
    if request.method == 'POST':
        try:
            print('before')
            s1 = int(request.POST.get('s1'))
            s2 = int(request.POST.get('s2'))
            s3 = int(request.POST.get('s3'))
            s4 = int(request.POST.get('s4'))
            s5 = int(request.POST.get('s5'))
            sum = s1 + s2 + s3 + s4 + s5
            per=sum*100/500
        except (ValueError, TypeError):
            print("invalid input .....")
            sum = "Invalid input"

    return render(request, 'marksheet.html', {'sum': sum,'per':per})  

def newdetails(request,id):
       newsdetails=NewsChanel.objects.get(id=id) 
       data={
             'newsdetails':newsdetails
       }
       return render(request,"newsdetail.html",data)           

def modelClassData(request):
      
    #   serviceModel=Services.objects.all().order_by('-service_title')[:3]

    #   serviceModel=Services.objects.all().order_by('service_title')[:3]
      serviceModel=Services.objects.all()
      pagintr=Paginator(serviceModel,2)
      pageNo=request.GET.get('page')
      ServiceFinalData=pagintr.get_page(pageNo)
     # news = NewsChanel.objects.all()
    #   if request.method=='GET':
    #         st=request.GET.get('serviceTitle')
    #         if  st!=None :
    #              serviceModel= Services.objects.filter(service_title__icontains=st)
                  


      data={
            # 'news':news,
            # 'serviceModel':serviceModel
            'serviceModel':ServiceFinalData
      }
      return render(request,"model.html",data)


def ContactUS(request):
      m=''
      if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            contact_No=request.POST.get('contact')
            Address=request.POST.get('Address')
            en=contactModel(Name=name,Contact_No=contact_No,email=email,Address=Address)
            en.save()
            m="data inserted  or saved "

      return render(request,"contact.html",{'m':m})
# def savecontactInfo(request):
#       return render(request,"contact.html")