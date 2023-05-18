# Fact-checking-app
## Introduzione
L'applicazione consente agli utenti di inserire una notizia e di verificare la sua veridicità.
## Requisiti
- Python 3.x
- Flask
- SQLAlchemy
## Installazione
1. Scaricare o clonare il repository su una directory locale.
2. Aprire il terminale e posizionarsi nella directory del progetto.
3. Creare un ambiente virtuale utilizzando il comando: python -m venv venv
4. Attivare l'ambiente virtuale utilizzando il comando:
```python
#Linux/Mac
source venv/bin/activate
``` 
```python
#Windows
venv\Scripts\activate
``` 
5. Installare le dipendenze utilizzando il comando: pip install -r requirements.txt
6. Avviare l'applicazione utilizzando il comando: flask run
## Utilizzo
Dopo aver avviato l'applicazione, è possibile accedere all'applicazione nel browser web all'indirizzo http://localhost:5000/
## Struttura del progetto
- app.py: il file principale dell'applicazione Flask.
- routes.py: il file che definisce le rotte dell'applicazione.
- templates/: la directory che contiene i file HTML del progetto.
- static/: la directory che contiene i file statici del progetto (CSS, JS, immagini, ecc.).
- tests/: la directory che contiene i file di test dell'applicazione.
- requirements.txt: il file che elenca le dipendenze del progetto.
