import keyboard
import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z', ' ']

subject = ['Tina', 'Kamran', 'She']
verb = ['went home', 'is', 'picked']
obj = ['shopping', 'happy', 'yellow flower']

a = random.choice(subject)
b = random.choice(verb)
c = random.choice(obj)

random_sentence = a + ' ' + b + ' ' + c

result1 = {}
result2 = {}

print(random_sentence)
print(' ')

while True:
    keyboard.block_key('backspace')
    user_input = input('Type the above sentence:  ')
    print(' ')

    for r in random_sentence:
        if r in alphabet:
            result1[r] = alphabet.index(r)  

    index_random = set(result1)
    print(result1)

    for u in user_input:
        if u in alphabet:
            result2[u] = alphabet.index(u)

    index_user = set(result2)
    print(result2)

    for p in result2 and result1:
        if (p in result1) == (p in result2):
            continue
        else:
            print(' ')
            print('Error ', p, ' at index: ', random_sentence.index(p))

    print(' ')
    if index_random == index_user:
        print('Both sentences are identical')
    else:
        print('Sentences are not identical')
    break
