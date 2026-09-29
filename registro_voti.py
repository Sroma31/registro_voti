class RegistroVoti:
    def __init__(self):
        self.voti = []

    def aggiungi_voto(self, voto: float):
        if 0 <= voto <= 10:
            self.voti.append(voto)
        else:
            print("Voto non valido!")

    def media(self) -> float:
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)

if __name__ == "__main__":
    registro = RegistroVoti()
    registro.aggiungi_voto(8.5)
    registro.aggiungi_voto(7.0)
    print("Voti inseriti:", registro.voti)
    print("Media voti:", registro.media())