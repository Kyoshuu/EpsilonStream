from django.shortcuts import render
from django.utils import timezone
from .models import *
def post_list(request):
	comments = Comment.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'Comment/post_list.html', {})

def utwor_list(request):
    utwory = Utwor.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'Comment/post_list.html', {'utwory': utwory})
# Create your views here.