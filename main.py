import speech_recognition as sr
from openai import OpenAI
import os
from playsound import playsound

OpenAI.api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()

#Sends the generated text prompt to Chat-GPT 3.5, returns the response
def analyze_text(user_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are acting as an AI assistant named Solaris to help manage a home, provide information and run certain systems, similar to the Jarvis or Friday AI Iron Man uses.  Talk in a similar style as these AI. Refer to yourself as Solaris in responses."},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=500,
    )
    response_text = response.choices[0].message.content
    return response_text

#Calls OpenAI TTS to generate audio clip from the recieved text
def play_audio(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    response.stream_to_file("audio/output.mp3")
    playsound("audio/output.mp3")

#Calls OpenAI Whisper to generate text from the recorded audio clip from the microphone
def get_audio_prompt():
    audio_file = open("audio/input.wav", "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    return transcript

#Generates audio clip from the microphone
def get_input_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Listening for speech...")
        recognizer.adjust_for_ambient_noise(mic)
        audio = recognizer.listen(mic)

    with open("audio/input.wav", "wb") as f:
        f.write(audio.get_wav_data())
        print("Audio saved as input.wav")


def main():
    get_input_audio()
    user_prompt = get_audio_prompt()
    print(user_prompt)
    analysis = analyze_text(user_prompt)
    print(analysis)
    play_audio(analysis)

main()