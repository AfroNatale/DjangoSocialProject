from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class AfterLogoutPage(TemplateView):
    template_name = 'after_logout.html'

class AfterLoginPage(TemplateView):
    template_name = 'after_login.html'
