from django.http import HttpResponse
from django.shortcuts import render
from .models import Story
from django.contrib.auth.decorators import login_required
from .import model_forms
from django.shortcuts import redirect

# Create your views here.

def story_list(request):
    stories = Story.objects.all().order_by('date');
    return render(request,'stories/story_list.html',{'stories':stories})

def story_detail(request, slug):
    story = Story.objects.get(slug=slug)
    return render(request,'stories/story_detail.html',{'story':story})

@login_required(login_url="/accounts/login/")
def story_new(request):
    if request.method == 'POST':
        form = model_forms.NewStory(request.POST,request.FILES)
        if form.is_valid():
            writing = form.save(commit=False)
            writing.writer = request.user
            writing.save()
            return redirect('stories:list')
    else:
        form = model_forms.NewStory()
        return(render(request,'stories/story_new.html',{'form':form}))
