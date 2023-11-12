from elevenlabs import set_api_key,generate,play
set_api_key("0e5e5aaaa76605da4a7f5b670e4ccd49")

def speak(text):
    audio = generate(
        text=text,
        voice="Bella",
        model="eleven_multilingual_v2"
)
    play(audio)