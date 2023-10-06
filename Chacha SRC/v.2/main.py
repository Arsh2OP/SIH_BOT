import speech_recognition as sr
import user_input_module as user_input
import aiml_module as aiml
import audio_module as audio

def main():
    recognizer = sr.Recognizer()
    english_kernel, hindi_kernel = aiml.initialize_aiml()
    audio.initialize_audio()

    input_method = input("Choose input method ('1.voice' or '2.text'): ")

    if input_method.lower() not in ["1", "2"]:
        print("Invalid input method. Please choose 'voice' or 'text'.")
    else:
        print("Hello, I am Chacha Chaudhary. I am here to assis you on NAMAMI Gange Project")

        while True:
            if input_method == "1":
                user_input_text = user_input.get_user_input(recognizer)
            else:
                user_input_text = input("You (Text): ")

            if user_input_text.lower() == "exit":
                print("Goodbye!")
                break

            response = aiml.respond_to_user_input(user_input_text, english_kernel, hindi_kernel)

            if response:
                print(f"Chacha Chaudhary: {response}")
                audio.play_response(response)
            else:
                print("I couldn't understand your request.")

    audio.cleanup()

if __name__ == "__main__":
    main()
