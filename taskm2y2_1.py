class Wiget():
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def print_info(self):
        print('Надпис:', self.text)
        print("Розташування:", self.x, self.y)

class Button(Wiget):
    def __init__(self, text, x, y, is_clicked):
        super(). __init__(text, x, y)
        self.is_clacked = is_clicked

    def click(self):
        self.is_clacked = True
        print("you are singet up")

button = Button("Брати участь", 100, 100, False)
button.print_info()
answer = input("Бажаєте зареструватися? (так/ні):")
if answer == "так":
    button.click()
else:
    print("Шкода(")