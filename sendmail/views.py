from django.shortcuts import render
from sendmail.models import MailPost
from sendmail.forms import MailPostForm


from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


class MailPostCreate(CreateView):
    model = MailPost
    form_class = MailPostForm
    template_name = 'edit.html'

    def get_success_url(self):
        return reverse_lazy("sendmail:list")

class MailPostRead(ListView):
    model = MailPost
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        object_list = MailPost.objects.all().order_by('-created_date')[:10]
        return {"object_list": object_list}