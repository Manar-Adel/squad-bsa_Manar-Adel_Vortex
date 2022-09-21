#Build a Translator

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou": #vowels changed to "V" , only the translated letter is UPPERCASE
                translation+="V"
        else:
            translation+=letter.lower()    

    return translation       

print(translate(input("Enter a phrase: ")))     
