# ⚖️ Regret Matching (RM) y Equilibrio Correlacionado

Este documento detalla el fundamento teórico, la formulación matemática y el pseudocódigo del algoritmo **Regret Matching (RM)**, así como su convergencia matemática al conjunto de **Equilibrios Correlacionados (CE)** de Robert Aumann.

---

## 1. Concepto de Arrepentimiento (Regret)
Regret Matching (Hart y Mas-Colell, 2000) es un algoritmo de la familia de aprendizaje con **"arrepentimiento nulo" (No-Regret Learning)**.
*   **Intuición:** El arrepentimiento es la diferencia de utilidad entre lo que un agente *obtuvo* realmente y lo que *pudo haber obtenido* de haber elegido otra acción pura, asumiendo que los oponentes no cambiaron su decisión.
*   **Nivel de información:** A diferencia de Fictitious Play, RM es un algoritmo **informado**. No necesita estimar o modelar las creencias del oponente de forma directa; únicamente requiere conocer su propia matriz de recompensas y calcular qué recompensas alternativas habrían surgido ante cada una de sus posibles acciones puras.

---

## 2. Formulación Matemática

### A. Arrepentimiento Instantáneo
Sea $a^t = (a_p^t, a_{-p}^t) \in A$ la acción conjunta jugada en la iteración $t$. La utilidad real del jugador $p$ es $R_p(a^t)$.
Si el jugador $p$ hubiese elegido una acción alternativa $a'_p \in A_p$, su utilidad simulada habría sido $R_p(a'_p, a_{-p}^t)$.

El **arrepentimiento instantáneo** $g_p^t(a'_p)$ por no haber jugado la acción $a'_p$ en la ronda $t$ se define como:
$$g_p^t(a'_p) = R_p(a'_p, a_{-p}^t) - R_p(a^t)$$

*   Si $g_p^t(a'_p) > 0$, el agente lamenta no haber elegido $a'_p$ porque habría obtenido más recompensa.
*   Si $g_p^t(a'_p) \le 0$, el agente no lamenta su decisión (obtuvo igual o más recompensa que eligiendo $a'_p$).

### B. Arrepentimiento Acumulado
El **arrepentimiento acumulado** $G_p^t(a'_p)$ hasta la iteración $t$ es la suma de los arrepentimientos instantáneos de cada ronda:
$$G_p^t(a'_p) = \sum_{s=1}^t g_p^s(a'_p) = G_p^{t-1}(a'_p) + g_p^t(a'_p)$$

### C. Estrategia de Selección de Acciones
En la iteración $t+1$, el agente $p$ construye una distribución de probabilidad $\hat{\pi}_p^{t+1}$ sobre su espacio de acciones $A_p$ proporcional a los **arrepentimientos positivos acumulados**:
$$\hat{\pi}_p^{t+1}(a'_p) = \frac{\max\{G_p^t(a'_p), 0\}}{\sum_{a''_p \in A_p} \max\{G_p^t(a''_p), 0\}}$$

*   **Caso Especial:** Si el denominador es nulo o negativo (es decir, el agente no tiene arrepentimiento positivo acumulado para ninguna de sus acciones), se asigna la **distribución uniforme**:
$$\hat{\pi}_p^{t+1}(a'_p) = \frac{1}{|A_p|} \quad \forall a'_p \in A_p$$

### D. Estrategia Promedio Aprendida
El algoritmo extrae a lo largo de las rondas una estrategia promedio $\bar{\pi}_p^t$, que es la media aritmética de las estrategias jugadas en cada iteración:
$$\bar{\pi}_p^t = \frac{1}{t} \sum_{s=1}^t \hat{\pi}_p^s$$

---

## 3. Pseudocódigo

```text
Para cada agente p en P:
    Inicializar G_p(a_p) = 0 para todo a_p en A_p
    Inicializar pi_hat_p con la distribución uniforme: pi_hat_p(a_p) = 1 / |A_p|
    
En cada ronda t = 1, 2, ...:
    1. El agente p elige su acción a_p^t muestreando de pi_hat_p:
       a_p^t ~ pi_hat_p
       
    2. Jugar la acción conjunta y observar el vector de acciones de los rivales a_{-p}^t
       y la recompensa obtenida R_p(a_p^t, a_{-p}^t)
       
    3. Calcular el arrepentimiento instantáneo para toda acción pura alternativa a'_p en A_p:
       Para cada a'_p en A_p:
           g_p^t(a'_p) = R_p(a'_p, a_{-p}^t) - R_p(a_p^t, a_{-p}^t)
           
    4. Acumular los arrepentimientos:
       Para cada a'_p en A_p:
           G_p(a'_p) = G_p(a'_p) + g_p^t(a'_p)
           
    5. Actualizar la estrategia de juego para la siguiente iteración t+1:
       SumaRegretsPositivos = sum_{a''_p} max{ G_p(a''_p), 0 }
       
       Si SumaRegretsPositivos > 0:
           Para cada a'_p en A_p:
               pi_hat_p(a'_p) = max{ G_p(a'_p), 0 } / SumaRegretsPositivos
       Sino:
           Para cada a'_p en A_p:
               pi_hat_p(a'_p) = 1 / |A_p|
               
    6. Actualizar y almacenar la estrategia promedio acumulada:
       pi_avg_p = (1 / t) * sum_{s=1..t} pi_hat_p^s
```

---

## 4. Equilibrio Correlacionado (Correlated Equilibrium - CE)
Propuesto por Robert Aumann en 1974, el **Equilibrio Correlacionado** generaliza el concepto de Equilibrio de Nash introduciendo la posibilidad de señales de correlación coordinadas (como semáforos, un mediador o el lanzamiento de una moneda conjunta).

### Definición Matemática
Sea $\pi : A \to [0, 1]$ una distribución de probabilidad conjunta sobre el espacio de acciones $A$.
Un modificador de acción para el jugador $p$ es cualquier función $\xi_p : A_p \to A_p$.
La distribución conjunta $\pi$ es un **Equilibrio Correlacionado** si para todo jugador $p$ y todo modificador de acción $\xi_p$ se cumple:
$$\sum_{a \in A} \pi(a) R_p(\xi_p(a_p), a_{-p}) \le \sum_{a \in A} \pi(a) R_p(a)$$

*   **Interpretación:** Si un mediador sortea en secreto una acción conjunta $a$ de acuerdo con $\pi$ y le indica a cada jugador $p$ únicamente su propia componente recomendada $a_p$, ningún jugador tiene incentivos para desobedecer y desviarse a otra acción $a'_p = \xi_p(a_p)$, asumiendo que los demás obedecen sus recomendaciones.
*   **Propiedad:** El conjunto de Equilibrios Correlacionados es **convexo** y contiene rigurosamente a todos los Equilibrios de Nash (tanto puros como mixtos).

---

## 5. Garantías de Convergencia de Regret Matching
*   **Teorema de Hart y Mas-Colell (2000):** Si todos los jugadores en un juego repetido en forma normal adoptan el algoritmo Regret Matching, la **estrategia promedio conjunta** $\bar{\pi}^t = (\bar{\pi}_1^t, \bar{\pi}_2^t, \dots)$ converge casi seguro al conjunto de **Equilibrios Correlacionados (CE)** del juego cuando $t \to \infty$.
*   **Juegos de Suma Cero:** En juegos de suma cero de dos jugadores, la convergencia del promedio de las estrategias de RM al conjunto de Equilibrios Correlacionados resulta equivalente a converger a un **Equilibrio de Nash (NE)** del juego.
