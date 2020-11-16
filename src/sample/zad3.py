class Planets:
    def __init__(self):
        self.result = None
        self.planets = [['Merkury', 0.2408467],
                        ['Wenus', 0.61519726],
                        ['Mars', 1.8808158],
                        ['Jowisz', 11.862615],
                        ['Saturn', 29.447498],
                        ['Uran', 84.016846],
                        ['Neptun', 164.79132],
                        ['Ziemia', 31557600]]

    def game(self, num, name):
        if isinstance(num, int) and isinstance(name, str):
            if num >= 1:
                for i in range(0, len(self.planets), 1):
                    if name == self.planets[i][0]:
                        self.result = int(num) / self.planets[i][1]
                        break
                    else:
                        if i == 7:
                            raise Exception("Error")
                if name != "Ziemia":
                    self.result = self.result / self.planets[7][1]

                return round(self.result, 2)
            else:
                raise Exception("Error")
        else:
            raise Exception("Error")
