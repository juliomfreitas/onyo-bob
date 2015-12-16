from powerball_backend.serializers import TicketSerializer
from powerball_backend.models import Ticket
from rest_framework import mixins
from rest_framework import generics


class CreateTicketView(mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
