#Raise the Issues if any doubts are present...
import speech_recognition as sr
import pyttsx3
import openai

# Set up your OpenAI API key
openai.api_key = 'Your_API_KEY'

# Text-to-speech engine setup
engine = pyttsx3.init()

# Speech recognition setup
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)  # Set a timeout of 5 seconds
            text = recognizer.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return None
        except sr.WaitTimeoutError:
            print("Timeout: Please try speaking again.")
            return None

def speak(text):
    print("Jarvis:", text)
    # Adjust text-to-speech settings
    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
    engine.setProperty('volume', 1.0)  # Adjust the speech volume (0.0 to 1.0)
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello, I am Jarvis. How can I assist you today?")
    
    while True:
        user_input = listen()

        if user_input:
            print("User:", user_input)
            
            # Check if the user wants to quit
            if user_input == 'quit':
                speak("Thank you! Have a nice day.")
                break

            # Communicate with ChatGPT API
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "system", "content": "You are a helpful voice assistant."},
                          {"role": "user", "content": user_input}],
                max_tokens=150
            )
            jarvis_response = response['choices'][0]['message']['content']
            
            speak(jarvis_response)

if __name__ == "__main__":
    main()
