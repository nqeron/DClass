from django.views.generic import TemplateView

class LoginSuccessPage(TemplateView):
    template_name = 'login_success.html'

class LeavePage(TemplateView):
    template_name = 'leave.html'

class HomePage(TemplateView):
    template_name = 'index.html'
