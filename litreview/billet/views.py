from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Critic, Billet
from .forms import TicketForm, CriticForm, BilletForm

def create_ticket(request):
    if request.method == "POST":
        print(request.POST)
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('billet:list_tickets')
        else:
            print(form.errors)
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

def create_critic(request, ticket_id=None):
    ticket = get_object_or_404(Ticket, id=ticket_id) if ticket_id else None
    if request.method == "POST":
        form = CriticForm(request.POST)
        if form.is_valid():
            critic = form.save(commit=False)
            critic.user = request.user
            critic.ticket = ticket
            critic.save()
            return redirect('billet:list_tickets')
        else:
            print("Erreurs dans le formulaire :", form.errors)
    else:
        form = CriticForm()
    return render(request, 'critics/create_critic.html', {'form': form, 'ticket': ticket})

def create_billet(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        critic_form = CriticForm(request.POST)
        
        if ticket_form.is_valid() and critic_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user  # Associer l'utilisateur actuel
            ticket.save()

            critic = critic_form.save(commit=False)
            critic.user = request.user
            critic.ticket = ticket  # Associer le ticket à la critique
            critic.save()

            billet = Billet.objects.create(user=request.user, ticket=ticket, critic=critic)
            billet.save()

            return redirect('billet:list_billets')  # Rediriger après la création
    else:
        ticket_form = TicketForm()
        critic_form = CriticForm()

    return render(request, 'billets/create_billet.html', {
        'ticket_form': ticket_form,
        'critic_form': critic_form
    })


def list_tickets(request):
    tickets = Ticket.objects.all().order_by('-date_creation')  # Affiche les tickets du plus récent au plus ancien
    critics = Critic.objects.all()
    
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets, 'critics': critics})

def list_critics(request):
    critics = Critic.objects.all().order_by('-date_creation')
    return render(request, 'critics/list_critics.html', {'critics': critics})

def list_billets(request):
    billets = Billet.objects.all()
    return render(request, 'billets/list_billets.html', {'billets': billets})

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.user == ticket.user:
        ticket.delete()

    return redirect('billet:list_tickets')