from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

import re

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)


def summary_text(text):
    summaries = []
    chapter_list = text.split("!!!")
    for chapter in chapter_list:
        chapter = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?",
                         "",
                         chapter)
                         
        summarized = summarizer(chapter, min_length=30, max_length=50)
        summaries.append(summarized)
    return summaries


