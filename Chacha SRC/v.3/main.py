import speech_recognition as sr
import aiml_module as aiml
import audio_module as audio
import user_input_module as user_input  
def main():
    recognizer = sr.Recognizer()
    english_kernel, hindi_kernel = aiml.initialize_aiml()
    audio.initialize_audio()

    input_method = input("Choose input method ('1.voice' or '2.text'): ")

    if input_method.lower() not in ["1", "2"]:
        print("Invalid input method. Please choose 'voice' or 'text'.")
    else:
        print("Hello, I am Chacha Chaudhary. I am here to assist you on NAMAMI Gange Project")

        while True:
            if input_method == "1":
                user_input_text = user_input.get_spoken_input(recognizer)
            else:
                user_input_text = input("You (Text): ")

            if user_input_text.lower() == "exit":
                print("Goodbye!")
                break

            detected_language = user_input.detect_input_language(user_input_text)

            if "chacha chaudhary" in user_input_text.lower():
                print(f"Chacha Chaudhary ({detected_language}): Yes, I am Chacha Chaudhary. How can I assist you?")
                continue

            response = aiml.respond_to_user_input(user_input_text, detected_language, english_kernel, hindi_kernel)

            if response:
                print(f"Chacha Chaudhary ({detected_language}): {response}")
                audio.play_response(response)
            else:
                print(f"Chacha Chaudhary ({detected_language}): I couldn't understand your request.")

    audio.cleanup()

if __name__ == "__main__":
    main()
