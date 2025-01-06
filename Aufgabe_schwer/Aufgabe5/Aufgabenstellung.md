### **Floyd-Warshall (Alle-Paare-Kürzeste-Wege)**  

**Aufgabe:**  

Berechne die kürzesten Entfernungen zwischen allen Paaren von Knoten in einem gewichteten Graphen (auch negative Gewichte, aber keine negativen Zyklen).

**Input Format:**  

- Erste Zeile: `V` (Anzahl Knoten), `E` (Anzahl Kanten).  

- Nächste `E` Zeilen: `u v w` für eine Kante von `u` nach `v` mit Gewicht `w`.  

  (Nicht definierte Wege gelten als unendlich.)

**Output Format:**  
- `V` Zeilen mit je `V` Werten, die die minimalen Distanzen zwischen jedem Knotenpaar angeben, oder `INF`, wenn kein Pfad existiert.

**Beispiel:**  

**Input:**  
4 4  
1 2 5  
2 3 2  
3 4 3  
4 1 1  

**Mögliche Ausgabe (Matrixform, jeweils eine Zeile pro Quellknoten):**  
0 5 7 8  
INF 0 2 5  
INF INF 0 3  
1 INF INF 0  

(Erläuterung: Von Knoten 1 nach 3 mit 1->2->3 sind es 7, nach 4 mit 1->2->3->4 sind es 8, etc.)  