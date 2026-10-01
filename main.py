import RegistroVoti
import registro_classe_voti



registro = RegistroVoti()
registro.aggiungi_voto(8.5)
registro.aggiungi_voto(7.0)

registroclasse= registro_classe_voti()
registroclasse.aggiungi_voto(8.5)
registroclasse.aggiungi_voto(7.0)

print("Voti inseriti:", registro.voti)
print("Media voti:", registro.media())
print("Esito:", registro.esito())

print("Voti inseriti:", registroclasse.registro.voti)
print("Media voti:", registroclasse.media())
print("Esito:", registroclasse.esito())