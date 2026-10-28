from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
    def registrar_entrada(self):
        cpf = "".join(c for c in self.campo_cpf.text() if c.isdigit())
        nome = " ".join(self.campo_nome.text().split())

        if len(cpf) != 11:
            self.mensagem.setText("O CPF precisa ter 11 dígitos.")
            self.campo_cpf.setFocus()
            return
        if not nome:
            self.mensagem.setText("Informe o nome do visitante.")
            self.campo_nome.setFocus()
            return
        if self.combo_setor.currentIndex() == 0:
            self.mensagem.setText("Selecione o setor de destino.")
            return

        setor = self.combo_setor.currentText()
        self.mensagem.setText(f"Dados válidos: {nome} para {setor}. Ainda não gravamos nada.")

    def limpar_campos(self):
        self.campo_cpf.clear()
        self.campo_nome.clear()
        self.combo_setor.setCurrentIndex(0)
        self.campo_cpf.setFocus()
        
        self.setWindowTitle("Portaria Digital")
        self.resize(820, 520)

        titulo = QLabel("Recepção: controle de visitantes")

        layout = QVBoxLayout()
        layout.addWidget(titulo)
        self.setLayout(layout)

        # ---------- eventos: sinal.connect(slot) ----------
        self.botao_entrada.clicked.connect(self.registrar_entrada)
        self.botao_limpar.clicked.connect(self.limpar_campos)