import pandas as pd

# Load the Bible CSV
df = pd.read_csv("bible.csv")

# Define keyword-based emotion tags
emotion_keywords = {
    "joy": ["rejoice", "joy", "glad", "delight"],
    "sadness": ["sorrow", "weep", "cry", "brokenhearted"],
    "fear": ["afraid", "fear", "terrified", "dread"],
    "hope": ["hope", "promises", "future", "trust"],
    "love": ["love", "loving", "compassion", "kindness"],
    "anger": ["anger", "wrath", "furious", "rage"],
    "peace": ["peace", "calm", "still", "quiet"],
    "faith": ["faith", "believe", "trust", "confidence"],
    "strength": ["strength", "strong", "mighty", "power"],
    "comfort": ["comfort", "heal", "rest", "soothe"]
}

# Function to assign tags
def tag_verse(text):
    tags = []
    text_lower = text.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(word in text_lower for word in keywords):
            tags.append(emotion)
    return ",".join(tags)

# Apply the tagging function
df["tags"] = df["text"].apply(tag_verse)

# Save updated file
df.to_csv("bible.csv", index=False)
print("✅ Emotion tags added and saved to bible.csv")
