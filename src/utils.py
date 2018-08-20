import re, string

pattern = re.compile("[\d{}]+$".format(re.escape(string.punctuation)))

def preprocess(text):
    # remove punctuations
    text = re.sub("[()/.:?,!@#$%\"']", "", text)
    new_string = ""
    for token in text.split():
        # check if no alphabet character
        if not pattern.match(token):
            # if not in all-caps, make it lower case
            if not token.isupper():
                token = token.lower()
            new_string += (token + " ")
    return new_string

def create_n_gram(text, n):
    new_string = ""
    for token in text.split():
        if len(token) <= n:
            new_string += (token + " ")
        else:
            for i in range(len(token)-n+1):
                new_string += (token[i:i+n] + " ")
    return new_string.strip()

def create_full_word_and_n_gram(text, n):
    new_string = ""
    for token in text.split():
        new_string += (token + " ")
        if len(token) > n:
            for i in range(len(token)-n+1):
                new_string += (token[i:i+n] + " ")
    return new_string.strip()