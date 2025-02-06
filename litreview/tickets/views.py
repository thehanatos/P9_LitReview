from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm

@login_required
def create_ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)  # Gérer les fichiers uploadés
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associer l'utilisateur connecté
            ticket.save()
            return redirect("tickets:ticket_list")  # Redirection après création
    else:
        form = TicketForm()

    return render(request, "tickets/create_ticket.html", {"form": form})

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by("-created_at")  # Tri par date
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})
