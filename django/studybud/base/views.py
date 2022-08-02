from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Questions

# Create your views here.
rooms = [
    {'id': 1, 'name':'lets learn python'},
    {'id': 2, 'name':'lets learn python'},
    {'id': 3, 'name':'lets learn python'},
]
def home(request):
    context = {'rooms':rooms}
    #return HttpResponse('HOme Page')
    return render(request, 'home.html',context)
def about(request):
    context={'ip_address': request.META['REMOTE_ADDR']}
    #return HttpResponse('About')
    return render(request, 'about.html', context)

def studentindex(request):
    # Generate counts of some of the main objects
    all_students =Student.objects.all()
    num_students =Student.objects.all().count()
    num_questions =Questions.objects.all().count()
    context = {
        'all_students': all_students,
        'num_students': num_students,
        'num_questions': num_questions,
    }
    return render(request, 'students.html', context)
