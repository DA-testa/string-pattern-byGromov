# python3
# Author: Aleksandrs Pučenkins 17.gr. 221RDB335



def read_input():
    in_type = input()

    while 'I' not in in_type or 'F' not in in_type:
        if 'I' in in_type:
            return (input().rstrip(), input().rsstrip())
        elif 'F' in in_type:
            with open("./tests/06", "r") as file:
                return(file.readline().rstrip(), file.readline().rstrip())
        in_type = input()

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    pattern_len = len(pattern)
    pattern_hash = get_hash(pattern)
    text_len = len(text)

    occurrences = []
    for i in range(0, text_len - pattern_len + 1):
        text_part = text[i:i + pattern_len]
        text_part_hash = get_hash(text_part)

        if pattern_hash == text_part_hash:
            if pattern == text_part:
                occurrences.append(i)
    return occurrences 


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))