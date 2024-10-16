from openai import OpenAI

# Instantiate the OpenAI client with the correct API key syntax
client = OpenAI(api_key="..")

# Use a raw string for the file path to avoid escape sequence issues
audio_file = open(r"F:\testing_data\harvard.wav", "rb")

# Generate the transcription using the Whisper model
transcription = client.audio.transcriptions.create(model="whisper-1", file=audio_file)

# Print the transcription text
print(transcription.text)
