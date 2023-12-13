from django.shortcuts import render, get_object_or_404
from main.models import Student
from django.views.generic import ListView, DetailView



class StudentListView(ListView):
    model = Student
    template_name = 'main/material_list.html'



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)

class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'


