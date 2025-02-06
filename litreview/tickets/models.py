from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="ticket_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.book_title} by {self.user.username}"
