print("--- Begin report of books/frankenstein.txt ---")

def main():

    with open("books/frankestein.txt") as f:
        f_contents = f.read()
        return f_contents

def count_words(word_string):
    content = word_string.split()
    return len(content)
    
def count_characters(text):
    text = text.lower()
    
    char= {}
    for c in text:
        if c.isalpha():
            if c in char:
                char[c] += 1
            else:
                char[c] =1
        
    return char
    

content = main()
words = count_words(content)
char_dict = count_characters(content)

# print(character)
print(f"{words} words found in the document")
print()


for key,value in char_dict.items():
    print(f"The '{key}' character was found {value} times") 
    
print("--- End Report ---")