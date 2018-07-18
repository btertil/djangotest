from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class DetailInfo(generic.DetailView):
    model = Question
    template_name = 'polls/info_template.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
          'question': question,
          'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def info(request):
    html = """
        <h2>To jest po prostu HttpResponse</h2><br><p>A to jakiś paragraf</p><br>request = '%s'<br>
        <a href=\"/polls\">back to app page</a>
    """ % str(request)

    return HttpResponse(html)


def testowytemplate(request):
    template = loader.get_template('polls/testowytemplate.html')
    return HttpResponse(template.render({'raz': 1, 'dwa': 2, 'trzy': 3}, request))
