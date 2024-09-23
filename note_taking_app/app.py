from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# File to store notes
NOTES_FILE = 'notes.txt'

# Function to load notes from a file
def load_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as file:
            return file.read().splitlines()  # Each line represents a note
    return []

# Function to save a new note to the file
def save_note(note):
    with open(NOTES_FILE, 'a') as file:
        file.write(note + '\n')

@app.route("/", methods=["GET", "POST"])
def index():
    notes = load_notes()  # Load notes from the file
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            save_note(note)  # Save the new note to the file
        return redirect('/')  # Redirect to the homepage after saving
    return render_template("sample.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)