from powerball_backend.serializers import TicketSerializer
from datetime import date


def test_serializing(mock):
    mockengine = mock.patch('powerball_backend.serializers.Engine')
    mock.patch('powerball_backend.serializers.Ticket')
    mock.patch('powerball_backend.serializers.Prize')

    mockengine.return_value.generate_ticket.return_value = {
        'ticket_code': 'AAAAAAAAAAAAAAAA', 'prize_code': 'AAAA'
    }

    t = TicketSerializer(
        data={"draw_date": "2016-10-10", "ticket": "[1,2,3,4,5,9]", }
    )

    assert t.is_valid()
    t.save()

    assert t.validated_data == {
        'ticket_code': 'AAAAAAAAAAAAAAAA', 'prize_code': 'AAAA',
        "draw_date": date(2016, 10, 10), "ticket": '[1,2,3,4,5,9]'
    }
