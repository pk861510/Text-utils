# I have created this file _ Prince(27 01 24)

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("WELCOME TO OUR WORLD(Mr Prince)")
    # dict={'Name':'Prince','Place':'Bihar'}
    return render(request,'index.html')
def analyze(request):
    # Get the text from textarea in index.html name = 'text'
    djtext=(request.POST.get('text','default'))
    djremovepunc =(request.POST.get("removepunc",'off'))
    djspaceremove = (request.POST.get("spaceremove",'off'))
    djuppercase = (request.POST.get("uppercase",'off'))
    djcharcount = (request.POST.get("charcount",'off'))
    djnewlineremover = (request.POST.get("newlineremover",'off'))

    # print(djremovepunc)
    # print(djtext)
    # analyzed = djtext

    punctuation= '''! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ \ { | } ~'''
    punctuation=punctuation.replace(" ","")
    # analyzed = ""

    if djremovepunc=='on':
        analyzed = ""
        for chair in djtext:
            if chair not in punctuation:
                analyzed = analyzed + chair
        # params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # Analyse the text
        # return render(request, 'analyze.html', params)
        djtext=analyzed
        # print(djtext)

    if djspaceremove=='on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]==" "):     
                analyzed = analyzed+char

            # if djtext[index]==" " and djtext[index+1]==" ":                    # Out of range? wht this will give the error
            #     pass
            # else:
            #     analyzed = analyzed + char

        djtext = analyzed
        print(djtext)
        # params = {'purpose': 'Extra space Remover', 'analyzed_text': analyzed}
        # Analyse the text
        # return render(request, 'analyze.html', params)

    if djuppercase=='on':
        analyzed = ''
        for text in djtext:
            analyzed=analyzed+text.upper()
        djtext = analyzed
        print(djtext)
        # params = {'purpose': 'Text in Upper case', 'analyzed_text': analyzed}
        # Analyse the text
        # return render(request, 'analyze.html', params)



    if djnewlineremover=="on":
        analyzed =""
        for char in djtext:
            if "\n"!=char and "\r"!= char:
            # if "\n" not in char and "\r" not in char:
                analyzed = analyzed+char
        print(analyzed)
        djtext = analyzed

    params = {'purpose': 'Analysing the text', 'analyzed_text': analyzed}
    # Analyse the text
    return render(request, 'analyze.html', params)

    # if djcharcount=="on":
    #     cnt=len(djtext)
        # params = {'purpose': 'Character count', 'analyzed_text': f"Number of character in your given text is:- {analyzed}"}
        # Analyse the text
        # return render(request, 'analyze.html', params)
        # djtext = analyzed
        # print(cnt)






        # Analyse the text
        # params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        # print(djtext)

    # By chag gpt
    # """if djtext:
    #     analyzed = ""
    #     for char in djtext:
    #         if char != '\n':  # Check for newline characters
    #             analyzed += char
    #     params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)"""

    # else:
    #     return HttpResponse(" Error: No text provided for analysi.")


def about(request):
    return render(request,"about.html")
    # return HttpResponse('''<h1>I am Mr Prince Kumar</h1> <h1>Phone:-7645091386</h1><div>
    #  <h1>Email I'd:-pk861510@gmail.com<div>
    #  <div>
    #  <a href = "https://www.instagram.com/__unique_boy_prince_/" target="_blank"> Instagram link </a> <div>
    #  <a href = "https://www.facebook.com/stories/163790601254721/UzpfSVNDOjY2MzAyNDM4OTEzNjAwMQ==/?bucket_count=9&source=story_tray"target="_blank"> Facebook Page </a> <div>
    #  <a href = "https://www.linkedin.com/feed/"target="_blank">LInkedin Page of Future Developer<div>
    #  <a href = '/'>Back</a><div>
    #  <a href= 'http://127.0.0.1:8000/'>Home Page</a><div>
    #       ''')

















#
# def capfirsrt(request):
#     return HttpResponse("Capitalised first page Smile your page is ready to rock")
# def newlineremove(request):
#     return HttpResponse("Remove new line Pagee ")
# def spaceremove(request):
#     return HttpResponse("Spaceremove page Created by Mr Prince Future Full Stake Developer")
# def charcount(request):
#     return HttpResponse("this is charcounr page")



# def index(request):
#     # return HttpResponse("I'm MR Prince")
#     return HttpResponse ('''<h1> MR Prince(Favourite singer) </h1> <a href = "https://www.youtube.com/@adityayadav6724/videos"> Songs Aditya yadav </a>''' )
# def about(request):
#     return HttpResponse("I'm the best person in this world")



# from django.http import HttpResponse
# from django.shortcuts import render

# def about(request):
#     return HttpResponse('''<h1>I am Mr Prince Kumar</h1>
#     <h1>Phone:-7645091386</h1>
#     <div>
#         <h1>Email I'd:-pk861510@gmail.com<div>
#         <div>
#             <a href="https://www.instagram.com/__unique_boy_prince_/" target="_blank">Instagram link</a>
#         </div>
#         <div>
#             <a href="https://www.facebook.com/stories/163790601254721/UzpfSVNDOjY2MzAyNDM4OTEzNjAwMQ==/?bucket_count=9&source=story_tray" target="_blank">Facebook Page</a>
#         </div>
#         <div>
#             <a href="https://www.linkedin.com/feed/" target="_blank">Linkedin Page of Future Developer</a>
#         </div>
#         <div>
#             <a href="/">Back</a>
#         </div>
#         <div>
#             <a href="http://127.0.0.1:8000/" target="_blank">Home Page</a>
#         </div>
#     ''')
