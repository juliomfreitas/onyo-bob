from rest_framework import serializers
from powerball_backend.engine import Engine
from powerball_backend.models import Ticket, Prize
from django.http import Http404


class TicketSerializer(serializers.Serializer):
    draw_date = serializers.DateField()
    ticket = serializers.JSONField()

    prize_code = serializers.CharField(read_only=True)
    ticket_code = serializers.CharField(read_only=True)

    def winner(self):
        ticket = Ticket.objects.filter(
            prize__draw_date=self.validated_data["draw_date"],
            numbers=self.validated_data["ticket"]
        )
        if not ticket:
            raise Http404()

        # not hadling duplicate ones
        ticket = ticket[len(ticket) - 1]

        if ticket.drawed():
            return ticket.winning
        else:
            return False

    def save(self):
        tkt = Engine().generate_ticket()

        prize, created = Prize.objects.get_or_create(
            draw_date=self.validated_data["draw_date"],
        )
        if created:
            prize.code = tkt['prize_code']
            prize.save()

        ticket = Ticket(
            prize=prize,
            code=tkt['ticket_code'],
            numbers=self.validated_data["ticket"],
            winning=None
        )
        ticket.save()

        self.validated_data['prize_code'] = prize.code
        self.validated_data['ticket_code'] = ticket.code
