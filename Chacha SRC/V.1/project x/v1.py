import aiml
import speech_recognition as sr
import pyttsx3
import langid
import pickle
import os

# File path for storing conversation history
CONVERSATION_HISTORY_FILE = "conversation_history.pkl"

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

def load_conversation_history():
    if os.path.exists(CONVERSATION_HISTORY_FILE):
        try:
            with open(CONVERSATION_HISTORY_FILE, "rb") as file:
                conversation_history = pickle.load(file)
        except Exception as e:
            print(f"Error loading conversation history: {e}")
            conversation_history = []
    else:
        print(f"Conversation history file '{CONVERSATION_HISTORY_FILE}' does not exist. Creating a new one.")
        conversation_history = []

    return conversation_history

def save_conversation_history(conversation_history):
    with open(CONVERSATION_HISTORY_FILE, "wb") as file:
        pickle.dump(conversation_history, file)

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

def respond_to_user_input(user_input, detected_language, english_kernel, hindi_kernel, engine_english, engine_hindi, conversation_history):
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

    # Update conversation history
    conversation_history.append((user_input, response))

def speak_response(response, language, engine_english, engine_hindi):
    # Implementation for speaking the bot's response
    engine = engine_english if language == "en" else engine_hindi
    engine.say(response)
    engine.runAndWait()

def handle_voice_input(english_kernel, hindi_kernel, recognizer, engine_english, engine_hindi, conversation_history):
    # Implementation for handling voice input
    speak_response("Hello, I am Chacha Chaudhary. How can I assist you today?", "hi", engine_english, engine_hindi)

    while True:
        user_input = get_user_input(recognizer, engine_english, engine_hindi)

        if user_input == "exit":
            clear_conversation(conversation_history)  # Clear conversation history
            speak_response("Goodbye!", "en", engine_english, engine_hindi)
            break

        detected_language, _ = langid.classify(user_input)

        if "chacha chaudhary" in user_input.lower():
            speak_response("Yes, I am Chacha Chaudhary. How can I assist you?", detected_language, engine_english, engine_hindi)
            continue

        respond_to_user_input(user_input, detected_language, english_kernel, hindi_kernel, engine_english, engine_hindi, conversation_history)

def handle_typed_input(english_kernel, hindi_kernel, engine_english, engine_hindi, conversation_history):
    # Implementation for handling typed input
    speak_response("Hello, I am Chacha Chaudhary. How can I assist you today?", "hi", engine_english, engine_hindi)

    while True:
        user_input = input("You (Type): ").lower()

        if user_input == "exit":
            clear_conversation(conversation_history)  # Clear conversation history
            speak_response("Goodbye!", "en", engine_english, engine_hindi)
            break

        detected_language, _ = langid.classify(user_input)

        if "chacha chaudhary" in user_input.lower():
            speak_response("Yes, I am Chacha Chaudhary. How can I assist you?", detected_language, engine_english, engine_hindi)
            continue

        respond_to_user_input(user_input, detected_language, english_kernel, hindi_kernel, engine_english, engine_hindi, conversation_history)

def clear_conversation(conversation_history):
    # Clear conversation history
    conversation_history.clear()

def cleanup(engine_english, engine_hindi):
    # Cleanup resources, such as speech engines
    engine_english.stop()
    engine_hindi.stop()

if __name__ == "__main__":
    # Load conversation history from the file
    conversation_history = load_conversation_history()

    english_kernel, hindi_kernel, recognizer, engine_english, engine_hindi = initialize_kernels()
    try:
        while True:
            print("Choose Input Mode:")
            print("1. Voice Input")
            print("2. Typed Input")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                handle_voice_input(english_kernel, hindi_kernel, recognizer, engine_english, engine_hindi, conversation_history)
            elif choice == "2":
                handle_typed_input(english_kernel, hindi_kernel, engine_english, engine_hindi, conversation_history)
            elif choice == "3":
                # Save conversation history before exiting
                save_conversation_history(conversation_history)
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    except KeyboardInterrupt:
        pass
    finally:
        cleanup(engine_english, engine_hindi)
