import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QMessageBox
)

class LoginWindow(QWidget):
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 200)  # Ancho, Alto

        # Layout
        layout = QVBoxLayout()

        # Mensaje de bienvenida
        welcome_message = QLabel("Estás intentando acceder al panel de control de Ozaru Bot!")
        welcome_message.setStyleSheet("font-size: 10px; text-align: center;")
        layout.addWidget(welcome_message)

        # Etiqueta y campo de contraseña
        password_label = QLabel("CONTRASEÑA:")
        password_label.setStyleSheet("font-size: 16px; text-align: center;")
        layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  # Ocultar texto de contraseña
        layout.addWidget(self.password_input)

        # Botón de inicio de sesión
        login_button = QPushButton("Iniciar Sesión")
        login_button.clicked.connect(self.check_password)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def check_password(self):
        # Comprobar contraseña
        if self.password_input.text() == "elnegro12345sexo":
            self.on_login_success()
            self.close()  # Cerrar ventana de inicio de sesión
        else:
            QMessageBox.critical(self, "Error", "Dashboard cerrada, contraseña incorrecta")


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard de Ozaru Bot")
        self.setGeometry(100, 100, 800, 600)  # Ancho, Alto

        # Agregar un título
        title = QLabel("Bienvenido al Dashboard de Ozaru Bot")
        title.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        self.setCentralWidget(title)  # Usar QLabel como contenido central por simplicidad

def main():
    app = QApplication(sys.argv)

    # Crear la ventana de inicio de sesión
    def on_login_success():
        dashboard = Dashboard()
        dashboard.show()

    login_window = LoginWindow(on_login_success)
    login_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
