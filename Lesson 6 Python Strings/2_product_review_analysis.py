
# Product Review Analysis

# Task 1: Keyword Highlighter
def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        for keyword in keywords:
            if keyword in review.lower():
                review = review.replace(keyword, keyword.upper())
        print(review)

# Task 2: Sentiment Tally
def sentiment_tally(reviews, positive_words, negative_words):
    for review in reviews:
        positive_count = sum(word in review.lower() for word in positive_words)
        negative_count = sum(word in review.lower() for word in negative_words)
        print(f"Positive: {positive_count}, Negative: {negative_count}")

# Task 3: Review Summary
def create_review_summary(reviews):
    for review in reviews:
        if len(review) > 50 and review[49] != " ":
            summary = review[:50].rsplit(' ', 1)[0] + "..."
        else:
            summary = review[:50] + "..."
        print(summary)

# Calls with dummy values
highlight_keywords(["This product is so good", "I had a bad experience"])
sentiment_tally(["I love this! It's excellent.", "This is terrible, a poor choice"], ["good", "excellent"], ["bad", "poor"])
create_review_summary(["This is a very long review that should be summarized.", "Short review"])
