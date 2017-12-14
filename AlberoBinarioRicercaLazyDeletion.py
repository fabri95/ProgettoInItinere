#NOME:Fabrizio
#COGNOME:Bruno
#MATRICOLA:0240586




from AlberoBinario import AlberoBinario
from AlberoBinario import NodoBinarioLazyDeletion



class ABRLD:
    """Un albero di ricerca binario (ARB) e' un albero binario, che per essere tale deve
       soddisfare tre prorpieta' fondamentali:
       1-ogni nodo v dell'albero contiene un elemento, che indicheremo con info[1]
         e una chiave, che indicheremo con info[0]. Le chiavi di ogni nodo sono
         prese da un universo di chiavi totalmente ordinato;
       2-le chiavi del sottalbero dx di v sono maggiori della chiave v:
                       chiave(figliodx)>=chiave(v)

       3-le chiavi del sottoalbero sx di v sono minori della chiave v:
                       chiave(figliosx)<=chiave(v)

       le proprieta' 2 e 3 sono dette anche proprieta' di ordinamento
       per alberi di ricerca binari"""

    def __init__(self):
        self.albero=AlberoBinario()

    def chiave(self,nodo):
        """Metodo per restituire la chiave i un determinato nodo"""
        if nodo==None:
            return None
        return nodo.info[0]                                                  #ritorna il valore corrispondente ad info[0], quindi il valore della chiave

    def elemento(self,nodo):
        """Metodo per restituire il valore dell'elemento contenuto in un nodo"""
        if nodo==None:
            return None
        return nodo.info[1]                                                 #ritorna il valore corrispondente ad info[1], quindi il valore dell'elemento associato al nodo

    def cerca(self,chiave):
        """Metodo per cercare nell'albero una chiave desiderata."""

        if self.albero.radice==None:                                        #L'albero e' vuoto, ritorna None"
            return None


        attuale=self.albero.radice
        while attuale!=None:                                                #Cerca nell'albero fino a quando la radice non e' vuota
            chiaveCorrente=self.chiave(attuale)                             #memeorizza la chiave del nodo corrente
            if chiave==chiaveCorrente:                                      #la chiave che voglio cercare e' uguale a quella in scansione
               if attuale.status== True:
                   return attuale
               else:
                   return None
            if chiave<chiaveCorrente:                                       #la chiave da cercare e' minore della chiave in scansione
                attuale=attuale.figlioSx                                    #il nodo attuale allora e' il figlio sx
            else:
                attuale=attuale.figlioDx                                    #il nodo attuale allore e' il figlio dx

        return None


    def boolDelete(self,chiave):
        """Metodo che consente l'eliminazione di un nodo. La particolarita' di tale
           metodo e' che include la lazy deletion, che contrassegna un nodo come "eliminato"
           senza pere' alterare la struttura dell'albero."""

        daCancellare=self.cerca(chiave)                                      #Inizializzo la chiave da cancellare dopo averla cercata
        if daCancellare==None:                                               #Se tale chiave non esiste, allora ritorna Falso
            return False
        else:
            daCancellare.stato=True                                          #La chiave esiste, quindi cambio il suo stato a True, che mi indica che il nodo a cui fa riferimento e' cancellato
            return True
        
    def inserisci(self,chiave,valore):
           """Metodo che mi permette di inserire una nuova coppia (chiave,valore).Tale inseriemento
           pero' non deve compromettere la proprita' di ordinamento dell'albero."""

           coppia=[chiave,valore]
           nuovoAlbero=AlberoBinario(NodoBinarioLazyDeletion(coppia))

           if self.albero.radice==None:
               self.albero.radice= nuovoAlbero.radice
           else:
               attuale=self.albero.radice                                     #Nodo in analisi
               precedente=None                                                #Nodo appena precedente a quello attuale
               while attuale!=None:                                           #Finche' il nodo attuale non e' vuoto
                   precedente=attuale                                         #il nodo precedente diventa attuale
                   if (chiave==self.chiave(attuale)):                         #se la chiave cercata e' uguale a quella nel nodo attuale
                      attuale.info=coppia                                     #sto sovrascrivendo i valori della nuova coppia a quelli della vecchia coppia
                      attuale.stato=True                                      #aggiorna lo stato del nodo
                      return
                   else:
                       if chiave<self.chiave(attuale):                        #La chiave cercata e' minore del nodo in analisi
                           attuale=attuale.figlioSx                           #il nodo allora da cui continuo la ricerca e' il figlio sx
                       else:
                           attuale=attuale.figlioDx                           #il nodo da cui continuo la ricerca e' il figlio dx
                            
           if chiave<self.chiave(precedente):                                 #la chiave e' minore della chiave del nodo precedente
               self.albero.inserisciComeSottoAlberoSx(precedente, nuovoAlbero)#inserisci l'albero radicato nel nodo precedente come sottalbero sx del nuovo albero
           else:
               self.albero.inserisciComeSottoAlberoDx(precedente,nuovoAlbero) #inserisci l'albero radicato nel nodo precedente come sottoalbero dx del nuovo albero





if __name__=="__main__":
    dizionario.ARBLD()                #chiamo la classe ABRLD

    print ("Inserisci(4,12)")         #Inizio una serie di inserimenti di nuove coppie
    dizionario.inserisci(4,12)

    print ("Inserisci(5,13)")
    dizionario.inserisci(5,13)

    print ("Inserisci (6,14)")
    dizionario.inserisci(6,14)

    print("L'albero risultante dopo gli inserimenti e':")
    dizionario.albero.stampa()

    print("cerca(4)="+str(dizionario.cerca(4)))
    print("cerca(5)="+str(dizionario.cerca(5)))
    print("cerca(6)="+str(dizionario.cerca(6)))


    print("delete(6)")                  #delete intesa come boolDeletion
    dizionario.boolDeletion(6)

    print("delete(4)")
    dizionario.boolDeletion(4)

    print("delete(5)")
    dizionario.boolDeletion(5)


    print("L'albero risultante dopo le cancellazioni e':")
    dizionario.albero.stampa()
