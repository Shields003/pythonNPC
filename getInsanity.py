# This is a compoent that will randomly select an insanity from a list of 50 insanities.

import random

randInsanity = random.randint(0, 19)

insanities = ["Schitsaphrenia", "Schizoaffective Disorder", "Schizotypal Personality Disorder", "Delusional Disorder", "Bipolar Disorder", "Depression", "Anxiety", "Obsessive Compulsive Disorder", "Post Traumatic Stress Disorder", "Dissociative Identity Disorder", "Dissociative Amnesia", "Dissociative Fugue", "Dissociative Disorder", "Somatoform Disorder", "Conversion Disorder", "Hypochondriasis", "Body Dysmorphic Disorder", "Factitious Disorder", "Munchausen Syndrome", "Munchausen Syndrome by Proxy"]

insanity = insanities[randInsanity]

def GetInsanity():
    print("Your Insanity is:" + insanities[randInsanity] + ".")

__all__ = ["GetInsanity"]