from Art import logo
print(logo)
alphabet = ["a", "b", "c", "d", "e","f", "g","h",
"i","j","k", "l","m","n","o","p", "q","r","s",
"t","u","v","w","x","y","z","a","b","c","d","e",
"f", "g","h","i","j","k", "l","m","n","o","p",
 "q","r","s","t","u","v","w","x","y","z"]
def ceaser(text,shift, direction):
    cipher_Text =""
    if direction == "decode":
            shift *= -1
    for letter in text:
        if letter in alphabet:
            position =alphabet.index(letter)
            new_position = position+shift
            cipher_Text += alphabet[new_position]
        else:
            cipher_Text +=letter

    print(f"The {direction}d text is {cipher_Text}")     
should_continue =True
while(should_continue==True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    ceaser(text,shift,direction)
    results = input("Type 'yes' if you want to go again and 'no' to exit\n").lower()
    if results =="yes":
        should_continue =True
    else:
        should_continue =False
        print("\nGoodbye")