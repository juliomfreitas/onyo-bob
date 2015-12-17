from powerball_backend.serializers import TicketSerializer
from datetime import date


def test_exists_prize(mock):
    mockengine = mock.patch('powerball_backend.serializers.Engine')
    mockticket = mock.patch('powerball_backend.serializers.Ticket')
    mockticket.return_value.code = "AAAAAAAAAAAAAAAA"

    prize = mock.Mock()
    prize.code = "OLD_EXISTING_CODE"
    mockprize = mock.patch('powerball_backend.serializers.Prize')
    mockprize.objects.get_or_create.return_value = prize, False

    mockengine.return_value.generate_ticket.return_value = {
        'ticket_code': 'AAAAAAAAAAAAAAAA', 'prize_code': 'NEW_GENERATED_CODE'
    }

    t = TicketSerializer(
        data={"draw_date": "2016-10-10", "ticket": "[1,2,3,4,5,9]", }
    )

    assert t.is_valid()
    t.save()

    assert t.validated_data == {
        'ticket_code': 'AAAAAAAAAAAAAAAA', 'prize_code': 'OLD_EXISTING_CODE',
        "draw_date": date(2016, 10, 10), "ticket": '[1,2,3,4,5,9]'
    }


def test_not_exists_prize(mock):
    mockengine = mock.patch('powerball_backend.serializers.Engine')
    mockticket = mock.patch('powerball_backend.serializers.Ticket')
    mockticket.return_value.code = "AAAAAAAAAAAAAAAA"

    prize = mock.Mock()
    mockprize = mock.patch('powerball_backend.serializers.Prize')
    mockprize.objects.get_or_create.return_value = prize, True

    mockengine.return_value.generate_ticket.return_value = {
        'ticket_code': 'AAAAAAAAAAAAAAAA', 'prize_code': 'NEW_GENERATED_CODE'
    }

    t = TicketSerializer(
        data={"draw_date": "2016-10-10", "ticket": "[1,2,3,4,5,9]", }
    )

    assert t.is_valid()
    t.save()

    assert t.validated_data == {
        'ticket_code': 'AAAAAAAAAAAAAAAA', 'prize_code': 'NEW_GENERATED_CODE',
        "draw_date": date(2016, 10, 10), "ticket": '[1,2,3,4,5,9]'
    }
