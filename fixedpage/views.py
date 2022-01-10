from django.views.generic import TemplateView


class TopView(TemplateView):
    template_name = "top.html"

class FirstView(TemplateView):
    template_name = "first.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class NeologismView(TemplateView):
    template_name = "neologism.html"

