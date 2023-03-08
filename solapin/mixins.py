from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages


class IsSuperuserMixing(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')
    
class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        # print('Permiso requerido para módulo: {}'.format(self.permission_required))
        if isinstance(self.permission_required, str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms  

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('login')
        return self.url_redirect
    
    def dispatch(self, request, *args, **kwargs):
        # print('Permisos del usuario: {}'.format(request.user.get_user_permissions()))
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.ERROR, 'No tiene acceso a este módulo.')
        return redirect(self.get_url_redirect())