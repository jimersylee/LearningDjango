from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))


# 问题详情
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question not found")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "you are looking at results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = "you are voting on question %s"
    return HttpResponse(response % question_id)
