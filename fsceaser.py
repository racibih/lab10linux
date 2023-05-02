import sys

def main():
    # Get the shift amount from the command line arguments
    shift = int(sys.argv[1])

    # Read in the message from the keyboard
    message = input().upper()

    # Encode each letter by shifting it the right amount
    encoded = ""
    for letter in message:
        if letter.isalpha():
            encoded += chr((ord(letter) - 65 + shift) % 26 + 65)

    # Print the final encoded message in blocks of five letters
    count = 0
    for i in range(0, len(encoded), 5):
        if count == 10:
            print()
            count = 0
        print(encoded[i:i+5], end=" ")
        count += 1

if __name__ == "__main__":
    main()

