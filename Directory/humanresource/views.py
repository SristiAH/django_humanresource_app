from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Staff

class StaffListView(ListView):
    model = Staff
    template_name = "staff_list.html"  
    context_object_name = "staff_members"  
    
class StaffDetailView(DetailView):
    model = Staff
    template_name = "staff_detail.html" 
    context_object_name = "staff" 

class StaffCreateView(CreateView):
    model = Staff
    template_name = "staff_form.html" 
    fields = ['FirstName', 'MiddleName', 'LastName', 'EmailID', 'ContactNo', 'Department']
    success_url = reverse_lazy('staff_list')  

    def form_valid(self, form):
        return super().form_valid(form)
    
class StaffUpdateView(UpdateView):
    model = Staff
    template_name = "staff_form.html" 
    fields = ['FirstName', 'MiddleName', 'LastName', 'EmailID', 'ContactNo', 'Department']
    success_url = reverse_lazy('staff_list')  

    def form_valid(self, form):
        # Additional custom validation if needed
        return super().form_valid(form)
    
class StaffDeleteView(DeleteView):
    model = Staff
    template_name = "staff_confirm_delete.html"  
    success_url = reverse_lazy('staff_list')

