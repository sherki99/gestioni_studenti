class GestioniStudenti: 
    def __init__(self):
        self.studenti = []
    

    def aggiungi_studente(self, studente):
        """
        """
        pass

    def ordine_alfabitico_studenti(self):
        """
        Ordina la lista interna per cognome, poi per nome.
        usando il metodo sort() della lista.
        
        Parameters
        ----------
        None

        Returns
        -------
        None

        Raises
        -------
        Exception: Se si verifica un errore durante l'ordinamento della lista.

        Examples
        >>> oridine_alfabitico_studenti([["nome": "Mario", "cognome": "Rossi"], ["nome": "Luca", "cognome": "Bianchi"]])
        >>> # Risultato: Lista studenti ordinata per cognome e nome.
        """

        try: 
            self.studenti.sort(key=lambda s: (s["cognome"].lower(), s["nome"].lower()))
            print("Lista studenti ordinata con successo")

        except Exception as e:
            print("Errore durante l'ordinamento della lista studenti:", e)