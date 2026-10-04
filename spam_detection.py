import re

spam_keywords = [
    "win", "winner", "prize", "cash", "free",
    "offer", "click", "urgent", "congratulations",
    "lottery", "claim", "reward"
]

def detect_spam(message):
    message = message.lower()

    score = 0

    for word in spam_keywords:
        if re.search(r"\b" + word + r"\b", message):
            score += 1

    if score >= 2:
        return "SPAM"
    else:
        return "NOT SPAM"


print("=" * 50)
print("          SPAM MESSAGE DETECTOR")
print("=" * 50)

message = input("\nEnter a message: ")

result = detect_spam(message)

print("\nMessage:", message)
print("Result:", result)