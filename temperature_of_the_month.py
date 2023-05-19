class NyCityWeather():
    def __init__(self):
        self.jan = []

    def average_of_temp(self, jan, mes):
    # idx = index \\ key = info completa en la list \\ jan[idx][0] = claves \\ jan[idx][1] = valores
        self.str_jan = []
        for index, keys in enumerate(jan):
            self.str_jan.append(jan[index][0])
            index_mes = mes - 1
            if index == index_mes:
                jan[index_mes][0]
                break

        for idx, key in enumerate(jan):
            self.jan.append(jan[idx][1])
            if jan[idx][0] == jan[index_mes][0]:
                operacion = sum(self.jan) // mes
                print(f"la temperatura promedio en la primera semana era de: {operacion}ºF")
                break

    def maximum_temperature(self, jan, day):
    # idx = index \\ key = info completa en la list \\ jan[idx][0] = claves \\ jan[idx][1] = valores
        self.day_jan = []
        for index, keys in enumerate(jan):
            self.day_jan.append(jan[index][0])
            index_mes = day - 1
            if index == index_mes:
                jan[index_mes][0]
                break

        self.temp_list = []
        for idx, key in enumerate(jan):
            self.temp_list.append(jan[idx][1])
            if jan[idx][0] == jan[index_mes][0]:
                max_temp = max(self.temp_list)
                
        if day > 1:
            print(f"la temperatura maxima de los primeros {day} dias es de {max_temp}ºF")
        else:
            print(f"la temperatura maxima del dia {day} es: {max_temp}ºF")

'''
temp = {
    "jan 1":27,
    "jan 2":31,
    "jan 3":23,
    "jan 4":34,
    "jan 5":37,
    "jan 6":38,
    "jan 7":29,
    "jan 8":30,
    "jan 9":35,
    "jan 10":30}
'''
temp = [
    ["jan 1",27],
    ["jan 2",31],
    ["jan 3",23],
    ["jan 4",34],
    ["jan 5",37],
    ["jan 6",38],
    ["jan 7",29],
    ["jan 8",30],
    ["jan 9",35],
    ["jan 10",30]]

t = NyCityWeather()
#t.average_of_temp(temp, 2)
t.maximum_temperature(temp, 1)




