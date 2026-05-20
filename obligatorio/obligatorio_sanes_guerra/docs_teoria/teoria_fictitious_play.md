# 🧠 Fictitious Play (FP) - Teoría y Algoritmo

Este documento detalla el marco teórico, las fórmulas matemáticas y el pseudocódigo para la implementación de **Fictitious Play**, uno de los algoritmos de aprendizaje por refuerzo multiagente clásicos solicitados en la letra del obligatorio.

---

## 1. Introducción y Supuestos
Fictitious Play (propuesto por Brown en 1951 y Robinson en 1951) es una técnica iterativa de aprendizaje basada en creencias.
*   **Supuesto de Estacionariedad:** Cada jugador $p$ asume de manera simplista que sus oponentes juegan de acuerdo con una estrategia mixta (estocástica) estacionaria, aunque desconocida.
*   **Hipótesis de Independencia:** Cada jugador asume que las decisiones de sus oponentes son estadísticamente independientes entre sí. Por ende, la probabilidad conjunta de las acciones del rival es simplemente el producto de las probabilidades marginales individuales estimadas.
*   **Aprendizaje del Oponente (Agent Modeling):** A diferencia de algoritmos ingenuos que solo observan recompensas, FP requiere observar las acciones jugadas por los rivales en cada ronda y conocer completamente su propia matriz de utilidades.

---

## 2. Formulación Matemática

### A. Conteo de Acciones del Oponente
Sea $\text{count}_{p,q}^t(a_q)$ la cantidad de veces que el jugador $p$ ha observado al oponente $q \neq p$ jugar la acción $a_q \in A_q$ hasta la iteración $t$.

1.  **Inicialización (t = 0):** Se asigna un conteo inicial arbitrario (usualmente estrictamente positivo para evitar divisiones por cero):
$$\text{count}_{p,q}^0(a_q) = c_0(a_q) > 0 \quad \forall a_q \in A_q$$
2.  **Regla de Actualización (t + 1):** Tras jugarse la ronda $t+1$, cada jugador $p$ observa las acciones elegidas y actualiza sus contadores:
$$\text{count}_{p,q}^{t+1}(a_q) = \text{count}_{p,q}^t(a_q) + \mathbb{I}(a_{q}^{t+1} = a_q)$$
donde $\mathbb{I}(\cdot)$ es la función indicadora que vale $1$ si el oponente $q$ jugó la acción $a_q$ en la iteración $t+1$, y $0$ en caso contrario.

### B. Estimación de la Estrategia del Oponente
En cada iteración $t$, el jugador $p$ estima la estrategia estocástica del oponente $q$ aproximando la frecuencia empírica de sus acciones del pasado:
$$\hat{\pi}_{q}^t(a_q) = \frac{\text{count}_{p,q}^t(a_q)}{\sum_{a'_q \in A_q} \text{count}_{p,q}^t(a'_q)}$$

Bajo la hipótesis de independencia de los oponentes, la creencia conjunta sobre las acciones de todos los rivales $\hat{\pi}_{-p}^t(a_{-p})$ se calcula como:
$$\hat{\pi}_{-p}^t(a_{-p}) = \prod_{q \neq p} \hat{\pi}_{q}^t(a_q)$$

### C. Regla de Decisión (Mejor Respuesta)
El jugador $p$ elige jugar una acción pura $a_p^t$ en la iteración $t$ que maximice su valor esperado (Mejor Respuesta) frente a sus creencias sobre los oponentes:
$$a_p^t \in BR_p(\hat{\pi}_{-p}^t) = \arg\max_{a_p \in A_p} V_p^t(a_p, \hat{\pi}_{-p}^t)$$

Donde la utilidad esperada de jugar la acción pura $a_p$ es:
$$V_p^t(a_p, \hat{\pi}_{-p}^t) = \sum_{a_{-p} \in A_{-p}} R_p(a_p, a_{-p}) \hat{\pi}_{-p}^t(a_{-p})$$

---

## 3. Pseudocódigo para $N$ Agentes

```text
Para cada agente p en P:
    Inicializar count_{p,q}(a_q) = c_0 > 0 para todo q != p, a_q en A_q
    
En cada ronda t = 1, 2, ...:
    1. Calcular la creencia marginal estimada de cada oponente q != p:
       Para todo q != p, a_q en A_q:
           pi_hat_q(a_q) = count_{p,q}(a_q) / sum_{a'_q} count_{p,q}(a'_q)
           
    2. Calcular la creencia conjunta de los rivales (bajo independencia):
       Para cada vector de acciones del oponente a_{-p} en A_{-p}:
           pi_hat_{-p}(a_{-p}) = producto_{q != p} pi_hat_q(a_q)
           
    3. Computar la utilidad esperada para cada una de sus acciones puras a_p en A_p:
       Para cada a_p en A_p:
           V(a_p) = sum_{a_{-p} en A_{-p}} R_p(a_p, a_{-p}) * pi_hat_{-p}(a_{-p})
           
    4. Elegir la acción que maximiza la utilidad esperada:
       a_p^t = arg_max_{a_p} V(a_p)  [rompiendo empates de forma consistente o aleatoria]
       
    5. Jugar a_p^t y observar la acción conjunta real jugada a^t = (a_p^t, a_{-p}^t)
    
    6. Actualizar contadores:
       Para todo q != p:
           count_{p,q}(a_{q}^t) = count_{p,q}(a_{q}^t) + 1
```

---

## 4. Propiedades de Convergencia
*   **Equilibrio de Nash:** Si la estrategia empírica conjunta simulada por Fictitious Play converge a una distribución de probabilidad $\pi$, entonces $\pi$ es un **Equilibrio de Nash**.
*   **Juegos de Suma Cero para 2 Jugadores:** La convergencia empírica está garantizada matemáticamente en juegos de suma cero de dos jugadores (como *Matching Pennies* y *Rock-Paper-Scissors*).
*   **Juegos Solubles por Dominancia Estratégica:** Converge en juegos resolubles por eliminación iterativa de estrategias estrictamente dominadas.
*   **Juegos de Potencial:** Converge en juegos de potencial (donde los intereses de los agentes están fuertemente alineados).
*   ⚠️ **No Convergencia (Ciclos):** En juegos de coordinación general, FP puede no converger y exhibir ciclos infinitos de estrategias puras (como lo demostró el famoso contraejemplo de Shapley en 1964).
