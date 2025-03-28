import re

def count_sentences(text: str) -> int:
    text = re.sub(r'\.{3}', '<ELLIPSIS>', text)
    sentences = re.split(r'[.!?]|<ELLIPSIS>', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)