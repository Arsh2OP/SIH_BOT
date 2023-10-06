import speech_recognition as sr
import aiml_module as aiml
import audio_module as audio
import user_input_module as user_input
from intent_recognition import recognize_intent, responses

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

            recognized_intent = recognize_intent(user_input_text, detected_language)

            if recognized_intent:
                response = responses.get(recognized_intent, "I'm not sure how to respond to that intent.")
                print(f"Chacha Chaudhary ({recognized_intent}): {response}")
                audio.play_audio(response)
            else:
                aiml_response = aiml.respond_to_user_input(user_input_text, detected_language, english_kernel, hindi_kernel)
                if aiml_response:
                    print(f"Chacha Chaudhary ({detected_language}): {aiml_response}")
                    audio.play_audio(aiml_response)
                else:
                    print("Chacha Chaudhary: I'm sorry, I couldn't understand your question. Please try rephrasing it.")

    audio.cleanup_audio()

if __name__ == "__main__":
    main()
