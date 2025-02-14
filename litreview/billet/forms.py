from django import forms
from .models import Ticket, Critic

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

class CriticForm(forms.ModelForm):
    class Meta:
        model = Critic
        fields = ['title', 'note', 'comment']

class BilletForm(forms.ModelForm):
    ticket = TicketForm()
    critic = CriticForm()

    class Meta:
        model = Critic  
        fields = ['title', 'note', 'comment']  

    def save(self, user):
        # Create a Ticket
        ticket = Ticket.objects.create(
            user=user,
            title=self.cleaned_data['title'],
            description=self.cleaned_data['comment']
        )
        critic = Critic.objects.create(
            user=user,
            ticket=ticket,
            title=self.cleaned_data['title'],
            note=self.cleaned_data['note'],
            comment=self.cleaned_data['comment']
        )
        return critic  
