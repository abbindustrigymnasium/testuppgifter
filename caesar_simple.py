def caesar(message, shift):
    encoded_message = ""
    alph=["a","b","c","d","e","f","g","h","i","j","k","l",\
          "m","n","o","p","q","r","s","t","u","v","w","x",\
            "y","z","å","ä","ö"]
    for char in message:
        enc_char=alph[(alph.index(char)+shift)% len(alph)]
        encoded_message += enc_char
    return encoded_message

def main():
    message = input("Enter your message to encode: ")
    shift=3

    encoded_message = caesar(message, shift)
    print("Encoded message:", encoded_message)

if __name__ == "__main__":
    main()
