from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from experiences.models import Post

# Create your views here.
def experience(request):
    experiences = Post.objects.all().order_by('-created_at')
    return render(request, "experience.html", {"experiences" : experiences})

def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostModelForm()
    return render(request, 'form_create.html', {'form': form})

def experience_detail(request, post_id):
    experience = get_object_or_404(Post, pk=post_id)
    return render(request, "experience_detail.html", {"experience" : experience})

def experience_update(request, id):
    experience = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('experiences')
    else:   #GET이면
        form = PostModelForm(instance=experience)
        return render(request, 'form_create.html', {'form':form, 'id':id})
    
def experience_delete(request, id):
    experience = Post.objects.get(pk=id)
    experience.delete()
    return redirect('experiences')