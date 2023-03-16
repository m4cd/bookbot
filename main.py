book = "books/frankenstein.txt"

with open(book) as f:
    file_contents = f.read()
    words = file_contents.split()
    wordCount = len(words)
    dict = dict()

    for word in words:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                if letter not in dict:
                    dict.update({letter : 1})
                else:
                    dict.update({letter : (dict[letter]+1)})
    
    

    print(f"--- Begin report of {book} ---")
    print(f"{wordCount} words found in the document")
    print("")

    for letter in range(len(dict)):
        maxKey = max(dict, key=dict.get)
        maxV = max(dict.values())
        del dict[maxKey]
        print(f"The '{maxKey}' character was found {maxV} times")

    print("--- End report ---")