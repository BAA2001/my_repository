# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, time_of_day, cow_milking_status, cow_location, season, slurry_tank, grass_status):
    if weather == 'rainy' and time_of_day == 'night'and cow_location == 'pasture':
        print('take cows to cowshed')
    if cow_location == 'cowshed' and weather == 'sunny' or weather =='windy':
        print('milk cows')
    if cow_location == 'cowshed' and weather == 'rainy' or weather == 'neutral' and slurry_tank == True:
        print('fertilize pasture')
    if cow_location == 'cowshed' and weather == 'sunny' and grass_status == True and season == 'spring':
        print('mow grass')
    else:
        print('wait')

farm_action(weather='nvm', time_of_day='nvm', cow_milking_status="nvm" , cow_location='nvm', season='nvm',slurry_tank= 'nvm' , grass_status = 'nvm')

example_list_a = [1, 2, 3]
example_list_b = [3, 2, 1]
if example_list_a == example_list_b:
    print(True)
else:
    print(False)