import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow

class EasyEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Змінна для зберігання поточної робочої директорії
        self.workdir = ""

        # Підключаємо сигнали до кнопок
        self.ui.btn_dir.clicked.connect(self.show_filenames_list)
    

    """
    Фільтрує файли в заданій директорії за розширенням (png, jpg etc).
    """
    def filter(self, files, extensions):
        # Дописати код (видалити pass)
        result = []
        for filename in files:
            for ext in extensions:
                if filename.endswith(ext):
                    result.append(filename)
        return result

        
    
    """
    Відкриває діалог вибору директорії та зберігає її шлях.
    """
    def choose_workdir(self):
        # Дописати код (видалити pass)
        self.workdir = QFileDialog.getExistingDirectory(self, "Обрати папку")
        
    """
    Показує список зображень в обраній директорії.
    """
    def show_filenames_list(self):
        # Дописати код (видалити pass)
        extension = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        self.choose_workdir()
        if self.workdir:
            filenames = self.filter(os.listdir(self.workdir), extension )
            self.ui.lw_files.clear()
            self.ui.lw_files.addItems(filenames)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = EasyEditor()
    main_window.show()
    sys.exit(app.exec())

class ImageProcesor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modifiled/"