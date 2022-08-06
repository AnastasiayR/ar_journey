def check_word_transformation (word_1, word_2):
    count_error = 0
    for i_sym in range(len(word_1)):
        if word_1[i_sym] != word_2[i_sym]:
            count_error += 1
    if count_error == 1:
        return True
    return False

def print_way_transformation(my_dict, my_word):
    if not my_word in my_dict.keys():
        print(my_word)
        return 0
    print(my_word, end ='-')
    print_way_transformation(my_dict, my_dict[my_word])

def search_way(start_word, end_word, words_list, pairs_word_dict):
    current_word = []
    current_word.append(end_word)
    next_words = []
    last_word = []
    while True:
        for exodus in current_word:
            for word in words_list:
                if not word in current_word and not word in last_word:
                    if check_word_transformation(exodus, word):
                        next_words.append(word)
                        pairs_word_dict[word] = exodus
        last_word.extend(current_word)
        current_word = next_words
        next_words = []
        if len(last_word)==len(words_list) or len (current_word)==0:
            break
    if start_word in last_word:
        return True
    else:
        return False


original_list = ['сок','тор','том', 'дом', 'сор', 'вор', 'тим', 'сом', 'доп']

start_word = 'тим'
end_word = 'вор'
total_dict = dict()
if search_way(start_word, end_word, original_list, total_dict):
    print('\nНайден путь:')
    print_way_transformation(total_dict, start_word)
else:
    print('Нет решения')