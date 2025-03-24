
 
print('Welcome to the quiz')

print ('Instructions:')

print('The final score will be given in the end of the quiz.')
score = 0

Qa = {'Cellphone': 'Martin Cooper',
      'Airplane': 'Alberto Santos Dumont',
      'Lightbulb': 'Thomas Edison',
      'Internet': 'Tim Berners-Lee'}

for k,v in Qa.items():
    user_ans=input(f'Who invented the {k}:')
    if user_ans==v:
        score+1
    else:
        print('incorrect')
        total_score==score
        print(total_score)
