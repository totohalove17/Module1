import re

def count_sentences(text: str) -> int:
    text = re.sub(r'\.{3}', '<ELLIPSIS>', text)
    sentences = re.split(r'[.!?]|<ELLIPSIS>', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)

def count_words(text: str) -> int:
    text = re.sub(r'[,:;]', ' ', text)
    words = text.split()
    return len(words)

def main():
    file_path = input("Enter the path to the .txt file: ")
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    print(f"Words: {count_words(text)}")
    print(f"Sentences: {count_sentences(text)}")

if __name__ == "__main__":
     main()