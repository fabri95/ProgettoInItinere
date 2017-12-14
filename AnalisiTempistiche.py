#NOME:Fabrizio
#COGNOME:Bruno
#MATRICOLA:0240586




from AlberoBinarioRicercaLazyDeletion import ABRLD      #ARBLD sta per albero di ricerca binaria con lazy deletion
from time import time






def provaAlbero(passi):
    """Misuro i tempi delle varie operazioni passo dopo passo"""

    albero=ARBLD()
    inzio=start()
    for i in range(passi):

        albero.inserisci(2*i,i)
    tempoImpiegato=inzio-start()
    print('Tempo teorico:O(h)')                     #h è la profondità dell'albero
    print('Tempo calcolato:'tempoImpiegato/passi)



    inizio=start()
    for i in range(passi):

        albero.cerca(2*i)
    tempoImpiegato=inizio-start()
    print('Tempo teorico:O(h)')
    print('Tempo calcolato:' tempoImpiegato/passi)


    inizio=start()
    for i in range(passi):

        albero.boolDelete(2*i)

    tempoImpiegato=inizio-start()
    print('Tempo teorico:O(h)')
    print('Tempo calcolato:' tempoImpiegato/passi)




if __name__=="__main__"                            #test con input di 450 passi
    passi=450
    provaAlbero(passi)
