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

    def esito(self) -> str:
        media_voti = self.media()
        if media_voti >= 6:
            return "Promosso"
        else:
            return "Bocciato"
        #i love niggers






