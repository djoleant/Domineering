# Domineering
Domineering is student project done for Artificial Intelligence subject at Faculty of Electronic Engineering, University of Niš.

#### ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
#### Contributors:
-> Emilija Ćojbašić, 18026 </br>
-> Matija Špeletić, 18043 </br>
-> Đorđe Antić, 17544 </br>

### What is Domineering
Domineering (also called Stop-Gate or Crosscram) is a mathematical game that can be played on any collection of squares on a sheet of graph paper. For example, it can be played on a 6×6 square, a rectangle, an entirely irregular polyomino, or a combination of any number of such components. Two players have a collection of dominoes which they place on the grid in turn, covering up squares. One player places tiles vertically, while the other places them horizontally. (Traditionally, these players are called "Left" and "Right", respectively, or "V" and "H". Both conventions are used in this article.) As in most games in combinatorial game theory, the first player who cannot move loses. [1]

<img width="367" alt="image" src="https://user-images.githubusercontent.com/48065134/204281790-eaed2912-86f3-4896-be0d-a51bf09e6bac.png">

### Problem description
-> Problem is the game "Domineering" </br>
-> Board dimensions: mxn </br>
-> Tiles dimensions: 2x1 </br>
-> Two players: X and O </br>
-> Player that can't place tile on the board loses </br>
-> Human vs Computer (it is optional who plays first) [2]

### Game rules
-> Board is initially empty </br>
-> Players play alternately </br>
-> First player can place tiles only vertically and another one horizontally </br>
-> Tiles can't overlap or peek out of the board [2]

### References
[1] https://en.wikipedia.org/wiki/Domineering </br>
[2] Assignment description

## Quickstart

Clone this repository via

```
git clone https://github.com/djoleant/Domineering.git
cd Domineering
```

Install requirements
```
pip install pygame
```

Start the game
```
TODO: define main file
```

## Izveštaj prve faze izrade projekta
### Formulacija problema i interfejs
</br>

U prvoj fazi izrade projekta Dominacija su implementirane sledeće funkcije:

- Funkcija za postavljanje početnog stanja
- Funkcija za proveru kraja igre
- Funkciju za proveru ispravnosti unetog poteza
- Funkcija za igranje poteza
- Funkcija za prikaz stanja

## Izveštaj prve faze izrade projekta
### Operator promene stanja
</br>

U drugoj fazi izrade projekta Dominacija su realizovane su funkcije koje obezbeđuju:
- Menjanje trenutnog stanja igre na osnovu konkretnog poteza
- Unos početnih parametara igre
- Unos novog poteza i proveru da li je potez ispravan
- Odigravanje novog poteza ako je ispravan i promenu trenutnog stanja igre
- Prikaz novonastalog stanja igre nakon odigravanja poteza
- Proveru kraja i određivanje pobednika u igri nakon odigravanja svakog poteza
- Formiranje novog stanja igre na osnovu zadatog poteza i zadatog stanja igre
- Formiranje svih mogućih stanja igre na osnovu zadatog igrača i stanja igre
</br>



### Funkcija za postavljanje početnog stanja
```def initialize(size_n, size_m, first)```
Funkcija priprema tablu za novu partiju igre. Funkciji se prosleđuju parametri koji se odnose
na veličinu table, kao i parametar koji se odnosi na prvog igrača.

### Funkcija za proveru kraja igre

```def check_winner()```
Funkcija proverava da li je neki od igrača pobedio tj. da li je došlo do kraja igre. Ona
proverava da li se igra nastavlja. Ona vraća _N_ ako niko nije pobedio, _X_ ako je X pobedio i _O_
ako je O pobedio.

### Funkcija za proveru ispravnosti unetog poteza

```def is_valid(x, y, dir)```
Funkcija proverava da li je potez ispravan. Prosleđuju joj se parametri koordinata kao i smer
igranja. Ako je potez validan vraća _True_ , a u suprotnom _False._

### Funkcija za igranje poteza

```def play_move(x, y)```
Funkcija postavlja na tablu za igru domine uz prethodnu proveru da li je potez validan.

### Funkcija za prikaz stanja

```def print_board()```
Funkcija prikazuje aktuelno stanje table za igru tj. štampa njenu grafčku reprezentaciju.

### Funkcija koja formira novo stanje igre

```def make_move(x, y, dir)```
Funkcija koja na osnovu zadatog poteza i zadatog stanje igre (table) formiraju novo stanje igre
(table)

### Funkcija koja kreira sva moguća stanja igre (Operator promene stanja)

```def get_valid_moves()```
Funkcija koja na osnovu zadatog igrača na potezu i zadatog stanje igre (table) formiraju sva
moguća stanje igre (sve moguće table), korišćenjem funkcija iz prethodne stavke

### Funkcija odigravanja

```def play_game(size_n, size_m, first)```
Glavna funkcija koja pozivanjem prethodno implementiranih funkcija omogućava
odigravanje partije igre.
