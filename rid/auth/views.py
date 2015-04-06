from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView


class PasswordChangeView(FormView):
    template_name = 'auth/settings/change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('change_password')

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your password has been changed.")
        return super(FormView, self).form_valid(form)
