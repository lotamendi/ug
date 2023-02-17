from config import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.forms import TextInput


class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print(self.form_class)

    def dispatch(self, request, *args, **kwargs):
        print(request.user)
        if(request.user.is_authenticated):
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Iniciar sesión'
        return context


class LoginFormView(LoginView):
    template_name = 'login.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for field in self.form_class.base_fields:
            self.form_class.base_fields[field].widget.attrs.update({'class' : 'form-control'})
        # self.form_class.base_fields['username'].widget.attrs.update({'class' : 'form-control'})

    def dispatch(self, request, *args, **kwargs):
        print(request.user.username)
        if(request.user.is_authenticated):
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Iniciar sesión'
        return context
    
    def post(self, request, *args, **kwargs):
        print(self.form_class)
        return super().post(request, *args, **kwargs)