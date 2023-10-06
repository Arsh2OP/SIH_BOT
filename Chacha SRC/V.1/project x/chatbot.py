import aiml
import speech_recognition as sr
import pyttsx3
import langid

def initialize_kernels():
    # Initialize AIML kernels
    english_kernel = aiml.Kernel()
    hindi_kernel = aiml.Kernel()
    english_kernel.learn("English.aiml")
    hindi_kernel.learn("Hindi.aiml")

    # Initialize speech recognition
    recognizer = sr.Recognizer()

    # Initialize text-to-speech engines
    engine_english = pyttsx3.init()
    engine_hindi = pyttsx3.init()

    return english_kernel, hindi_kernel, recognizer, engine_english, engine_hindi

def get_user_input(recognizer, engine_english, engine_hindi):
    # Implementation for getting user input (voice)
    with sr.Microphone() as source:
        print("Listening...")
        try:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=5)
            user_input = recognizer.recognize_google(audio, language="hi-IN")
            print("You (Voice):", user_input)
            return user_input.lower()
        except sr.WaitTimeoutError:
            speak_response("You didn't provide any input. Goodbye.", "en", engine_english, engine_hindi)
            return ""
        except sr.UnknownValueError:
            speak_response("I couldn't understand your voice. Please try again.", "en", engine_english, engine_hindi)
            return ""
        except sr.RequestError as e:
            speak_response(f"Error with speech recognition: {e}", "en", engine_english, engine_hindi)
            return ""

def respond_to_user_input(user_input, detected_language, english_kernel, hindi_kernel, engine_english, engine_hindi):
    # Implementation for responding to user input
    if detected_language == "hi":
        response = hindi_kernel.respond(user_input)
    else:
        response = english_kernel.respond(user_input)

    if response:
        print(f"Chacha Chaudhary ({detected_language}):", response)
        speak_response(response, detected_language, engine_english, engine_hindi)
    else:
        print(f"Chacha Chaudhary ({detected_language}): I'm sorry, I couldn't understand your request.")
        speak_response("I'm sorry, I couldn't understand your request.", detected_language, engine_english, engine_hindi)

def speak_response(response, language, engine_english, engine_hindi):
    # Implementation for speaking the bot's response
    engine = engine_english if language == "en" else engine_hindi
    engine.say(response)
    engine.runAndWait()

def handle_voice_input(english_kernel, hindi_kernel, recognizer, engine_english, engine_hindi):
    # Implementation for handling voice input
    speak_response("Hello, I am Chacha Chaudhary. How can I assist you today?", "hi", engine_english, engine_hindi)

    while True:
        user_input = get_user_input(recognizer, engine_english, engine_hindi)

        if user_input == "exit":
            speak_response("Goodbye!", "en", engine_english, engine_hindi)
            break

        detected_language, _ = langid.classify(user_input)

        if "chacha chaudhary" in user_input.lower():
            speak_response("Yes, I am Chacha Chaudhary. How can I assist you?", detected_language, engine_english, engine_hindi)
            continue

        respond_to_user_input(user_input, detected_language, english_kernel, hindi_kernel, engine_english, engine_hindi)

def handle_typed_input(english_kernel, hindi_kernel, engine_english, engine_hindi):
    # Implementation for handling typed input
    speak_response("Hello, I am Chacha Chaudhary. How can I assist you today?", "hi", engine_english, engine_hindi)

    while True:
        user_input = input("You (Type): ").lower()

        if user_input == "exit":
            speak_response("Goodbye!", "en", engine_english, engine_hindi)
            break

        detected_language, _ = langid.classify(user_input)

        if "chacha chaudhary" in user_input.lower():
            speak_response("Yes, I am Chacha Chaudhary. How can I assist you?", detected_language, engine_english, engine_hindi)
            continue

        respond_to_user_input(user_input, detected_language, english_kernel, hindi_kernel, engine_english, engine_hindi)

def cleanup(engine_english, engine_hindi):
    # Cleanup resources, such as speech engines
    engine_english.stop()
    engine_hindi.stop()
