from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subscription
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def subscriptions_view(request):
    query = request.GET.get('q', '')

    # Search users
    users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)

    # List of followers
    followers = Subscription.objects.filter(followed=request.user).select_related('follower')

    # List of subscriptions 
    following = Subscription.objects.filter(follower=request.user).select_related('followed')

    # Crate a list of Ids of followed users
    following_user_ids = set(following.values_list('followed__id', flat=True))

    return render(request, 'subscriptions/subscriptions.html', {
        'users': users,
        'query': query,
        'followers': followers,
        'following': following,
        'following_user_ids': following_user_ids,  
    })

@login_required
def follow_user(request, user_id):
    followed = get_object_or_404(User, id=user_id)
    if request.user != followed:
        Subscription.objects.get_or_create(follower=request.user, followed=followed)
    return redirect('subscriptions:subscriptions_view')

@login_required
def unfollow_user(request, user_id):
    followed = get_object_or_404(User, id=user_id)
    Subscription.objects.filter(follower=request.user, followed=followed).delete()
    return redirect('subscriptions:subscriptions_view')
