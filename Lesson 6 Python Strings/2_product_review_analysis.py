
# Task 1: Keyword Highlighter
def highlight_keywords(reviews):
    keywords = ["good", "excellent", "bad", "poor", "average"]
    for review in reviews:
        for keyword in keywords:
            if keyword in review.lower():
                review = review.replace(keyword, keyword.upper())
        print(review)

# Task 2: Sentiment Tally
def sentiment_tally(reviews):
    positive_words = ["good", "excellent"]
    negative_words = ["bad", "poor"]
    for review in reviews:
        positive_count = sum(review.lower().count(word) for word in positive_words)
        negative_count = sum(review.lower().count(word) for word in negative_words)
        print(f"Positive: {positive_count}, Negative: {negative_count}")

# Task 3: Review Summary
def review_summary(reviews):
    for review in reviews:
        if len(review) > 50 and review[49] != " ":
            summary = review[:50].rsplit(' ', 1)[0] + "..."
        else:
            summary = review[:50] + "..."
        print(summary)
if __name__ == '__main__':
    highlight_keywords("test")
    sentiment_tally("test")
    review_summary("test")