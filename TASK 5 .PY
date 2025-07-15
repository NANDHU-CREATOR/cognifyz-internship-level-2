def count_words_in_file(filename):
    word_count = {}

    
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().lower().split()
            for word in words:
                word = word.strip(".,!?\"'()[]{}")
                if word:
                    word_count[word] = word_count.get(word, 0) + 1

    
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

count_words_in_file('sample.txt')
