from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # Retrieve the custom user

class Subscription(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followed')  # Prevent duplicate

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"