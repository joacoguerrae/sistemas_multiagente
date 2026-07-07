# 🎮 Conceptos Fundamentales de Teoría de Juegos

Este documento sintetiza la teoría base extraída de las diapositivas sobre **Juegos Ordinales** y **Estrategias Mixtas**, esencial para justificar los resultados y entender los equilibrios teóricos en los ambientes de validación como **Matching Pennies** y **Rock-Paper-Scissors (RPS)**.

---

## 1. Juegos en Forma Normal (Repeated Normal-Form Games)
Un juego en forma normal finito se define por la tupla:
$$\Gamma = \langle P, A, R \rangle$$

Donde:
*   $P = \{1, 2, \dots, n\}$ es el conjunto finito de **agentes** (jugadores).
*   $A = A_1 \times A_2 \times \dots \times A_n$ es el espacio de **acciones conjuntas**, donde cada $A_p$ es el conjunto finito de acciones del jugador $p$. Un perfil de acciones conjuntas se denota como $a = (a_p, a_{-p}) \in A$.
*   $R = (R_1, R_2, \dots, R_n)$ es el vector de funciones de **recompensa/utilidad**, donde $R_p : A \to \mathbb{R}$ es la recompensa obtenida por el jugador $p$ ante la acción conjunta $a$.

---

## 2. Estrategias Mixtas o Estocásticas
Una **estrategia mixta** $\pi_p$ para el jugador $p$ es una distribución de probabilidad sobre su conjunto de acciones $A_p$:
$$\pi_p \in \Delta(A_p) \quad \text{tal que} \quad \sum_{a_p \in A_p} \pi_p(a_p) = 1 \quad \text{y} \quad \pi_p(a_p) \ge 0 \; \forall a_p \in A_p$$

*   Una **estrategia pura** es un caso particular en el cual existe una acción $a_p$ con probabilidad $\pi_p(a_p) = 1$ y $\pi_p(a'_p) = 0$ para toda $a'_p \neq a_p$.
*   Una **estrategia conjunta** $\pi = (\pi_1, \dots, \pi_n)$ es el producto de las estrategias individuales de cada jugador (bajo la hipótesis de independencia):
$$\pi(a) = \prod_{p \in P} \pi_p(a_p)$$
*   El **soporte** de una estrategia mixta $\pi_p$ es el conjunto de acciones puras elegidas con probabilidad no nula: $\text{supp}(\pi_p) = \{ a_p \in A_p \mid \pi_p(a_p) > 0 \}$.

---

## 3. Valor Esperado (Expected Utility)
El **valor esperado** para el jugador $p$ dado un perfil de estrategia conjunta $\pi$ se define como:
$$V_p(\pi) = \mathbb{E}_{a \sim \pi} [R_p(a)] = \sum_{a \in A} \pi(a) R_p(a)$$

### Ejemplo en *Matching Pennies*:
Si ambos jugadores juegan cara ($H$) y cruz ($T$) con distribución uniforme $\pi_p(H) = \pi_p(T) = \frac{1}{2}$, el valor esperado para el Jugador 1 es:
$$V_1(\pi) = \frac{1}{4} R_1(H,H) + \frac{1}{4} R_1(H,T) + \frac{1}{4} R_1(T,H) + \frac{1}{4} R_1(T,T)$$
$$V_1(\pi) = \frac{1}{4}(1) + \frac{1}{4}(-1) + \frac{1}{4}(-1) + \frac{1}{4}(1) = 0$$

---

## 4. Mejor Respuesta (Best Response)
Una estrategia mixta $\pi_p$ es una **Mejor Respuesta (BR)** del jugador $p$ a las estrategias del resto de los jugadores $\pi_{-p}$ si maximiza su valor esperado:
$$\pi_p \in BR_p(\pi_{-p}) \iff V_p(\pi_p, \pi_{-p}) = \max_{\pi'_p \in \Delta(A_p)} V_p(\pi'_p, \pi_{-p})$$

> 💡 **Propiedad Fundamental:** Para toda estrategia conjunta de los oponentes $\pi_{-p}$, siempre existe al menos una **estrategia pura** $a_p \in A_p$ que pertenece al conjunto de Mejores Respuestas $BR_p(\pi_{-p})$.

---

## 5. Equilibrio de Nash (NE)
Un **Equilibrio de Nash** es una estrategia conjunta $\pi^* = (\pi^*_1, \dots, \pi^*_n)$ tal que ningún jugador tiene incentivos para desviarse unilateralmente. Es decir, la estrategia de cada jugador es una mejor respuesta a las estrategias de los demás:
$$\pi^*_p \in BR_p(\pi^*_{-p}) \quad \forall p \in P$$

*   **Teorema de Nash (1951):** Todo juego finito posee al menos un Equilibrio de Nash (ya sea puro o mixto).

---

## 6. Teorema Minimax (von Neumann, 1928)
En juegos de **suma cero para dos jugadores** (donde $R_1(a) = -R_2(a)$ para toda acción conjunta $a$), las utilidades están en estricto conflicto. 
El teorema Minimax establece que:
$$V_{\text{máx},\text{mín}} = \max_{\pi_1} \min_{\pi_2} V_1(\pi_1, \pi_2) = \min_{\pi_2} \max_{\pi_1} V_1(\pi_1, \pi_2) = V_{\text{mín},\text{máx}} = V^*$$

Donde $V^*$ es el **valor minimax** (o valor del juego).
*   Cualquier perfil de estrategias que resuelva el problema minimax es un **Equilibrio de Nash**.
*   Todos los Equilibrios de Nash de un juego de suma cero tienen el mismo valor esperado $V^*$ y son intercambiables.

### Programación Lineal para calcular la estrategia Minimax de $p$:
Para hallar la estrategia minimax del jugador $p$:
$$\text{Minimizar } V$$
$$\text{Sujeto a: } \sum_{a \in A_p} \pi_p(a) R_p(a, b) \le V \quad \forall b \in A_q$$
$$\sum_{a \in A_p} \pi_p(a) = 1$$
$$\pi_p(a) \ge 0 \quad \forall a \in A_p$$

---

## 7. Perfiles de Equilibrio de Nash de los Juegos de Validación

### A. Matching Pennies (MP)
Juego simétrico de suma cero. Matriz de recompensas (Jugador 1 es filas):
$$\begin{array}{c|cc}
 & H & T \\
\hline
H & 1, -1 & -1, 1 \\
T & -1, 1 & 1, -1 \\
\end{array}$$
*   **Equilibrio de Nash:** $\pi^*_1 = (\frac{1}{2}, \frac{1}{2})$, $\pi^*_2 = (\frac{1}{2}, \frac{1}{2})$.
*   **Valor del juego:** $V^* = 0$.
*   No posee equilibrios en estrategias puras (los agentes cíclicamente quieren cambiarse si el rival juega de forma determinista).

### B. Rock-Paper-Scissors (RPS)
Juego simétrico de suma cero de 3 acciones. Matriz de recompensas:
$$\begin{array}{c|ccc}
 & R & P & S \\
\hline
R & 0, 0 & -1, 1 & 1, -1 \\
P & 1, -1 & 0, 0 & -1, 1 \\
S & -1, 1 & 1, -1 & 0, 0 \\
\end{array}$$
*   **Equilibrio de Nash:** $\pi^*_1 = (\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$, $\pi^*_2 = (\frac{1}{3}, \frac{1}{3}, \frac{1}{3})$.
*   **Valor del juego:** $V^* = 0$.
