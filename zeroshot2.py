from transformers import pipeline

classifier = pipeline("zero-shot-classification")

print(
    classifier(
        "Ukraine's Energy Minister Svitlana Grynchuk and Justice Minister German Galushchenko submitted their resginations, Prime Minister Yulia Svyrydenko said Wednesday amid a wide-reaching corruption scandal involving the state nuclear power company.",
        candidate_labels=["peace", "politics", "business", "corruption", "war"],
))

