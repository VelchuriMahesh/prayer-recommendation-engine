import pandas as pd
import random

# Load the CSV
df = pd.read_csv("bible.csv")

def get_recommended_verse(feeling):
    # Ensure the emotion column is treated as string
    df['emotion'] = df['emotion'].astype(str)

    # Filter verses that match the given emotion
    matches = df[df['emotion'].str.contains(feeling, case=False, na=False)]

    if not matches.empty:
        verse = matches.sample(1).iloc[0]
        return f"{verse['verse_text']} - {verse['reference']} ({verse['version']})"
    else:
        return "Sorry, no verse found for that emotion."
