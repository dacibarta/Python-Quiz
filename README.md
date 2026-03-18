# Python-Quiz
Python középhaladó záróvizsga feladat

Ez a projekt egy interaktív, feleletválasztós kvízjáték, amelynek célja, hogy szórakoztató 
formában tegye próbára a játékos tudását, miközben a háttérben statisztikák 
gyűjtésével segít képet adni a fejlődésről és a leggyakrabban elkövetett hibákról. 

Telepítés és futtatás: 
A projekt Python 3.14.2 verzióban készült. (ajánlott, de min. 3.10) 

Fontos a jupyter notebook futtatása a projektkönyvtárban 8888 porton: 
Anaconda Prompt -> 
  cd C:\(teljes_elérési útvonal)\zv 
  jupyter notebook 

Django admin felület:
Terminal -> 
  pip install django 
  python backend/manage.py makemigrations 
  python backend/manage.py migrate 

Tkinter felhasználói interfész: 
Terminal -> 
  python client\quiz_client.py 
