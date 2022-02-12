# def func(n):
#     return int(str(n)) + int(str(n)*2) + int(str(n)*3)
#
# print(func(input('Введите цифру: ')), ' - n + nn + nnn')

# class Car:
# #     pass
# # car_object = Car()
# # print(dir(Car))
# #
# # class Car:
# #     color = 'grey'
# #     def turn_on(self):
# #         pass
# #     def call(self):
# #         pass
# # car_object = Car()
# # print(dir(Car))
# #____________________
#
#     #статические поля (переменные класса)
#     default_color = 'Grey'
#     default_weight = 5000
#
#     def __init__(self, color, model):
#         #динамические поля (переменные объекта)
#         self.color = color
#         self.model = model
#
#     def turn_on(self):
#         pass
#
#     def info(self):
#         print(self.color, self.model)
#
# car_obj_1 = Car('blue', 'BMW')
# car_obj_2 = Car('red', 'BMW2')
# car_obj_1.turn_on()
# print(car_obj_1.color)
# print(car_obj_1.model)
# car_obj_1.info()
# car_obj_2.info()

class Car:
    def __init__(self, color, type, year, on, off):
        self.color = color
        self.type = type
        self.year = year
        self.on = on
        self.off = off
car_1 = Car('green', 'BMW', 2021, 'Автомобиль заведен', 'Автомобиль заглушен')
car_2 = Car('blue', 'Mercedes', 2017, 'Автомобиль заведен', 'Автомобиль заглушен')
print(car_1.on)
print(car_1.off)
print(car_1.year)
print(car_1.type)
print(car_1.color)