from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Art, Category
from .forms import CommentForm


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
                messages.error(request, "Sorry,the are no art works for sale right now. Please comeback later!")

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


def art_detail(request, id):
    """
    renders a detailed display of a single art image
    """

    details = get_object_or_404(Art, pk=id)
    comments = details.comments.order_by('created_on')
    liked = False
    if details.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'details': details,
        "comments": comments,
        "liked": liked,
    }

    return render(request, 'art/details.html', context)


def like_item(request, id):
    """Adds and removes likes on an art piece(details)"""
    details = get_object_or_404(Art, pk=id)

    if details.likes.filter(id=request.user.id).exists():
        details.likes.remove(request.user.id)
    else:
        details.likes.add(request.user.id)

    return HttpResponseRedirect(reverse('details', args=[id]))


def comment_on_art(request, id):
    """Handles users adding comments to item"""
    details = get_object_or_404(Art, pk=id)
    comments = details.comments.order_by('created_on')
    user_comment = CommentForm(data=request.POST)
    if user_comments.is_valid():
        user_comments.instance.email = request.user.email
        user_comments.instance.name = request.user.username
        user_comments.instance.email = request.user.email
        comment = user_comments.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(request, "You have successfully commented")
    else:
        messages.error(request, "Something went wrong,try again!")
        user_comments = CommentForm()

    context = {
        'details': details,
        'comments': comments,
        'user_comment': CommentForm()
    }

    return render(request, context, 'art/details.html')
