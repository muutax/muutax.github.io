from django.shortcuts import render, redirect
from .models import Records
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import RecordForm, AuthUserForm, RegisterUserForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class WorkListView(ListView):
    model = Records
    template_name = 'index.html'
    context_object_name = 'list_records'

class WorkDetailView(DetailView):
    model = Records
    template_name = 'detail.html'
    context_object_name = 'get_record'

class RecordCreateView(CreateView):
    model = Records
    template_name = 'edit_page.html'
    form_class = RecordForm
    success_url = reverse_lazy('edit_page')
    def get_context_data(self, **kwargs):
        kwargs['list_records'] = Records.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

class RecordUpdateView(UpdateView):
    model = Records
    template_name = 'edit_page.html'
    form_class = RecordForm
    success_url = reverse_lazy('edit_page')
    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

#class RecordDeleteView(DeleteView):
#    model = Records
#    template_name = 'edit_page.html'
#    success_url = reverse_lazy('edit_page')

def delete_page(request, pk):
    get_record = Records.objects.get(pk=pk)
    get_record.delete()
    return redirect(reverse('edit_page'))

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')
    def get_success_url(self):
        return self.success_url

class Logout(LogoutView):
    next_page = reverse_lazy('edit_page')

#class RegisterUserView(CreateView):
#    model = User
#    template_name = 'register_page.html'
#    form_class = RegisterUserForm
#    success_url = reverse_lazy('edit_page')
#    success_msg = 'Пользователь успешно создан'
#    def form_valid(self,form):
#        form_valid = super().form_valid(form)
#        username = form.cleaned_data["username"]
#        password = form.cleaned_data["password"]
#        aut_user = authenticate(username=username,password=password)
#        login(self.request, aut_user)
#        return form_valid

#def update_page(request, pk):
#    get_record = Records.objects.get(pk=pk)
#    if request.method == 'POST':
#        form = RecordForm(request.POST,instance = get_record)
#        if form.is_valid():
#            form.save()
#    template = 'edit_page.html'
#    context = {
#        'get_record':get_record,
#        'update':True,
#        'form':RecordForm(instance = get_record),
#    }
#    return render(request, template, context)

#def delete_page(request, pk):
#    get_record = Records.objects.get(pk=pk)
#    get_record.delete()
#    return redirect(reverse('edit_page'))

#def detail_page(request, id):
#    get_record = Records.objects.get(id=id)
#    context = {
#        'detail_page':detail_page,
#        'get_record':get_record
#    }
#    template = 'detail.html'
#    return render(request, template, context)

#def home(request):
#    list_records = Records.objects.all()
#    context = {
#        'list_records':list_records
#    }
#    template = 'index.html'
#    return render(request, template, context)

#def edit_page(request):
#    success = False
#    if request.method == 'POST':
#        form = RecordForm(request.POST)
#        if form.is_valid():
#            form.save()
#            success = True
#    template = 'edit_page.html'
#    context = {
#       'list_records':Records.objects.all().order_by('-id'),
#        'form':RecordForm(),
#        'success':success
#    }
#    return render(request, template, context)