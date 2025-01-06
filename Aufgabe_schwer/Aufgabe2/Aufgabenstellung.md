### **Kürzester Pfad mit Dijkstra**  

**Aufgabe:**  

Gegeben ein gerichteter, gewichteter Graph, ermittle die kürzesten Distanzen vom Startknoten zu allen anderen Knoten.

**Input Format:**  

- Erste Zeile: `V` und `E` (Anzahl Knoten, Anzahl Kanten).

- Zweite Zeile: Startknoten `s`.  

- Nächste `E` Zeilen: `u v w` mit einer Kante von `u` nach `v` mit Kosten `w`. Knoten sind z. B. von 1 bis `V` nummeriert.

**Output Format:**  

- Eine Zeile mit `V` Zahlen: Die kürzeste Distanz von `s` zu jedem Knoten (oder `INF`, wenn unerreichbar).

**Beispiel:**  

**Input:**  

5 6  

1  

1 2 1  

1 3 2  

2 3 1  

2 4 2  

3 5 4  

4 5 1  

**Output:**  

0 2 3 4 5  

(Erläuterung: Distanz von 1 zu 1 ist 0, zu 2 ist 2, zu 3 über 2 ist 3 (1->2->3), zu 4 ist 4 (1->2->4) und zu 5 ist 5 (1->2->4->5).)  