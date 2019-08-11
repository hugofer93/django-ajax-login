import json

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
class Index(TemplateView):
    http_method_names = ['get']
    template_name = 'core/index.html'


class Login(LoginView):
    http_method_names = ['get', 'post']
    template_name = 'core/login.html'

    def get(self, request, *args, **kwargs):
        if 'search' in request.GET:
            data = None
            status = None

            search = request.GET['search']

            try:
                query = (
                    Q(username = search) |
                    Q(email = search)
                )
                user = User.objects.get(query)
                data = {'username': user.username}
                status = 200
            except User.DoesNotExist:
                data = {'error': 'User does not exist'}
                status = 404

            return JsonResponse(data, safe=False, status=status)
            
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = None
        status = None

        form = self.form_class(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                data = {'success': True}
                status = 200

        else:
            data = json.dumps(dict(form.errors.items()), ensure_ascii=False)
            status = 401

        return JsonResponse(data, safe=False, status=status)


class Home(LoginRequiredMixin, TemplateView):
    http_method_names = ['get']
    template_name = 'core/home.html'

    def get_login_url(self):
        return reverse('core:login')


class Logout(LogoutView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('core:index'))