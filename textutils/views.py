# I have created this file
from django.http import HttpResponse
from django.shortcuts import render



# home 
def home(request):
    return render(request, 'home.html')
    
# contact
def contact(request):
    return render(request, 'contact.html')

# analize
def blog(request):
    # Getting text
    blogText = request.GET.get('text', 'off')

    # check checkbox value on or off
    checkRemoveButton = request.GET.get('punc', 'off')
    caps = request.GET.get('caps', 'off')
    small = request.GET.get('small', 'off')
    newLine = request.GET.get('newLine', 'off')
    spaceRemover = request.GET.get('spaceRemover', 'off')

    if (checkRemoveButton == "off" and caps == "off" and small == "off" and newLine == "off" and spaceRemover == "off" or blogText == ''):
        analyzed = "Hello World!"
        params = {'purpose': 'You Does Not Select Any Operation', 'analyzed_text': analyzed}
        blogText = analyzed

    # checking checkbox is on 
    if (checkRemoveButton == "on"):
        # list of punctuation 
        punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~`'''
        analyzed = ""

        # putting value in char
        for char in blogText:

            # removing punctuation
            if char not in punctuation:
                analyzed = analyzed + char

        # putting value into params
        params = {'purpose':'Remove Punctuation', 'analyzed_text': analyzed}
        
        # updating blogText
        blogText = analyzed
    
    # checking Capatllize checkbox
    if (caps == "on"):
        analyzed = ""

        # putting text into char
        for char in blogText:

            # Capatllizing text 
            analyzed = analyzed + char.upper()
        
        # putting value into params
        params = {'purpose': 'Change To Upper Case Latter', 'analyzed_text': analyzed}

        # updating blogText
        blogText = analyzed

    # Checking for Smallization checkbox
    if (small == "on"):
        analyzed = ""

        # putting text into char
        for char in blogText:

            # converting text into small letters
            analyzed = analyzed + char.lower()
        
        # putting value into params
        params = {'purpose': 'Change To Lower Case Latter', 'analyzed_text': analyzed}

        # updating blogText
        blogText = analyzed
    # checking for newline checkbox
    if (newLine == "on"):
        analyzed = ""

        # putting text into char
        for char in blogText:
            # checking for new line keywords
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        # putting value into params
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # updating blogText
        blogText = analyzed
    # checking extra space Remover
    if (spaceRemover == "on"):
        analyzed = ""
        # checking index and putting value into char
        for index, char in enumerate(blogText):
            # It is for if a extraspace is in the last of the string
            if char == blogText[-1]:
                    if not(blogText[index] == " "):
                        analyzed = analyzed + char

            elif not(blogText[index] == " " and blogText[index+1]==" "):                        
                analyzed = analyzed + char
        # putting values in params
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        blogText = analyzed

    return render(request, 'blog.html', params)
