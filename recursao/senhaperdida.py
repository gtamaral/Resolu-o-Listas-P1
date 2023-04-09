# definindo todas as funcoes necessarias 
def apply_mod_11(_number):
    return _number % 11

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def generate_fibonacci_sequence(_range):
    sequence = []
    for index in range(_range):
        sequence.append(fibonacci(index))

    return sequence


def cal_fatorial(_number):
    if _number == 0:
        return 1
    else:
        return _number * cal_fatorial(_number - 1)


def generate_fatorial_sequence(_range):
    sequence = []
    for index in range(_range):
        sequence.append(cal_fatorial(index))

    return sequence


def add_lists(_listA, _listB):
    response = []
    for index in range(len(_listA)):
        response.append(_listA[index] + _listB[index])

    return response


def multiply_lists(_listA, _listB):
    response = []
    for index in range(len(_listA)):
        response.append(_listA[index] * _listB[index])

    return response


def cal_minimum_mod_26(_number):
    if _number < 26:
        return _number;
    else:
        return cal_minimum_mod_26(_number % 26)


def convert_numbers_to_word(_listNumbers):
    response = []
    for number in _listNumbers:
        response.append(ALPHABET[cal_minimum_mod_26(number)])

    separator = ''
    return separator.join(response)
#  ///////////////////////////////////////////////////

# recebendo os inputs da questao
password = input()
number_words = int(input())
words = []
for i in range(number_words):
    words.append(input())

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

possible_passwords = []
# criando um for pra pecorrer cada palavra na minha lista words
for word in words:
    compare_array_password = []
    #  outro for pra pecorrer cada letra da palavra
    for letter in word:
        index_mod_11 = apply_mod_11(ALPHABET.index(letter))
        if index_mod_11 != 0:
            sequence_fibonacci = generate_fibonacci_sequence(index_mod_11)
            sequence_fatorial = generate_fatorial_sequence(index_mod_11)

            if index_mod_11 % 2 == 0:
                sequence_numbers_word = add_lists(sequence_fibonacci, sequence_fatorial)
            else:
                sequence_numbers_word = multiply_lists(sequence_fibonacci, sequence_fatorial)

            compare_array_password.append(convert_numbers_to_word(sequence_numbers_word))
        else:
            compare_array_password.append("1")

    separator = ''
    possible_passwords.append(separator.join(compare_array_password))

# output
if password in possible_passwords:
    print('Achamos! Achamos a senha.')
else:
    print('É... Temos que procurar mais')