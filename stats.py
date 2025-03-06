def get_num_words(text):
    words = text.split()
    return len(words)


def amount_each_letter(text):
    low_text = str.lower(text)
    dict = {}
    for char in low_text:
        if char not in dict:
            dict[char] = 1
        elif char in dict:
            dict[char] += 1
    return dict

def sort_on(dict):
    return dict["num"]

def sort_dict(letter_dict):
    letter_list = []
    for letter in letter_dict:
        if letter.isalpha():
            temp = {"char": letter, "num": letter_dict[letter]}
            letter_list.append(temp)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
        
        