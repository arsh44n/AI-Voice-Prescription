import tkinter as tk
from tkinter import messagebox, scrolledtext
import sounddevice as sd
import numpy as np
import speech_recognition as sr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import json
import os

# Global configuration
SAMPLE_RATE = 16000  # Sample rate for recording
DURATION = 5  # Recording duration in seconds
AUDIO_FILE = "recording.wav"

# Function to record audio
def record_audio():
    try:
        messagebox.showinfo("Recording", "Recording will start for 5 seconds. Please speak clearly.")
        # Record audio
        audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
        sd.wait()  # Wait for the recording to finish

        # Save to WAV file
        audio_data = (audio_data * 32767).astype(np.int16)  # Convert to int16 for WAV
        with open(AUDIO_FILE, "wb") as f:
            import wave
            with wave.open(f, "w") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(SAMPLE_RATE)
                wf.writeframes(audio_data.tobytes())

        messagebox.showinfo("Recording Complete", "Recording saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Error during recording: {e}")

# Function to transcribe audio
def transcribe_audio():
    if not os.path.exists(AUDIO_FILE):
        messagebox.showerror("Error", "No recording found. Please record audio first.")
        return

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        transcription_box.delete(1.0, tk.END)
        transcription_box.insert(tk.END, text)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand the audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"API error: {e}")

# Function to classify prescription
def classify_prescription():
    input_text = transcription_box.get(1.0, tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", "No transcription found. Please transcribe audio first.")
        return

    categories = {
        "antibiotic": ["amoxicillin", "penicillin", "azithromycin"],
        "painkiller": ["ibuprofen", "paracetamol", "aspirin"],
        "antidepressant": ["sertraline", "fluoxetine", "citalopram"],
        "antihistamine": ["loratadine", "cetirizine", "diphenhydramine"]
    }

    training_texts = [
        "Take 500mg of amoxicillin twice daily",
        "Take ibuprofen 200mg for pain relief",
        "Use 20mg of fluoxetine every morning",
        "Take 10mg of loratadine once a day"
    ]
    labels = ["antibiotic", "painkiller", "antidepressant", "antihistamine"]

    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(training_texts)

    classifier = MultinomialNB()
    classifier.fit(X_train, labels)

    X_input = vectorizer.transform([input_text])
    prediction = classifier.predict(X_input)[0]

    medication_name = ""
    dosage = None  # Set dosage as None initially
    frequency = ""

    # Extract medication details from input_text
    for word in input_text.split():
        if word.lower() in categories[prediction]:
            medication_name = word
        # Capture dosage directly as an integer from the input (e.g., 500)
        if word.isdigit():  # If the word is a number, it's the dosage
            dosage = int(word)
        if "once" in input_text.lower():
            frequency = "Once a day"
        elif "twice" in input_text.lower():
            frequency = "Twice a day"
        elif "every" in input_text.lower():
            frequency = "Every day"

    # Ensure dosage is captured as integer
    if dosage is None:
        dosage = 0  # Default if no dosage is found

    structured_data = {
        "Medication type": prediction,
        "Medicine Name": medication_name.capitalize(),
        "Dosage": dosage,
        "Frequency": frequency
    }
    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, json.dumps(structured_data, indent=4))

# GUI setup
root = tk.Tk()
root.title("AI-Driven Prescription Classifier")

# Instructions
instructions = tk.Label(root, text="Use the buttons below to record, transcribe, and classify prescriptions.")
instructions.pack(pady=10)

# Buttons
record_button = tk.Button(root, text="Record Voice", command=record_audio)
record_button.pack(pady=5)

transcribe_button = tk.Button(root, text="Transcribe Audio", command=transcribe_audio)
transcribe_button.pack(pady=5)

classify_button = tk.Button(root, text="Classify Prescription", command=classify_prescription)
classify_button.pack(pady=5)

# Text boxes
transcription_label = tk.Label(root, text="Transcription:")
transcription_label.pack(pady=5)
transcription_box = scrolledtext.ScrolledText(root, height=5, width=50)
transcription_box.pack(pady=5)

result_label = tk.Label(root, text="Classification Result:")
result_label.pack(pady=5)
result_box = scrolledtext.ScrolledText(root, height=10, width=50)
result_box.pack(pady=5)

# Run the GUI
root.mainloop()
