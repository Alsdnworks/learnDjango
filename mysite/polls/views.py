from django.http import HttpResponse, Http404
from .models import Question,Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
import django.shortcuts as shortcuts
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 에러 메세지와 함께 폼을 다시 디스플레이합니다.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터 처리를 정상적으로 마친 뒤에는 항상 HttpResponseRedirect를 리턴합니다.        
        # 이 방법을 통해 유저가 브라우저의 "뒤로가기"을 눌렀을 때
        # 데이터가 두 번 저장되는 것을 방지할 수 있습니다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))