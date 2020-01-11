from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Manager,Employee
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import xlsxwriter




@login_required
def download(request):
    pk=request.user.pk
    path=os.path.join(settings.MEDIA_ROOT,"feedback.xlsx")
    ls = Employee.objects.filter(manager__pk=1).order_by('pk')
    workbook = xlsxwriter.Workbook(path)
    worksheet = workbook.add_worksheet()
    array=[["Manager_name","Date_posted","Comment"]]
    [array.append(x.json()) for x in ls]
    row = 0
    col=0
    for row,data in enumerate(array):
        worksheet.write_row(row, col, data)
    print(array)
    workbook.close()
    print(path)
    file_path = path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


class CommentCreateView(SuccessMessageMixin,CreateView):
    fields = ('manager','comment')
    model=Employee
    template_name='comment_form.html'
    success_message = "Feedback submitted successfully"


class CommentListView(LoginRequiredMixin,ListView):
    context_object_name = 'comments'
    model = Employee
    template_name = 'comments.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        pk = self.request.user.pk
        context = super().get_context_data(**kwargs)
        context['comments']=context['comments'].filter(manager__pk=1)
        print(context)
        return context