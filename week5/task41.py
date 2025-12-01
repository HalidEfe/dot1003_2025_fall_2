def check_length(word, word2):
    if len(word) > len(word2):
        return word
    elif len(word2) > len(word):
        return word2
    else:
        print("Their length are same")

w1 = input("First Word:")
w2 = input("Second Word:")
result = check_length(w1, w2)

if result:
    print(result)