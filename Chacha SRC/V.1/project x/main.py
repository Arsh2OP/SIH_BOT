import aiml
import speech_recognition as sr
import pyttsx3
import langid
import logging
from chatbot import (
    initialize_kernels,
    get_user_input,
    respond_to_user_input,
    speak_response,
    handle_voice_input,
    handle_typed_input,
    cleanup,
)

# Initialize AIML kernels and other components
english_kernel, hindi_kernel, recognizer, engine_english, engine_hindi = initialize_kernels()

# Logging configuration
logging.basicConfig(filename='chatbot.log', level=logging.INFO, format='%(message)s')

if __name__ == "__main__":
    while True:
        print("\nSelect Input Mode:")
        print("1. Voice Input")
        print("2. Type Input")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            handle_voice_input(english_kernel, hindi_kernel, recognizer, engine_english, engine_hindi)
        elif choice == "2":
            handle_typed_input(english_kernel, hindi_kernel, engine_english, engine_hindi)  # Pass the engines here
        elif choice == "3":
            print("Chacha Chaudhary: Goodbye!")
            cleanup(engine_english, engine_hindi)
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
