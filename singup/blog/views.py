from django.shortcuts import render
from django.urls import reverse_lazy
from  django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
class IndexView ( LoginRequiredMixin, View ):
    login_url = reverse_lazy('login_url')
    def get(self, request):
        return render(request, 'blog/index.html', context={'text': 'Hello World'})
