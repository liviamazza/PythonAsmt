#This program is a Inventros quiz

score = 0

#Instructions
print('Welcome to the inventors quiz')
print ('instructions')
print('Every questions has 1 point \nFinal score will be given at the end of the quiz') 

#Asking Questions
print('q1.Who invented the Cellphone')
print ('Options \nMartin Cooper\nThomas Edison\nMarie Currie')
ans= input ('Enter your answer : ')
if ans == 'Martin Cooper':
    print ('Correct ')
    score = score+1
else:
    print ( 'Incorrect')

print ('-------------')
print('q2. Who invented the Lightbulb')
print ('Options \nAlbert Einsten\nSantos Dumont\nThomas Edison')
ans= input ('Enter your answer :' )
if ans == 'Thomas Edison':
    print ('Correct ')
    score = score+1
else:
    print ( 'Incorrect')

                
print ('-------------')
print('q3.Who invented the Airplane')
print ('Options \nMartin Cooper\nTim Bernes-Lee\nSantos Dumont')
ans= input ('Enter your answer :' )
if ans == 'Santos Dumont':
    print ('Correct ')
    score = score+1
else:
    print ( 'Incorrect')



print ('-----------')
final_score = score
print(f'your final score is {score}')



       
       
