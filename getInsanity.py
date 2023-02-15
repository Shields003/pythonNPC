# This is a compoent that will randomly select an insanity from a list of 50 insanities.

import random

randInsanity = random.randint(0, 49)

insanities = ["Antisocial Personality Disorder (Psychopathy)", "Borderline Personality Disorder", "Narcissistic Personality Disorder", "Schizophrenia", "Bipolar Disorder", "Major Depressive Disorder", "Obsessive-Compulsive Disorder (OCD)", "Post-Traumatic Stress Disorder (PTSD)", "Generalized Anxiety Disorder (GAD)", "Attention Deficit Hyperactivity Disorder (ADHD)", "Panic Disorder", "Dissociative Identity Disorder (DID)", "Anorexia Nervosa", "Bulimia Nervosa", "Schizoid Personality Disorder", "Paranoid Personality Disorder", "Histrionic Personality Disorder", "Avoidant Personality Disorder", "Dependent Personality Disorder", "Obsessive-Compulsive Personality Disorder (OCPD)", "Depression", "Social Anxiety Disorder", "Agoraphobia", "Specific Phobias", "Substance Use Disorders (Drug Addiction)", "Gambling Addiction", "Internet Addiction", "Pyromania (Fire-Starting)", "Kleptomania (Stealing)", "Trichotillomania (Hair Pulling)", "Dermatillomania (Skin Picking)", "Body Dysmorphic Disorder", "Tourette's Syndrome", "Asperger's Syndrome", "Autism Spectrum Disorder", "Ankylosing Spondylitis", "Fibromyalgia", "Multiple Sclerosis", "Huntington's Disease", "Alzheimer's Disease", "Parkinson's Disease", "Schizophreniform Disorder", "Delusional Disorder", "Psychotic Disorder Not Otherwise Specified (NOS)", "Somatic Symptom Disorder", "Conversion Disorder", "Factitious Disorder", "Munchausen Syndrome", "Munchausen Syndrome by Proxy", "Substance-Induced Psychotic Disorder"]



insanity = insanities[randInsanity]

def GetInsanity():
    print("Your Insanity is:" + insanities[randInsanity] + ".")

__all__ = ["GetInsanity"]