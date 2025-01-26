# AI-Voice-Prescription
AI-Driven Prescription Classifier
# AI-Driven Prescription Classifier

This is an AI-powered prescription classifier built using Python and machine learning. The application records voice input, transcribes the speech to text, and then classifies the prescription details such as medication type, medicine name, dosage, and frequency. The classifier uses a pre-trained Naive Bayes model to predict the medication type and extracts dosage and frequency from the transcribed text.

## Features

- **Voice Recording**: The app records voice for 5 seconds and saves it as an audio file.
- **Speech-to-Text**: Transcribes the recorded audio into text using Google's Speech Recognition API.
- **Prescription Classification**: Classifies the prescription into medication type (antibiotic, painkiller, antidepressant, etc.), extracts the medicine name, dosage (as an integer), and frequency from the transcribed text.
- **GUI Interface**: A user-friendly GUI built with Tkinter for easy interaction.

## Requirements

- Python 3.x
- Required Libraries:
  - `tkinter`: For creating the GUI interface.
  - `sounddevice`: For recording audio.
  - `numpy`: For handling audio data and manipulation.
  - `speechrecognition`: For transcribing the speech to text.
  - `scikit-learn`: For the machine learning model (Naive Bayes classifier).
  - `pyaudio` (optional): For sound recording if not using `sounddevice`.
  - `wave`: For handling WAV file format.

## Installation

### 1. Install Python

Ensure that Python 3.x is installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/)

### 2. Install Dependencies

Use pip to install the required libraries:

```bash
pip install sounddevice numpy speechrecognition scikit-learn tk
```

If you're missing any specific library, you can install them manually via pip as needed.

### 3. Set up your environment

Make sure that your microphone is connected and working properly for audio recording.

### 4. Running the Application

1. Clone the repository or download the code.
2. Navigate to the project directory in your terminal or command prompt.
3. Run the script using:

   ```bash
   python app.py
   ```

This will launch the GUI where you can start recording, transcribing, and classifying prescriptions.

## Usage

- **Record Audio**: Click the "Record Voice" button to start recording your prescription.
- **Transcribe Audio**: After recording, click the "Transcribe Audio" button to convert the audio into text.
- **Classify Prescription**: Once the transcription is available, click "Classify Prescription" to predict the medication type, name, dosage, and frequency based on the transcription.

The result will be displayed in the GUI as a structured JSON output.

### Example Input and Output

#### Example Input (Voice):
"Take 500 mg of amoxicillin twice a day"

#### Example Output (JSON):
```json
{
    "Medication type": "antibiotic",
    "Medicine Name": "Amoxicillin",
    "Dosage": 500,
    "Frequency": "Twice a day"
}
```

## How It Works

1. **Recording Audio**: The user clicks "Record Voice," which captures the user's voice using the `sounddevice` library and saves it as a `.wav` file.
2. **Transcribing Audio**: The `speechrecognition` library is used to convert the recorded audio into text using Google's Speech Recognition API.
3. **Classifying Prescription**: A simple machine learning model (Naive Bayes) is trained on sample prescription data to predict the medication type based on the transcription. The dosage is extracted as an integer, and the frequency is detected by parsing keywords like "once," "twice," etc.

## Screenshots

1. **Interface:**
![Screenshot 2025-01-26 192650](https://github.com/user-attachments/assets/0f274428-98f2-45a1-a5dc-f28582195f94)

2. **Record Your Voice:**
   
![Screenshot 2025-01-26 192706](https://github.com/user-attachments/assets/9435170e-0501-40fa-9702-04899e3c31cc)

3. **Transcribe Audio and Classify Presciption:**
   
![Screenshot 2025-01-26 192727](https://github.com/user-attachments/assets/d1f7eafd-3cc8-4e22-abdd-66d9d85db990)


## Troubleshooting

1. **Microphone Issues**: Ensure your microphone is connected and selected as the input device in your operating system settings.
2. **No Transcription Found**: If the transcription is not recognized, try speaking clearly and ensure the audio is of good quality.
3. **Installation Issues**: If you encounter any errors related to missing libraries, make sure to install them using `pip install <library-name>`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Google's Speech Recognition API for converting speech to text.
- `scikit-learn` for providing the tools for creating the machine learning model.
- `sounddevice` for audio recording functionality.

