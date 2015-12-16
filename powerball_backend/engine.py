"""
The powerball drawing engine
"""
import string
import random


class Engine:

    def generate_ticket(self):
        # randomize between ascii uppercase letters and digits
        # The parameter is the string length of the code returned
        randcode = lambda N: ''.join(
            random.choice(
                string.ascii_uppercase + string.digits
            ) for _ in range(N)
        )

        return {
            'prize_code': randcode(4),
            'ticket_code': randcode(16)
        }
