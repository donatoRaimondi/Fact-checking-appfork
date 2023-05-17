# Fact-checking-app
---
##Introduzione
L'applicazione consente agli utenti di inserire una notizia e di verificare la sua veridicità.
##Requisiti
Python 3.x
Flask
Database
##Installazione
1.Scaricare o clonare il repository su una directory locale.
2.Aprire il terminale e posizionarsi nella directory del progetto.
3.Creare un ambiente virtuale utilizzando il comando: python -m venv venv
4.Attivare l'ambiente virtuale utilizzando il comando: source venv/bin/activate (per Linux/Mac) o venv\Scripts\activate (per Windows)
5.Installare le dipendenze utilizzando il comando: pip install -r requirements.txt
6.Creare il database utilizzando il comando: flask init-db
7.Avviare l'applicazione utilizzando il comando: flask run
##Utilizzo
Dopo aver avviato l'applicazione, è possibile accedere all'applicazione nel browser web all'indirizzo http://localhost:5000/
##Struttura del progetto
-app.py: il file principale dell'applicazione Flask.
< -models.py: il file che definisce il database e le tabelle. >
-routes.py: il file che definisce le rotte dell'applicazione.
-templates/: la directory che contiene i file HTML del progetto.
-static/: la directory che contiene i file statici del progetto (CSS, JS, immagini, ecc.).
-tests/: la directory che contiene i file di test dell'applicazione.
-requirements.txt: il file che elenca le dipendenze del progetto.