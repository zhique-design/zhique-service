import binascii
import os
from urllib import parse

from django.contrib import auth
from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from rest_framework.reverse import reverse

from .forms import LoginForm


# Create your views here.

def get_redirect_uri(request):
    redirect_uri = request.GET.get('redirect_uri', None)
    from django.conf import settings
    return redirect_uri if redirect_uri else settings.FRONT_BASE_URL


class LoginView(FormView):
    """登录视图"""
    form_class = LoginForm
    template_name = 'oauth/login.html'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['redirect_to'] = get_redirect_uri(self.request)
        return super(LoginView, self).get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=self.request.POST, request=self.request)
        if form.is_valid():
            auth.login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
        return self.render_to_response({
            'form': form
        })

    def get_success_url(self):
        authorize_uri = reverse('authorize', request=self.request, kwargs={
            'authorize_type': 'account'
        })
        data = parse.urlencode({
            'response_type': 'token',
            'redirect_uri': get_redirect_uri(self.request)
        })
        return f'{authorize_uri}?{data}'


def generate_token():
    return binascii.hexlify(os.urandom(20)).decode()


class AuthorizeView(RedirectView):
    """用户授权"""

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(AuthorizeView, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, authorize_type, *args, **kwargs):
        request = self.request
        user = request.user
        token = None
        if authorize_type == 'account':
            if user.is_authenticated:
                token = generate_token()
                token_user_cache_key = f'oauth:token:{token}:user:id'
                user_token_cache_key = f'oauth:user:id:{user.id}:token'
                cache.set(token_user_cache_key, user.id, timeout=60 * 60 * 24)
                cache.set(user_token_cache_key, token, timeout=None)
        if token:
            data = parse.urlencode({
                'access_token': token,
                'token_type': 'bearer'
            })
            return f'{get_redirect_uri(request)}#{data}'
        return reverse('login', request=request)
