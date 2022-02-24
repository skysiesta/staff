from solution import *

print('\nЧтение заданных параметров для машины\n')

car = Car('\nBugatti Veyron', 'bugatti.png', '0.312', '2')
print(car.car_type, car.brand, car.photo_file_name, car.carrying,
car.passenger_seats_count, sep='\n')

print('\nЧтение заданных параметров для трака + вычисление длины, ширины трака\n')

truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length,
truck.body_width, truck.body_height, sep='\n')

print('\nЗапись .csv файла с заданными параметрами для таблицы\n')

spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs\n')
print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying,
spec_machine.photo_file_name, spec_machine.extra, sep='\n')

print('\nЧтение расширения файла, прикрепленного к таблице')

spec_machine.get_photo_file_ext()

print('\nОпределение количества столбцов, исключая пусты столбцы и одинаковые\n')

cars = get_car_list('cars.csv')
len(cars)

print('\nОпределение типов для атрибутов класса\n')

for car in cars:
     print(type(car))
