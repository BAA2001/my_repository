# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + ' ' + str(goal_0), scorer_1 + ' ' + str(goal_1)

report = f'{scorer_0} scored in the {goal_0}nd minute \n{scorer_1} scored in the {goal_1}th minute'

player = 'Igor Belanov'
first_name = player[:player.find(' ')]
last_name = player[player.find(' '):]

last_name = last_name.replace(' ', '')

last_name_length = len(last_name)

name_short = player[0] + '.' + ' ' + last_name

chant = (first_name + '!' + ' ') * (len(first_name)-1) + (first_name + '!')
good_chant = chant[-1] != ' '
