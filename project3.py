#Word replace program

def replace_word():

    str = "Hi, how are you all? I'm Sakib Sakib sakib"
    word_to_rep = input("Enter the word which will replace: ")
    replac_with = input("enter the word replace with: ")

    print(str.replace(word_to_rep, replac_with))

replace_word()