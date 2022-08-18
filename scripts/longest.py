# finds longest word in txt file, then makes all occurances of that word bold

with open('longest.txt', 'r') as f:
    longest = 0
    for line in f:
        words = line.split()
        for word in words:
            if len(word) > longest:
                longest = len(word)
                longest_word = word
    print(longest_word)
    with open('longest.txt', 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word == longest_word:
                    print('<b>' + word + '</b>', end='')
                else:
                    print(word, end='')
            print()
