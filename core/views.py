from django.shortcuts import render
from django.http import JsonResponse
import json

import requests
from bs4 import BeautifulSoup


def index(request):
	return render(request, 'core/index.html')


def search_word(request):
	word = request.GET.get('word', None)

	page = requests.get('https://www.dicio.com.br/' + word + "/")
	soup = BeautifulSoup(page.content, 'html.parser')

	week = soup.find_all(class_="adicional sinonimos")

	sinonimos = []

	try:
		for sinonimo in week[0].find_all('a'):
			sinonimos.append(sinonimo.text)
	except:
		sinonimos.append('Nenhuma definição encontrada')

	serialized_sinonimos = json.dumps(sinonimos)

	antonimos = []

	try:
		for antonimo in week[1].find_all('a'):
			antonimos.append(antonimo.text)
	except:
		antonimos.append('Nenhuma definição encontrada')		

	serialized_antonimos = json.dumps(antonimos)

	context = {
		'sinonimos': serialized_sinonimos,
		'antonimos':serialized_antonimos
	}

	return JsonResponse(context)