# This is a compoent that will randomly select a phobia from a list of 50 phobias.

import random

randPhobia = random.randint(0, 29)

phobias = ["Fear of the Dark", "Fear of Heights", "Fear of Spiders", "Fear of Snakes", "Fear of Clowns", "Fear of Flying", "Fear of Public Speaking", "Fear of Death", "Fear of Being Alone", "Fear of Failure", "Fear of Commitment", "Fear of Intimacy", "Fear of Rejection", "Fear of Change", "Fear of Losing Control", "Fear of the Unknown", "Fear of Being Judged", "Fear of Being Hurt", "Fear of Being Embarrassed", "Fear of Being Insulted",
           "Fear of Being Neglected", "Fear of Being Ridiculed", "Fear of Being Wrong", "Fear of Being Ignored", "Fear of Being Abandoned", "Fear of Being Disappointed", "Fear of Being Inferior", "Fear of Being Insulted", "Fear of Being Inadequate", "Fear of Being Incompetent", "Fear of Being Ineffective", "Fear of Being Inefficient", "Fear of Being Inept", "Fear of Being Inept", "Fear of Being Inept", "Fear of Being Inept", "Fear of Being Inept"]

phobia = phobias[randPhobia]

def GetPhobia():
    print("Your phobia is: " + phobias[randPhobia] + ".")

__all__ = ["GetPhobia"]