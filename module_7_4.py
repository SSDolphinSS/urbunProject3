team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score1 > score2 or score1 == score2 and tasks_total > team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
elif score1 < score2 or score1 == score2 and tasks_total < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья'
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s '
      'и %s !' % (team1_num, team2_num))
print('Команда Волшебники данных решила задач: {score} !'.format(score=score2))
print('Волшебники данных решили задачи за {time} с !'.format(time=team1_time))
print(f'Команды решили {score1} и {score2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
