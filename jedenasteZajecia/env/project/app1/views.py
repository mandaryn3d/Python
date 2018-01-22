from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
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
