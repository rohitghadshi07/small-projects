isPlaying  = input('Do you want to play? say yes or no \n')
score = 0

if isPlaying.lower() == 'yes':

    print('Lets Go!')
    question1 = input('what is CPU stands for? \n')
    answer1 = 'central processing unit'
    if question1.lower() == answer1:
        print('Correct!')
        score +=2
        print(f'your scored is: {score}/10')
    else:
        print('Incorrect!')
        score -=1
        print(f'your scored is: {score}/10')

    question2 = input('Name the National animal of India? \n')
    answer2 = 'tiger'
    if question2.lower() == answer2:
        print('Correct!')
        score +=2
        print(f'your scored is: {score}/10')
    else:
        print('Incorrect!')
        score -=1
        print(f'your scored is: {score}/10')

    question1 = input('Name the densest jungle in the world? \n')
    answer1 = 'amazon rainforest'
    if question1.lower() == answer1:
        print('Correct!')
        score +=2
        print(f'your scored is: {score}/10')
    else:
        print('Incorrect!')
        score -=1
        print(f'your scored is: {score}/10')

    question1 = input('Which festival is known as the festival of light? \n')
    answer1 = 'diwali'
    if question1.lower() == answer1:
        print('Correct!')
        score +=2
        print(f'your scored is: {score}/10')
    else:
        print('Incorrect!')
        score -=1
        print(f'your scored is: {score}/10')

    question1 = input('Name the National bird of India? \n')
    answer1 = 'peacock'
    if question1.lower() == answer1:
        print('Correct!')
        score +=2
    else:
        print('Incorrect!')
        score -=1
    print(f'your scored is: {score}/10')
    percentage = score/10*100
    print(f'you got ({int(percentage)})%')

elif isPlaying.lower() == 'no':
    print('Ok! Come back once your mood on!')
    quit()
else:
    print('Invalid answer')
    
    