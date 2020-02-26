from django.shortcuts import render
from .models import *


def index(request):
    # context = {'latest_question_list': latest_question_list}
    context={1: 'Geeks', 2: 'For', 3: 'Geeks'}
    return render(request, 'display/index.html', context)
# Create your views here.
