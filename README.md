Step I: Setting Up the Development Environment

For Windows, download Python from Python.org website.
Verify whether it is installed by typing in the command prompt:
```bash
	python --version
```
To create Python virtual environment, type the command:
```bash
	python -m venv myenv
```
Command to activate the virtual environment:
```bash
	.\myenv\Scripts\activate
```

Step II: Installing Django

	 Upgrade pip
		python -m pip install --upgrade pip

	 Installing Django with pip
		pip install Django

	 Checking Django installation
		python –m django –-version
			5.1.2

Step III: Inside the command prompt, type the following:
		Django-admin startproject Directory

Step IV: Download and install MySQL Workbench

Step V: Inside the command prompt, type the following command to install the Python MySQL driver
		pip install mysqlclient

Step VI: Configure MySQL workbench and create a database using the workbench by typing the following command:
		create database mydb;
	 
	 Update DATABASES setting inside settings.py file

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Step VII: Applying initial database migrations
	  
	  After navigating to the project's root directory, run the following inside command prompt :

		python manage.py migrate

Step VIII: Run the following command:
		python manage.py startapp humanresource  

Step IX: Creating the application entry in settings.py

	 Add the application configuration entry in INSTALLED_APPS.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'humanresource',
]

Step X: Inside models.py

from django.db import models

# Create your models here.
class Department(models.Model):
    ID = models.AutoField(primary_key=True)  
    DepartmentName = models.CharField(max_length=50, null=False)  
    IsActive = models.BooleanField(max_length=1, null=False, default=True)  

    def __str__(self):
        return self.DepartmentName

class Staff(models.Model): 
    FirstName = models.CharField(max_length=50, null=False)  
    MiddleName = models.CharField(max_length=50, null=True)  
    LastName = models.CharField(max_length=50, null=False)  
    EmailID = models.EmailField(max_length=50, null=False)  
    ContactNo = models.CharField(max_length=10, null=False)  
    Department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        null=False
    )  

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"


Step XI: Creating the migration file:
		python manage.py makemigrations humanresource
Step XII: Apply database changes
		python manage.py migrate

Step XIII: Inside views.py

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
        return super().form_valid(form)
    
class StaffDeleteView(DeleteView):
    model = Staff
    template_name = "staff_confirm_delete.html"  
    success_url = reverse_lazy('staff_list')


Step XIV: Create a file urls.py inside the humanresource application and write the below code:

from django.urls import path
from django.views.generic import TemplateView
from .views import StaffListView, StaffDetailView, StaffCreateView, StaffUpdateView, StaffDeleteView
urlpatterns = [
    path('staff/', StaffListView.as_view(), name='staff_list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staff/create/', StaffCreateView.as_view(), name='staff_create'),
    path('staff/<int:pk>/update/', StaffUpdateView.as_view(), name='staff_update'),
    path('staff/<int:pk>/delete/', StaffDeleteView.as_view(), name='staff_delete'),
]

Step XV: Update urls.py in the Project Directory

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('humanresource.urls')),  
]

Step XVI: Create HTML templates for each of the views inside a templates directory inside the humanresource app. 

	  staff_list.html
	  staff_detail.html
	  staff_form.html
	  staff_confirm_delete.html

Inside staff_list.html

<h1>Staff Members</h1>
<ul>
    {% for staff in staff_members %}
        <li>
            <a href="{% url 'staff_detail' staff.id %}">{{ staff.FirstName }} {{ staff.LastName }}</a>
        </li>
    {% endfor %}
</ul>
<a href="{% url 'staff_create' %}">Add New Staff Member</a>

Inside staff_detail.html

<h1>{{ staff.FirstName }} {{ staff.LastName }}</h1>
<p>Email: {{ staff.EmailID }}</p>
<p>Contact: {{ staff.ContactNo }}</p>
<p>Department: {{ staff.Department.DepartmentName }}</p>
<a href="{% url 'staff_update' staff.id %}">Edit</a>
<a href="{% url 'staff_delete' staff.id %}">Delete</a>
<a href="{% url 'staff_list' %}">Back to List</a>

Inside staff_form.html

{% if view.object %}
    <h1>Update Staff</h1>
{% else %}
    <h1>Create Staff</h1>
{% endif %}
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save</button>
</form>
<a href="{% url 'staff_list' %}">Cancel</a>


Inside staff_confirm_delete.html

<h1>Confirm Delete</h1>
<p>Are you sure you want to delete {{ object.FirstName }} {{ object.LastName }}?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Yes, delete</button>
</form>
<a href="{% url 'staff_list' %}">Cancel</a>


Step XVII: Adding Department names
Inside command prompt
	python manage.py shell

from humanresource.models import Department
Department.objects.create(DepartmentName="HR")
Department.objects.create(DepartmentName="IT")
Department.objects.create(DepartmentName="Finance")

Step XVIII: Run the Development Server

python manage.py runserver

http://127.0.0.1:8000/staff/ to access the application.
