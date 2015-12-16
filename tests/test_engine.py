from powerball_backend.engine import Engine


def test_sum(mock):
    mock_random = mock.patch('powerball_backend.engine.random')
    mock_random.choice.return_value = "A"

    assert Engine().generate_ticket() == {
        'ticket_code': 'AAAAAAAAAAAAAAAA', 'prize_code': 'AAAA'
    }
