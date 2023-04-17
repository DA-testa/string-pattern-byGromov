# python3
# Author: Aleksandrs Pučenkins 17.gr. 221RDB335

B = 13

def get_hash(text: str) -> int:
    text_len = len(text)

    hash = 0

    for i in range(text_len):
        hash += ord(text[i]) * B**(text_len - i) 
    return hash

def read_input():
    inputType = input()

    while 'I' not in inputType or 'F' not in inputType:
        if 'I' in inputType:
            return (input().rstrip(), input().rsstrip())
        elif 'F' in inputType:
            with open("./tests/06", "r") as file:
                return(file.readline().rstrip(), file.readline().rstrip())
        inputType = input()

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