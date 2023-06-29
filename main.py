import random

print('Hi this simple key generator')
how_many_keys = input('Write how many keys you need\n')

try:

    how_many_keys = int(how_many_keys)

    if isinstance(how_many_keys, int):
        print('here are your keys\n')

        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

        def rnd_4_block():
            ready_key = ''
            rnd_mass = []
            for i in range(10):
                count = random.randint(0,9)
                rnd_mass.append(count)
                letters_rnd = random.choice(letters)
                rnd_mass.append(letters_rnd)
            result = random.SystemRandom().sample(rnd_mass, 4)
            for element in result:
                element = str(element)
                ready_key = ready_key + element
            # return print(ready_key)
            return ready_key

        def rnd_7_block():
            ready_key = ''
            rnd_mass = []
            for i in range(10):
                count = random.randint(0,9)
                rnd_mass.append(count)
                letters_rnd = random.choice(letters)
                rnd_mass.append(letters_rnd)
            result = random.SystemRandom().sample(rnd_mass, 7)
            for element in result:
                element = str(element)
                ready_key = ready_key + element
            # return print(ready_key)
            return ready_key

        def key_code():
            ready_key = rnd_4_block() + '-' + rnd_7_block() + '-' + rnd_4_block()
            return ready_key

        for i in range(how_many_keys):
            print(key_code())
        
        print('\nDone')

except Exception as E:
    print('please write in numbers.')