import csv
import tkinter as tk

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

    return f"No similar word found for '{word_to_find}'."

def on_submit():
    user_input = entry.get()
    result = find_meaning(user_input, "genz_slang.csv")  # Replace with your actual file path
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Jessica's Gen-Z Translator")

# Add margin to the sides
root.geometry("400x200+100+100")  # width x height + x_offset + y_offset

# Create and place widgets with added margins
label = tk.Label(root, text="Enter a word:")
label.pack(pady=10, padx=20)

entry = tk.Entry(root)
entry.pack(pady=10, padx=20)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10, padx=20)

result_label = tk.Label(root, text="")
result_label.pack(pady=10, padx=20)

# Start the main event loop
root.mainloop()

