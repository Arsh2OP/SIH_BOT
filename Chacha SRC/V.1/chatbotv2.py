import aiml
import speech_recognition as sr
import pyttsx3
import langid
import time


kernel = aiml.Kernel()


kernel.learn("English.aiml")


recognizer = sr.Recognizer()


engine_hindi = pyttsx3.init()


engine_english = pyttsx3.init()


def speak(text, language="en"):
    if language == "en":
        engine_english.say(text)
        engine_english.runAndWait()
    elif language == "hi":
        engine_hindi.say(text)
        engine_hindi.runAndWait()


def get_spoken_input(timeout=10):
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout)
            user_input = recognizer.recognize_google(audio, language="en")
            print("You (Voice):", user_input)  # Print user input on the screen
            return user_input.lower()
        except sr.WaitTimeoutError:
            print("Chacha Chaudhary: You didn't provide any input. Goodbye.")
        except sr.UnknownValueError:
            print("Chacha Chaudhary: I couldn't understand your voice. Please try again.")
        except sr.RequestError as e:
            print(f"Chacha Chaudhary: Error with speech recognition: {e}")
        return ""


def get_typed_input():
    user_input = input("You (Type): ").lower()
    return user_input

if __name__ == "__main__":
    
    while True:
        print("\nSelect Input Mode:")
        print("1. Voice Input")
        print("2. Type Input")
        
        choice = input("Enter 1 for Voice Input, 2 for Type Input: ")
        
        if choice == "1":
            introduction = "Hello, I am Chacha Chaudhary. How can I assist you today?"
            speak(introduction)
            
            while True:
                user_input = get_spoken_input()
                
                if user_input == "exit":
                    print("Chacha Chaudhary: Goodbye!")
                    break
                
                
                detected_language, _ = langid.classify(user_input)
                
                
                start_time = time.perf_counter()
                
                response = kernel.respond(user_input)
                
                
                end_time = time.perf_counter()
                
                if response:
                    print(f"Chacha Chaudhary ({detected_language}):", response)
                    speak(response, detected_language)  
                else:
                    print(f"Chacha Chaudhary ({detected_language}): I'm sorry, I couldn't understand your request.")
                
                
                response_time = end_time - start_time
                print(f"Response Time: {response_time:.2f} seconds")
        
        elif choice == "2":
            introduction = "Hello, I am Chacha Chaudhary. How can I assist you today?"
            print(introduction)
            
            while True:
                user_input = get_typed_input()
                
                if user_input == "exit":
                    print("Chacha Chaudhary: Goodbye!")
                    break
                
                
                detected_language, _ = langid.classify(user_input)
                
                
                start_time = time.perf_counter()
                
                response = kernel.respond(user_input)
                
            
                end_time = time.perf_counter()
                
                if response:
                    print(f"Chacha Chaudhary ({detected_language}):", response)
                    speak(response, detected_language)  
                else:
                    print(f"Chacha Chaudhary ({detected_language}): I'm sorry, I couldn't understand your request.")
                
                
                response_time = end_time - start_time
                print(f"Response Time: {response_time:.2f} seconds")
        
        else:
            print("Invalid choice. Please select 1 or 2.")
