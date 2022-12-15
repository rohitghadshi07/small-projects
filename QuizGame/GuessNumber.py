import random
guess= 0
while True:
    try:
        guess_a_number = int(input('Enter a number in between 1 to 5: \n'))
    except:
        print('invalid input!')
        continue
    else:
        random_integer = random.randint(1,5)
        if guess_a_number == random_integer:
            print("correct!")
            break
        else:
            print("Incorrect!")
            print(f"random Integer was {random_integer}")
            guess+=1
            continue
print(f'you got it {guess} guesses.')
