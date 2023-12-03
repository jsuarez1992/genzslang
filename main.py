import csv
import tkinter as tk
from tkinter import ttk

def find_meaning(word_to_find, file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Skip the header if your CSV file has one
        next(reader, None)

        # Convert user input to lowercase
        word_to_find_lower = word_to_find.lower()

        # Search for the word
        for row in reader:
            word_and_meaning = row[0].split(',')
            word = word_and_meaning[0].strip().lower()
            meaning = word_and_meaning[1].strip() if len(word_and_meaning) > 1 else ""

            # Check for whole word similarity
            if f" {word_to_find_lower} " in f" {word} ":
                return f"Meaning for '{word}': {meaning}"

    return f"{word_to_find}"

def translate_sentence(sentence, file_path):
    words_and_meanings = []

    # Split the sentence into words
    words = sentence.split()

    # Find translations for each word
    for word in words:
        translation = find_meaning(word, file_path)
        words_and_meanings.append((word, translation))

    # Create the translated sentence
    # Create the translated sentence
    translated_sentence = []

    # Iterate over each phrase and its translation
    for original_phrase, translation in words_and_meanings:
        if translation is not None:
            meaning_parts = translation.split(': ')
            if len(meaning_parts) > 1:
                translated_sentence.append(f"{meaning_parts[1]}")
            else:
                translated_sentence.append(f"{translation}")
        else:
            translated_sentence.append(original_phrase)

    return " ".join(translated_sentence)



def on_submit():
    user_input = entry.get()
    result = translate_sentence(user_input, "genz_slang.csv")  # Replace with your actual file path
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Word Translator")

# Add margin to the sides
root.geometry("600x200+100+100")  # width x height + x_offset + y_offset

# Create and place widgets with added margins
label = tk.Label(root, text="Enter a sentence:")
label.pack(pady=10, padx=20)

entry = tk.Entry(root, width=50)
entry.pack(pady=10, padx=20)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10, padx=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10, padx=20)

# Start the main event loop
root.mainloop()
