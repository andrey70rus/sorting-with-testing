import sys
import interface
from PyQt5 import QtWidgets


# интерфейс, функционал окна
class ExampleApp(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.sort_button.released.connect(self.sort)
        self.clear_button.released.connect(self.clear)
        self.plainTextEdit.setToolTip('Введите метки объектов через запятую/пробел/без разделителя')
        self.lineEdit.setToolTip('Введите порядок сортировки через запятую/пробел/без разделителя')

    def clear(self):
        # очистка полей по кнопке
        self.plainTextEdit.setPlainText('')
        self.plainTextEdit_2.setPlainText('')
        self.lineEdit.setText('')
        self.statusbar.showMessage('')

    def sort(self):
        # очищаем поле результата и статусбара
        self.plainTextEdit_2.setPlainText('')
        self.statusbar.showMessage('')

        # забираем строки из интерфейса
        str_objects = self.plainTextEdit.toPlainText()
        str_rule = self.lineEdit.text()

        # получаем результат функции
        error_main, text_main = main(str_objects, str_rule)
        if error_main == 0:
            # превращаем кортеж в строку, удаляем "лишнее" в строке
            str_result = str(text_main)
            str_result = str_result.replace("'", "")
            str_result = str_result.replace("[", "")
            str_result = str_result.replace("]", "")
            str_result = str_result.replace(",", " ")

            # возвращаем результат
            self.plainTextEdit_2.setPlainText(str_result)

        if error_main == 1:
            # записываем ошибку в статусбар
            self.statusbar.showMessage(text_main)

# основная функция, на входе две str
def main(str_objects, str_rule):
    error = 0

    # удаляем разделители из входной строки
    str_objects = str_objects.replace(',', '')
    str_objects = str_objects.replace(' ', '')
    str_rule = str_rule.replace(',', '')
    str_rule = str_rule.replace(' ', '')

    # получаем все буквы (isalpha()) из введенной строки объектов
    list_objects = []
    for letter in str_objects:
        if letter.isalpha():
            list_objects.append(letter)

    # получаем все буквы (isalpha()) из введенной строки правила сортировки, присваиваем порядковый номер
    dict_rule = {}
    i = 1
    for letter in str_rule:
        if letter.isalpha():
            dict_rule[letter] = i
            i += 1

    # проверки корректности ввода
    if str_objects == '' or str_rule == '':
        error = 1
        return error, 'Заполните поля "1" и "2"'

    # если в метках объектов кроме букв, есть другие символы (не считая разделителей) - уведомление
    elif str_objects.isalpha() == 0:
        error = 1
        return error, 'Введите буквенные метки объектов в поле "1"!'

    # если в правиле кроме букв, есть другие символы (не считая разделителей) - уведомление
    elif str_rule.isalpha() == 0:
        error = 1
        return error, 'Введите буквенные метки объектов в поле "2"!'

    # если правило не содержит все объекты - уведомление
    elif set(list_objects) != dict_rule.keys():
        error = 1
        return error, '"Порядок сортировки" должен содержать одну метку каждого типа!'

    # если дублируются буквы в правиле - уведомление
    elif len(dict_rule.keys()) != len(str_rule):
        error = 1
        return error, 'Проверьте "порядок сортировки"! (метки не должны повторяться)'

    if error == 0:
        # сортировка, i - шаг сортировки, j - номер перемещаемого объекта в list_objects
        for i in range(0, len(list_objects)):
            for j in range(len(list_objects) - 1, 0, -1):
                if dict_rule[list_objects[j]] < dict_rule[list_objects[j - 1]]:
                    list_objects[j], list_objects[j - 1] = list_objects[j - 1], list_objects[j]
        return error, list_objects

# запуск интерфейса
if __name__ == '__main__':
    # Дизайн
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
