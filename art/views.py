from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Art, Category, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


def art_display(request):
    """
    render a display of all the art
    """
    art = None
    query = None
    category = None
    is_available = None

    if request.GET:
        if 'is_available' in request.GET:
            is_available = request.GET['is_available']
            art = Art.objects.filter(is_available=is_available)
            if not art:
                messages.error(
                    request, "Sorry,the are no art works for sale right"
                    "now. Please comeback later!")

    if request.GET:
        if 'category' in request.GET:
            category = request.GET['category']
            art = Art.objects.filter(category=category)

    if request.GET:
        if 'art-search' in request.GET:
            query = request.GET['art-search']
            queries = Q(title__icontains=query)
            art = Art.objects.filter(queries)
            if not art:
                messages.error(request, "not found")
                return redirect(reverse('art'))

    context = {
        'art': art,
        'category': category,
        'search_term': query
    }

    return render(request, 'art/art.html', context)


def art_detail(request, id, *args, **kwargs):
    """
    renders a detailed display of a single art image
    """
    queryset = Art.objects
    details = get_object_or_404(queryset, pk=id)
    comments = details.art_commented_on.order_by('created_on')
    liked = False
    if details.likes.filter(id=request.user.id).exists():
        liked = True

    user_comments = CommentForm(data=request.POST)

    if request.method == 'POST':
        if user_comments.is_valid():
            user_comments.instance.art = Art.objects.get(id=id)
            user_comments.instance.user = request.user
            user_comments.save()
            messages.success(request, "You have successfully commented")
        else:
            messages.error(request, "Something went wrong,try again!")
            user_comments = CommentForm()

    context = {
        'details': details,
        "comments": comments,
        "liked": liked,
        'user_comments': CommentForm()
    }

    return render(request, 'art/details.html', context)


@login_required
def like_item(request, id):
    """Adds and removes likes on an art piece(details)"""
    details = get_object_or_404(Art, pk=id)

    if details.likes.filter(id=request.user.id).exists():
        details.likes.remove(request.user.id)
    else:
        details.likes.add(request.user.id)

    return HttpResponseRedirect(reverse('details', args=[id]))


def delete_comment(request, comment_id,):
    """ this deletes comments and
    redirects the the redirect need to be fixed"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, "You have successfully deleted comment")
    return redirect(reverse('details', args=[comment.art.id]))


def edit_comment(request, comment_id,):
    """
    this is handles the edit button. it gets the comment id from django.
    the redirect path need to be fixed to redirect back to the art details
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        user_comments = CommentForm(request.POST, instance=comment)
        if user_comments.is_valid():
            user_comments.save()
            messages.success(request, "You have successfully updated comment")
            return redirect(reverse('details', args=[comment.art.id]))
        else:
            messages.error(request, "Something went wrong,try again!")
    else:
        CommentForm()
    art = comment.art
    user_comments = CommentForm(instance=comment)
    context = {
        "user_comments": user_comments,
        'art': art,
        'comment': comment,
    }

    template = 'art/edit_comment.html'

    return render(request, template, context)
