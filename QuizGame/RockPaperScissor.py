import random

list1 = ["rock","paper","scissor"]


while True:
    try:
        is_play = input('Do you want to play? say yes or no and quit for Quit: \n')
    except:
        print('invalid input')
        continue
    else:
        if is_play.lower() == 'no':
            print('Better mood for next time!')
            quit()
        elif is_play.lower() == 'quit':
            quit()
        elif is_play.lower() == 'yes':
            print('Lets Go!')

            while True:
                try:
                    userinput = input("please select among Rock,Paper,Scissor!")
                except:
                    print('Invalid Input!')
                    continue
                else:
                    if userinput.lower() in ['rock','paper','scissor']:
                        computer_guess = random.randint(0,2)
                        print(userinput)
                        print(list1[computer_guess])

                        if userinput == list1[computer_guess]:
                            continue
                        
                        if (userinput == 'rock' and list1[computer_guess] == 'scissor'):
                            print('user win!')
                            break
                        if (userinput == 'rock' and list1[computer_guess] == 'paper'):
                            print('computer win!')
                            break
                        if (userinput == 'paper' and list1[computer_guess] == 'rock'):
                            print('user win!')
                            break
                        if (userinput == 'paper' and list1[computer_guess] == 'scissor'):
                            print('computer win!')
                            break
                        if (userinput == 'scissor' and list1[computer_guess] == 'rock'):
                            print('user win!')
                            break
                        if (userinput == 'scissor' and list1[computer_guess] == 'paper'):
                            print('computer win!')
                            break      
                                                                                                                                                          
        else:
            print('Invalid input!')
            continue