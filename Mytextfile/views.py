from django.shortcuts import render
from django.http import HttpResponse
import re



def home(request):
    return render(request, 'home.html')

def textmaster(request):
    return render(request, 'textmaster.html')

def email_v(request):
    
    return render(request, 'email_v.html')

def email_check(request):
    
    if request.method == 'GET':
        
        mytext2= str(request.GET.get('test2','default'))
        emails= re.findall("[^,;\s]+@[^,;\s]+", mytext2)
        emails=''.join(emails)
        print(emails)
        return render(request, 'email_check.html', {'your_email': emails})

def result(request):

    mytext= str(request.GET.get('test1','default'))
    removeP= request.GET.get('remove_punc','off')
    upper_text= request.GET.get('upper_case','off')
    lower_text= request.GET.get('lower_case','off')
    remove_number= request.GET.get('remove_numbers','off')
    remove_space= request.GET.get('remove_space', 'off')
    
    num='0123456789'
    
    if (removeP== "on"):
        emails= re.findall("[A-Z a-z 0-9]", mytext)
        removePunc=  ''.join(emails)
        parms={'Purpose': 'Remove punctuation', 'your_text':removePunc}
        return render(request, 'result.html', parms)

    elif (upper_text== "on"):
        upper_St=""
        for char_l in mytext:
            upper_St=upper_St+char_l.upper()
        parms={'Purpose': 'Upper Case ', 'your_text': upper_St}
        return render(request, 'result.html',parms)
    elif (lower_text== "on"):
        lower_St=""
        for char_l in mytext:
            lower_St = lower_St+char_l.lower()
        parms={'Purpose': 'LowerCase ', 'your_text':lower_St}
        return render(request, 'result.html',parms)

    elif (remove_number== "on"):
        removeN=""
        for char_l in mytext:
            if char_l not in num:
                removeN = removeN+char_l
        parms={'Purpose': 'Removed Number', 'your_text':removeN}
        return render(request, 'result.html',parms)
    elif (remove_space=="on"):
        analyzed = ""
        for index, char in enumerate(mytext):
            if char == mytext[-1]:
                    if not(mytext[index] == " "):
                        analyzed = analyzed + char
        parms={'Purpose': 'Remove Space', 'your_text':analyzed}
        return render(request, 'result.html',parms)
    else:
        parms={'Purpose': 'Please Select any option to see Magic...', 'your_text':mytext}
        return render(request, 'result.html',parms)
    

def face_det(request):
    return render(request, 'face_det.html')
