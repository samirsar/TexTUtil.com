# i have created this file 
from typing import Text
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''   <h1>five best website</h1>
#     <ul>
#        <li><a href="https://www.linkedin.com/in/samir-kumar-893b1a1a7/">linkdin</a></li>
#        <li><a href="https://www.linkedin.com/in/samir-kumar-893b1a1a7/"></a>linkdin</li>
#        <li><a href="https://www.linkedin.com/in/samir-kumar-893b1a1a7/"></a>linkdin</li>
#        <li><a href="https://www.linkedin.com/in/samir-kumar-893b1a1a7/"></a>linkdin</li>
#     </ul>''')
# def about(request):
#     return HttpResponse("About")


def index(request):
    return render(request,"index.html")
    # return HttpResponse("HOME")
def analyze(request):
    list=[]
    djtext = request.POST.get("text","default")
    removepunc1=request.POST.get("removepunc","off")
    capital_letter=request.POST.get("capital_letter","off")
    extra_space=request.POST.get("extra_space","off")
    newlineremove=request.POST.get("newlineremove","off")
    char_count=request.POST.get("char_count","off")
    ans=""
    print(djtext)
    flag=0
    if(removepunc1=="on"):
        # def removepunc(request):
            list.append("removepuctuation")
            str1='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for c in djtext:
                if(c not in str1):
                    ans=ans+c
            flag=1
                    

            

    if(capital_letter=="on"):
        # def capitalize(request):
        list.append("capitalize the text")
        if(flag):
            ans=ans.upper()
        else:
            ans=djtext.upper()


        flag=1

        
            

    if(extra_space=="on"):
        # def spaceremove(request):
            list.append("remove the extra space")
            if(flag):
                djtext=ans

            ans=""
            for i in range(0,len(djtext)):
                if(i!=len(djtext)-1 and djtext[i]==" "and djtext[i+1]==" "):
                    pass
                else:
                    ans=ans+djtext[i]


            flag=1

    if(newlineremove=="on"):
        # def newline(request):
            list.append("newline")
            if(flag==1):
                djtext=ans

            ans=""
            for c in djtext:
                if(c!="\n" and c!="\r"):
                    ans=ans+c
                else:
                    ans=ans



            flag=1


            
            



            



    if(char_count=="on"):
        # def charcount(request):
            list.append("count the character in text")
            x=0
            if(flag):
                djtext=ans

            for c in djtext:
                if(c!=" "):
                    x=x+1

            ans= str(x)

            flag=1

    if(flag==0):
        return HttpResponse("error")


    # print(ans)

    
    param={"purpose":list,"text":ans}
    
    return render(request,'analyze.html',param)












