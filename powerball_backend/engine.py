"""
The powerball drawing engine
"""
import string
import random


class Engine:

    def create_ticket(self):
        randcode = lambda N: ''.join(
            random.choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(N)
        )

        return {
            'prize_code': randcode(4),
            'ticket_code': randcode(16)
        }
