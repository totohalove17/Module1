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
    # File path input example
    file_path = 'test_01.txt'  # Example file path
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    print(f"Words: {count_words(text)}")
    print(f"Sentences: {count_sentences(text)}")


if __name__ == "__main__":
    main()