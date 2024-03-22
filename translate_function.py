from googletrans import Translator

def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text

def translator_main():
    while True:
        text = input("Enter text to translate (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        translated_text = translate_to_english(text)
        print("Translated to English:", translated_text)

if __name__ == "__main__":
    translator_main()
