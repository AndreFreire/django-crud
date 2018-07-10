from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import PersonForms
from .models import Person
import json
import requests

HEADERS = {'content-type':'application/json'}
URL_PERSON = "http://localhost:8080/person"

class FirstView(View):
	def get(self, request):
		print("Teste")
		return HttpResponse('pong')

#class NewPersonView(CreateView, LoginRequiredMixin):
class NewPersonView(CreateView):
	model = Person
	form_class = PersonForms
	
	def form_valid(self, form):
		person = dict(self.request.POST.items())
		data_person = {
			'name': person['name'],
			'lastName': person['last_name'],
			'nickname': person['nick_name']
		}

		result = requests.post(URL_PERSON, data=json.dumps(data_person), headers=HEADERS)
	
		return HttpResponseRedirect(reverse_lazy('person_list'))

	
#class DetailPersonView(DetailView, LoginRequiredMixin):
class DetailPersonView(DetailView):
	model = Person
	
	def get_object(self):
		result = requests.get(url='{}/{}'.format(URL_PERSON, self.kwargs['pk']))
		person = json.loads(result.text)
		return person


#class ListPersonView(ListView, LoginRequiredMixin):
class ListPersonView(ListView):
	model = Person
	
	def get_context_data(self, **kwargs):
		context = super(ListPersonView, self).get_context_data(**kwargs)
		result = requests.get(url=URL_PERSON)
		people = json.loads(result.text)
		context['people'] = people
		return context