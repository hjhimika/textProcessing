from openai import OpenAI
client = OpenAI(api_key="...")

audio_file= open(r"F:\testing_data\Bruce Foster & Julie Beaufort.mp3", "rb")

transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)
print('\n'+"second")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)

