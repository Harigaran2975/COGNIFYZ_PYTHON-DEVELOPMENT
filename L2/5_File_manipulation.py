def count_words(filename):
    word_count = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.strip().lower().split()
                for word in words:
                    # Remove punctuation from word
                    word = ''.join(char for char in word if char.isalnum())
                    if word:
                        word_count[word] = word_count.get(word, 0) + 1

        # Display results in alphabetical order
        print("Word Frequencies (Alphabetical Order):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")


if __name__ == "__main__":
    filename = input("Enter the filename (with .txt): ")
    count_words(filename)
