from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import RegistrationForm

from .models import Question, Choice, UserChoice


# Create your views here.
# def index(request):
# 	latest_question_list = Question.objects.order_by('pub_date')[:5]
# 	#output = ", ".join(q.body for q in latest_question_list)
# 	context = {'latest_question_list' : latest_question_list}
# 	return render(request, 'polls/index.html', context) 

class IndexView(generic.ListView):
	template_name = "polls/index.html"
	context_object_name = "latest_question_list"

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]	
		#__lte - <=
		# -pub_date - в порядке убывания
		

class DetailView(generic.DetailView):
	model = Question
	template_name = "polls/detail.html"

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())	
	

# def detail(request, question_id):	# request - обязателен для всех функций django
# 	# try:
# 	# 	question = Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question does not exists")
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk=question_id)
# 	return render(request, "polls/results.html", {'question': question})

class ResultsView(generic.DetailView):
	model = Question
	template_name = "polls/results.html"	

	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())	
	
class RegisterView(generic.edit.FormView):
	form_class = RegistrationForm
	sucess_url = "/polls/login"
	template_name = "registration/register.html"

	def form_valid(self, form):
		form.save()
		return super(RegisterView, self).form_valid(form)

	def form_invalid(self, form):
		return super(RegisterView, self).form_invalid(form)


def vote(request, question_id):
	if request.user.is_authenticated:
		question = get_object_or_404(Question, pk=question_id)
		try:
			selected_choice = question.choice_set.get(pk=request.POST['choice'])
		except (KeyError, Choice.DoesNotExist):
			context = {"question": question, "error_message": "You didn't select choice"}
			return render(request, 'polls/detail.html', context)
		else:
			founded_user_choice = UserChoice.objects.filter(user=request.user, question=question)
			if not founded_user_choice:
				selected_choice.votes += 1
				selected_choice.save()

				user_choice = UserChoice(question=question, user=request.user)
				user_choice.save()
				return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
			return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
	else:
		return HttpResponseRedirect(reverse('polls:login'))