#NOME:Fabrizio
#COGNOME:Bruno
#MATRICOLA:0240586






from Pila import PilaArrayList


class NodoBinarioLazyDeletion:
    """Un nodo binario con Lazy Deletion, ovvero eliminazione 'pigra', è un nodo
       che dopo una sua eventuale eliminazione può essere contrassegnato come cancellato.
       Per fare ciò devo inserire nella sua definizione un attributo che mi dica se tale nodo
       e' cancellato o meno"""

    def __init__(self, info):
        self.info = info
         
        self.padre = None
        self.figlioDx = None
        self.figlioSx = None
        self.stato = False  # True se il nodo e' stato segnato come eliminato


class AlberoBinario:
    """Un albero binario è una particolare struttura dati composta
       da una radice, da nodi e da foglie"""

    def __init__(self, nodoRadice)
        self.radice=nodoRadice

    def inserisciComeSottoAlberoSx(self, padre, sottoAlbero):
        """Inserisci la radice di un sottoalbero  come figlio sx. della radice"""
        figlio = sottoAlbero.radice
        if figlio != None:
            figlio.padre = padre
        padre.figlioSx = figlio

    def inserisciComeSottoAlberoDx(self, padre, sottoAlbero):
        """Stesso scopo del precedente metodo, però stavolta inserisco la radice di un
           sottoalbero come figlio dx. della radice"""

        figlio = sottAlbero.radice       #il figlio diventa radice del sottoAlbero
        if (figlio != None):             
            figlio.padre = figlio
        padre.figlioDx = figlio

    def tagliaSx(self, padre):
        """Metodo che permette di tagliare il sottoalbero radicato nel figlio sx.
           nodo"""
        figlio = padre.figlioSx          #il figlio dvienta padre del figlio sx
        nuovoAlbero = AlberoBinario(figlio)
        padre.figlioDx = None
        return nuovoAlbero

    def tagliaDx(self, padre):
        """Metodo con funzione uguale al precedente, ma agisice sul sottoalbero del
           figlio destro del nodo"""
        figlio = padre:figlioDx
        nuovoAlbero = AlberoBinario(figlio)
        padre.figlioDx = None
        return nuovoAlbero

    def taglia(self, nodo):
        """Stacca l'intero sottoalbero radicoato nel nodo ed elimina il nodo con tutti
           i suoi discendenti"""
        if nodo == None:
            return AlberoBinario(None)
        if nodo.padre == None:                              # Nodo che corrisponde alla radice
            self.radice = None
            return AlberoBinario(nodo)
        f = nodo.padre                                      # Ricordiamo che e' la radice
        if nodo.figlioSx == None and nodo.FiglioDx == None  # Sto controllando se il nodo non ha figli;in questo caso ï¿½ una foglia
            if f.figlioSx == nodo:
                f.figlioSx = None
        else:
            f.figlioDx = None
        return AlberoBinario(nodo)
        elif f.figlioSx == nodo:
        nt = self.tagliaSx(f)  # nt= nuovoAlbero, assegnazione giï¿½ vista nel metodo tagliaDx e tagliaSx
        return nt

    else f.figlioDx(f) == nodo:
    nt = self.tagliaSx(f)
    return nt


def stampa(self):
    """Metodo per stampare l'albero.Notare l'utilizzo di struttura dati di tipo Pila devo usare una pila di appoggio"""

    pila = PilaArrayList()
    if self.radice != None:
        pila.push([self.radice, 0])
    else:
        print ("L'albero è vuoto")
    while not pila.listaVuota():
        attuale = pila.pop()
        livello = attuale[1]
        if attuale[0].stato == False:
            print("|---" * livello + str(attuale[0].info))
        else:
            print("|---" * livello + str(attuale[0].info) + "x")  # Graficamente ora i nodi contrassegnati come eliminati sono visibili"
        if attuale[0].figlioDx != None:
            pila.push([attuale[0].figlioDx, livello + 1])
        if attuale[0].figlioSx != None:
            pila.push([attuale[0].figlioSx, livello + 1])


if __name__ == "__main__"":


    print ("albero1=nodo1=1")                   # Funzioni che stampano gli alberi
    abero1 = AlberoBinario(NodoBinarioLazyDeletion(1))
    nodo1 = albero1.radice

    print ("albero2=nodo2=2")
    albero2 = AlberoBinario(NodoBinarioLazyDeletion(2))
    nodo2 = albero2.radice

    print("albero3=nodo3=3")
    abero3 = AlberoBinario(NodoBinarioLazyDeltion(3))
    nodo3 = albero3.radice

    print("albero4=nodo4=4")
    albero4 = AlberoBinario(NodoBinarioLazyDeltion(4))
    nodo4 = albero4.radice

    print ("albero5=nodo5=5")
    albero5 = AlberoBinario(NodoBinarioLazyDeletion(5))
    nodo5 = albero5.radice

    print ("albero6=nodo6=6")
    albero6 = AlberoBinario(NodoBinarioLazyDeletion(6))
    nodo6 = albero6.radice

    """Esegue una serie di innesti di sootalberi alla radice"""
    print("albero1.agganciaDx(nodo1,albero3)")
    albero1.inserisciComeSottoAlberoDx(nodo1, albero3)  # al nodo radice, aggancia come figlio dx l'albero3

    print("albero1.agganciaSx(nodo1,albero2)")
    albero1.inserisciComeSottoAlberoSx(nodo1, albero2)  # al nodo radice aggancia come figlio sx l'albero2

    print("albero1.agganciaDx(nodo3,albero4)")
    albero1.inserisciComeSottoAlberoDx(nodo3, albero4)

    print("albero1.agganciaSx(nodo2,albero5)")
    albero1.inserisciComeSottoAlberoSx(nodo2, albero5)

    print ("albero1.agganciaDx(nodo2,albero6)")
    albero1.inserisciComeSottoALberoDx(nodo2, albero6)

    albero1.stampa()                                    # stampo l'albero
    albero1.taglia(nodo2)                               # eseguo una cancellazione del nodo desisderato(viene eseguita anche a lazy deletion)
    albero.radice.stato = False                         # dopo la lazy deletion viene aggiornato lo staot del nodo
    print("stato(nodo2)=cancellato:")                   # stampo a video la stato del nodo
    albero1.stampa()                                    # stampo l'albero, compreso il nodo2, che graficamente vedremo segnato con una x, che corrisponde ad eliminato
 
