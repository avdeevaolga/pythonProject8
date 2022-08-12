# Задание 3

def get_texts():
    TEXTS_DIR = 'texts'
    full_path_to_texts = os.path.join(os.getcwd(), TEXTS_DIR)
    texts_list = os.listdir(full_path_to_texts)
    all_texts = {}
    for file in texts_list:
        file_path = os.path.join(full_path_to_texts, file)
        with open(file_path, 'r', encoding = 'utf-8') as file_to_read:
            list_of_strings = []
            for line in file_to_read:
                list_of_strings.append(line.strip())
            text = '\n'.join(list_of_strings)
        all_texts[len(list_of_strings)] = {'name': file, 'length': str(len(list_of_strings)), 'text': text}
    return all_texts


def write_down_sorted_texts():
    SORTED_FILE = 'sorted_texts.txt'
    sorted_full_path = os.path.join(os.getcwd(), SORTED_FILE)
    all_texts = get_texts()
    sorted_len = sorted(all_texts.keys())
    with open(sorted_full_path, 'w', encoding = 'utf-8') as file_to_write:
        for i in sorted_len:
            file_to_write.write(all_texts[i]['name'] + '\n' + all_texts[i]['length'] + '\n' + all_texts[i]['text'] + '\n')
    return 'Sorted texts were written down.'

print(write_down_sorted_texts())