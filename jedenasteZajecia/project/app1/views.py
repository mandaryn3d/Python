from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from app1.models import Question, Choice
import datetime

# Create your views here.
def index(reposnse):
    return HttpResponse("Hello World!")

def pass_a_paramater(reposnse, message=None):
    message = reposnse.GET.get('message')
    return HttpResponse("Custom message: " + message)

def html_template(response):
    now = datetime.datetime.now()
    t = Template('''
<html>
<body>
This is a html template.<br>
It is now {{ current_date }}.
</body>
</html>
''')
    html  = t.render(Context({'current_date': now}))
    return HttpResponse(html)
    
def get_object_by_id(reposnse, message=None):
    message = reposnse.GET.get('message')
    q = Question.objects.get(pk=message)
    return HttpResponse("Requested question: " + 'Id: ' + str(q.id) + ' Name: ' + str(q) + ' Date: ' + str(q.pub_date))
    
def get_all_objects(reposnse):
    qList = []
    for entry in Question.objects.all():
        qList.append(entry)    

    stringToBeConverted ='''
<html>
<body>
This is a html template.<br>
It shows list of questions taken from database.<br>
'''
    for entry in qList:
        stringToBeConverted += ('Id: ' + str(entry.id) + ' Name: <a href=\"http://127.0.0.1:8000/app1/db/?message=' +str(entry.id)+ '\">' + str(entry) +'</a><br>')
    stringToBeConverted  +='''
</body>
</html>
'''
    t = Template(stringToBeConverted)
    html = t.render(Context())
    return HttpResponse(html)
