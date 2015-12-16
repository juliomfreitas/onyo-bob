from rest_framework import serializers
from powerball_backend.engine import Engine
from powerball_backend.models import Ticket, Prize


class TicketSerializer(serializers.Serializer):
    draw_date = serializers.DateField()
    ticket = serializers.JSONField()

    prize_code = serializers.CharField(read_only=True)
    ticket_code = serializers.CharField(read_only=True)

    def save(self):
        tkt = Engine().generate_ticket()

        prize = Prize(
            draw_date=self.validated_data["draw_date"],
            code=tkt['prize_code']
        )
        prize.save()

        ticket = Ticket(
            prize=prize,
            code=tkt['ticket_code'],
            numbers=self.validated_data["ticket"],
            winning=None
        )
        ticket.save()

        self.validated_data['prize_code'] = tkt['prize_code']
        self.validated_data['ticket_code'] = tkt['ticket_code']
