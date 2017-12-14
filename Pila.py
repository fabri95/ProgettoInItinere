#NOME: Fabrizio
#COGNOME:Bruno
#MATRICOLA:0240586








class PilaArrayList:
    """Implementazione di una pila, con tutte le funzione per gli inserimenti e le rimozioni di elementi"""
    def __init__(self):
        self.lista=[]

    def push(self,elem):
        """Metodo che appende in coda alla lista l'elemento da inserire(diverso da insert)"""
        

        self.lista.append(elem)

    def pop(self):
        """Metodo che rimuove un elemento"""
        if len(self.lista)==0:
            return None
        return self.lista.pop()

    def top(self):
        """Metodo per stampare a video il primo elemento della lista"""
        if len(self.lista)==0:
            return None
        return self.lista[-1]

    def listaVuota(self):
        """Metodo per controllare se la lista, dopo eventuali operazioni e' vuota"""
        return len(self.ista)==0

    def stampa(self):
        """Metodo per stampare tutti gli elementi della lista"""
        print("Elementi nella raccolta:")
        print(self.lista)







def provaPila(lista):
    """Ora eseguo un  test sulla pila appena implementata, imponendo che il tipo sia una lista"""

    if not istanza(lista,Pila):
        raise TypeError("Il tipo di dato atteso � una pila")

    for i in range(10):
        lista.push(i)
    lista.stampa()




    print("Top:", lista.top())
    print("Pop:", lista.pop())
    print("Top:", lista.top())
    print("Pop:", lista.pop())

    lista.stampa()



"""Eseguiamo il modulo direttamente qui, senza importarlo in un altro"""
if __name__=="__main__"":

   print("PilaArrayList")
   lista=PilaArrayList()
   provaPila(lista)
