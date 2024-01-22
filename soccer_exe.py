#This exercise is used to find out how much time has expired, or whether it was a draw in a game

team1 = input('First team name: ')
team2 = input('Second team name: ')

goals_team1 = input(f'how many goals did {team1} score? ')
goals_team2 = input(f'how many goals did {team2} score? ')

if goals_team1 > goals_team2:
    print(team1, 'is the winner!')
elif goals_team2 > goals_team1:
    print(team2, 'is the winner!')
else:
    print('Draw')
