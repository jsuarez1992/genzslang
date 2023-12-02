import csv


def find_meaning(word_to_find, file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Skip the header if your CSV file has one
        next(reader, None)

        # Search for the word
        for row in reader:
            word_and_meaning = row[0].split(',')
            word = word_and_meaning[0].strip()
            meaning = word_and_meaning[1].strip() if len(word_and_meaning) > 1 else ""

            # Check for similarity (you can adjust the similarity criteria)
            if word_to_find.lower() in word.lower() or word.lower() in word_to_find.lower():
                return f"Meaning for '{word}': {meaning}"

    return f"No similar word found for '{word_to_find}'."


if __name__ == "__main__":
    csv_file_path = "genz_slang.csv"  # Replace with your actual file path

    user_input = input("Enter a word: ")
    result = find_meaning(user_input, csv_file_path)
    print(result)
