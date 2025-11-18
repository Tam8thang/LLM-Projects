from transformers import pipeline

generator = pipeline("text-generation", model="baidu/ERNIE-4.5-21B-A3B-Thinking")
print(generator(
    "我想去",
    max_length=10,
    num_return_sequences=3,
))