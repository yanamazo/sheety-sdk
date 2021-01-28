from sheety import SheetyManager


sheety = SheetyManager(
    url='https://api.sheety.co/*********/myWorkouts/workouts',
    auth_method='bearer',
    token='123')
    
print(sheety.get_data())
print(sheety.add_data(exercise='Python Coding', duration='60'))
