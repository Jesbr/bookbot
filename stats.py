def get_num_words(number_count):
    words = number_count.split()
    return len(words)

def get_char_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        counts[char] = counts.get(char, 0) + 1
    high_low = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    return high_low

def dict_of_dict(hub):
    sorted_list = sorted(
        [{'char': char, 'num': count} for char, count in hub.items()],
        key=lambda x: x['num'], reverse=True
        )
    return sorted_list
