# This program uses Easygui to construct a Quiz Program
from easygui import*
score = 0
msgbox(f'Welcome to Inventors Quiz\nEach correct answer has 1 point\nTotal score is shown at the end')

# User details
name = enterbox('Enter your name : ')
yr_level = integerbox('Enter your year level : ')

# Asking user if they want to proceed to quiz.
choice = buttonbox('Do you want to play quiz?', choices = ['Yes', 'No'])
if choice == 'Yes':
    msgbox('Welcome to the Inventors Quiz')

    q1 = buttonbox('What Martin Cooper has developed?', choices = ['Lightning', 'Cellphone', 'Optics'])
    if q1 == 'Cellphone':
        msgbox('Correct!')
        score = score+1
    else:
        msgbox('Incorrect')

    q2 = buttonbox('What Nikolas Tesla has developed?', choices = ['Eletrecity', 'Photography', 'Eletric motor'])
    if q2 == 'Eletric motor':
        msgbox('Correct!')
        score =score+1
    else:
            msgbox('Incorrect')

    q3 = buttonbox('What Thomas Edison has developed?', choices = ['Pulley', 'Bulbs', 'Radio'])
    if q3 == 'Bulbs':
        msgbox('Correct!')
        score = score+1
    else:
        msgbox ('Incorrect')



    msgbox(f'Your total score is {score}')

else:
    msgbox('Thank you. Try again')
