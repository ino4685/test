from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.urls import reverse_lazy


class TopView(TemplateView):
    template_name = "fixed/top.html"

class FirstView(TemplateView):
    template_name = "fixed/first.html"

class ContactView(FormView):
    template_name = "fixed/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact-send')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class ContactsendView(TemplateView):
    template_name = "fixed/contactsend.html"

class NeologismView(TemplateView):
    template_name = "fixed/neologism.html"
    
class SiteView(TemplateView):
    template_name = "fixed/site.html"
    
class SearchView(TemplateView):
    template_name = "fixed/search.html"

class PrivacypolicyView(TemplateView):
    template_name = "fixed/privacypolicy.html"

