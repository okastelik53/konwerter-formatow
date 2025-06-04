import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QMessageBox
)import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QMessageBox
)
from PyQt5.QtCore import QThread, pyqtSignal
import os
from Task2_read_json import read_json
from Task3_write_json import write_json
from Task4_read_yaml import read_yaml
from Task5_write_yaml import write_yaml
from Task6_read_xml import read_xml
from Task7_write_xml import write_xml

class ConverterThread(QThread):
    finished = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(self, input_path, output_path):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        try:
            ext_in = self.input_path.split('.')[-1].lower()
            ext_out = self.output_path.split('.')[-1].lower()

            if ext_in == "json":
                data = read_json(self.input_path)
            elif ext_in in ["yaml", "yml"]:
                data = read_yaml(self.input_path)
            elif ext_in == "xml":
                data = read_xml(self.input_path)
            else:
                raise Exception("Nieobsługiwany format wejściowy")

            if ext_out == "json":
                write_json(self.output_path, data)
            elif ext_out in ["yaml", "yml"]:
                write_yaml(self.output_path, data)
            elif ext_out == "xml":
                write_xml(self.output_path, data)
            else:
                raise Exception("Nieobsługiwany format wyjściowy")

            self.finished.emit("Konwersja zakończona!")
        except Exception as e:
            self.failed.emit(str(e))

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konwerter Plików (Wątkowy)")
        self.resize(300, 150)

        self.layout = QVBoxLayout()

        self.label = QLabel("Wybierz pliki")
        self.layout.addWidget(self.label)

        self.input_btn = QPushButton("Plik wejściowy")
        self.input_btn.clicked.connect(self.choose_input)
        self.layout.addWidget(self.input_btn)

        self.output_btn = QPushButton("Plik wyjściowy")
        self.output_btn.clicked.connect(self.choose_output)
        self.layout.addWidget(self.output_btn)

        self.convert_btn = QPushButton("Konwertuj")
        self.convert_btn.clicked.connect(self.convert)
        self.layout.addWidget(self.convert_btn)

        self.setLayout(self.layout)

        self.input_path = ""
        self.output_path = ""

    def choose_input(self):
        file, _ = QFileDialog.getOpenFileName(self, "Wybierz plik wejściowy")
        if file:
            self.input_path = file
            self.label.setText(f"Wejście: {os.path.basename(file)}")

    def choose_output(self):
        file, _ = QFileDialog.getSaveFileName(self, "Zapisz jako")
        if file:
            self.output_path = file
            self.label.setText(f"Wyjście: {os.path.basename(file)}")

    def convert(self):
        if not self.input_path or not self.output_path:
            QMessageBox.warning(self, "Brak plików", "Musisz wybrać oba pliki.")
            return

        self.thread = ConverterThread(self.input_path, self.output_path)
        self.thread.finished.connect(lambda msg: QMessageBox.information(self, "Sukces", msg))
        self.thread.failed.connect(lambda err: QMessageBox.critical(self, "Błąd", err))
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())

from PyQt5.QtCore import QThread, pyqtSignal
import os
from Task2_read_json import read_json
from Task3_write_json import write_json
from Task4_read_yaml import read_yaml
from Task5_write_yaml import write_yaml
from Task6_read_xml import read_xml
from Task7_write_xml import write_xml

class ConverterThread(QThread):
    finished = pyqtSignal(str)
    failed = pyqtSignal(str)

    def __init__(self, input_path, output_path):
        super().__init__()
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        try:
            ext_in = self.input_path.split('.')[-1].lower()
            ext_out = self.output_path.split('.')[-1].lower()

            if ext_in == "json":
                data = read_json(self.input_path)
            elif ext_in in ["yaml", "yml"]:
                data = read_yaml(self.input_path)
            elif ext_in == "xml":
                data = read_xml(self.input_path)
            else:
                raise Exception("Nieobsługiwany format wejściowy")

            if ext_out == "json":
                write_json(self.output_path, data)
            elif ext_out in ["yaml", "yml"]:
                write_yaml(self.output_path, data)
            elif ext_out == "xml":
                write_xml(self.output_path, data)
            else:
                raise Exception("Nieobsługiwany format wyjściowy")

            self.finished.emit("Konwersja zakończona!")
        except Exception as e:
            self.failed.emit(str(e))

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konwerter Plików (Wątkowy)")
        self.resize(300, 150)

        self.layout = QVBoxLayout()

        self.label = QLabel("Wybierz pliki")
        self.layout.addWidget(self.label)

        self.input_btn = QPushButton("Plik wejściowy")
        self.input_btn.clicked.connect(self.choose_input)
        self.layout.addWidget(self.input_btn)

        self.output_btn = QPushButton("Plik wyjściowy")
        self.output_btn.clicked.connect(self.choose_output)
        self.layout.addWidget(self.output_btn)

        self.convert_btn = QPushButton("Konwertuj")
        self.convert_btn.clicked.connect(self.convert)
        self.layout.addWidget(self.convert_btn)

        self.setLayout(self.layout)

        self.input_path = ""
        self.output_path = ""

    def choose_input(self):
        file, _ = QFileDialog.getOpenFileName(self, "Wybierz plik wejściowy")
        if file:
            self.input_path = file
            self.label.setText(f"Wejście: {os.path.basename(file)}")

    def choose_output(self):
        file, _ = QFileDialog.getSaveFileName(self, "Zapisz jako")
        if file:
            self.output_path = file
            self.label.setText(f"Wyjście: {os.path.basename(file)}")

    def convert(self):
        if not self.input_path or not self.output_path:
            QMessageBox.warning(self, "Brak plików", "Musisz wybrać oba pliki.")
            return

        self.thread = ConverterThread(self.input_path, self.output_path)
        self.thread.finished.connect(lambda msg: QMessageBox.information(self, "Sukces", msg))
        self.thread.failed.connect(lambda err: QMessageBox.critical(self, "Błąd", err))
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec_())
