import csv, re, os

# ОСНОВНОЙ КЛАСС
class CarBase:

    def __init__(self, photo_file_name):
        path = 'f4'

        root_ext = os.path.splitext(path)

        return path

    # ПОЛУЧИТЬ РАСШИРЕНИЕ ФАЙЛА
    def get_photo_file_ext(file):
        path = 'f3.jpeg'

        root_ext = os.path.splitext(path)[1]

        print(root_ext)

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):

        with open('cars_2.csv', 'w', encoding='UTF8') as f:

            # ЗАПИСЬ ТАБЛИЦЫ
            writer = csv.writer(f)

            try:
                # ДЕФОЛТНЫЕ ОПРЕДЕЛЕНИЯ, БРЕНД, ТИП МАШИНЫ И Т.Д.
                default = ['car_type', 'brand', 'passenger_seats_count', 'photo_file_name', 'body_whl', 'carrying', 'extra']
                writer.writerow(default)
                data = [brand, photo_file_name, carrying, passenger_seats_count]
                writer.writerow(data)
            except NameError as e:
                word = re.findall("name '(\w+)' is not defined",str(e))[0]
                data = [brand, photo_file_name, carrying, passenger_seats_count]
                data = data.replace(word, ' ')
                writer.writerow(data)

            for word in data:
                if brand in word:
                    self.brand = word
                elif photo_file_name in word:
                    self.photo_file_name = word
                elif carrying in word:
                    self.carrying = float(word)
                elif passenger_seats_count in word:
                    self.passenger_seats_count = int(word)

                self.car_type = 'car'

    def car_type():
        return self.car_type
    def brand():
        return self.brand
    def photo_file_name():
        return self.photo_file_name
    def carrying():
        return self.carrying
    def passenger_seats_count():
        return self.passenger_seats_count

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, passenger_seats_count, body_whl, carrying = None, extra = None):
        with open('cars_2.csv', 'w', encoding='UTF8') as f:

            writer = csv.writer(f)

            try:
                default = ['car_type', 'brand', 'passenger_seats_count', 'photo_file_name', 'body_whl', 'carrying', 'extra']
                writer.writerow(default)
                data = [brand, photo_file_name, passenger_seats_count, body_whl]
                writer.writerow(data)
            except NameError as e:
                word = re.findall("name '(\w+)' is not defined",str(e))[0]
                data = [brand, photo_file_name, passenger_seats_count, carrying, body_whl]
                data = data.replace(word, ' ')
                writer.writerow(data)

            whl = data[-1].split('x')
            self.body_length = whl[0]
            self.body_width = whl[1]
            self.body_height = whl[2]
            # print(whl)

            for word in data:
                if brand in word:
                    self.brand = word
                elif photo_file_name in word:
                    self.photo_file_name = word
                elif passenger_seats_count in word:
                    self.passenger_seats_count = word
                elif body_whl in word:
                    self.body_whl = word
                elif carrying in word:
                    self.carrying = float(word)
                elif extra in word:
                    self.extra = word

                self.car_type = 'truck'

    def car_type():
        return self.car_type
    def brand():
        return self.brand
    def photo_file_name():
        return self.photo_file_name
    def body_length():
        return self.body_length
    def body_width():
        return self.body_width
    def body_height():
        return self.body_height
    def passenger_seats_count():
        return self.passenger_seats_count
    def carrying():
        return self.carrying
    def extra():
        return self.extra


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        with open('cars_2.csv', 'w', encoding='UTF8') as f:

            writer = csv.writer(f)

            try:
                default = ['car_type', 'brand', 'passenger_seats_count', 'photo_file_name', 'body_whl', 'carrying', 'extra']
                writer.writerow(default)
                data = [brand, photo_file_name, carrying, carrying, extra]
                writer.writerow(data)
            except NameError as e:
                word = re.findall("name '(\w+)' is not defined",str(e))[0]
                data = [brand, photo_file_name, carrying, carrying, extra]
                data = data.replace(word, ' ')
                writer.writerow(data)

            for word in data:
                if brand in word:
                    self.brand = word
                elif photo_file_name in word:
                    self.photo_file_name = word
                elif carrying in word:
                    self.carrying = word
                elif extra in word:
                    self.extra = extra
                elif passenger_seats_count in word:
                    self.passenger_seats_count = word

                self.car_type = 'spec_machine'

    def car_type():
        return self.car_type
    def brand():
        return self.brand
    def photo_file_name():
        return self.photo_file_name
    def carrying():
        return self.carrying
    def extra():
        if self.extra:
            pass
        else:
            other = ''
            other = self.extra
        return self.extra
    def passenger_seats_count():
        return self.passenger_seats_count

# ПОЛУЧИТЬ СПИСОК МАШИН
def get_car_list(csv_filename):
    car_list = []
    # ЧТЕНИЕ ФАЙЛА
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            if not row:
                pass
            elif all('' == s or s.isspace() for s in row):
                pass
            elif row[1] in ''.join(str(e) for e in car_list):
                pass
            else:
                # print()
                row = row[0:]
                car_list.append(row)
                if row[0] == 'car':
                    row[0] = Car
                elif row[0] == 'truck':
                    row[0] == Truck
                elif row[0] == 'spec_machine':
                    row[0] = SpecMachine
    # print(len(car_list))
    # print(car_list)

    return car_list
