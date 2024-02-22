from django.shortcuts import render, get_object_or_404, redirect
from forum import models
from forum.forms import TopicForm, CommentForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    topics = models.Topic.objects.all()

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            
            new_topic = form.save(commit=False)
            # Assign current user
            new_topic.auther = request.user
            new_topic.save()
            # messages.success(request, 'Topic added succesfully')
            # Redirect to new created item detail view
            return redirect(new_topic.get_absolute_url())
    else:
        form = TopicForm()

    context = {'topics':topics, 'form':form}
    return render(request, 'forum/index.html', context)

def detail(request, id, slug):
    topic = get_object_or_404(models.Topic, id=id, slug=slug)
    comments = topic.comments.all()
    # Form for users to comment
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic
            comment.auther = request.user
            comment.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CommentForm()
    
    return render(request, 'forum/detail.html', {'topic':topic, 'comments': comments, 'form': form})

def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.auther = request.user
            form.save()
            return redirect(form.get_absolute_url())
    else:
        form = TopicForm()
    
    return render(request, 'forum/create_topic.html', {'form':form})

@require_POST
def post_comment(request, topic_id):
    topic = get_object_or_404(models.Topic, id = topic_id)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # comment = form.save(commit=False)
        # comment.topic = topic
        # comment.auther = request.user
        # comment.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'forum/comment.html', {'topic':topic, 'form':form, 'comment':comment})