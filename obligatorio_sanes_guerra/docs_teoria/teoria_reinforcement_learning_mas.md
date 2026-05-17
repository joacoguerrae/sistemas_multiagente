# 🤖 Aprendizaje por Refuerzo Multiagente: IQL y JAL-AM

Este documento detalla el marco de los **Juegos Estocásticos (Stochastic Games)** y profundiza en las dos técnicas de aprendizaje por refuerzo multiagente requeridas por el obligatorio: **Independent Q-Learning (IQL)** y **Joint-Action Learning con Agent Modeling (JAL-AM)**.

---

## 1. Juegos Estocásticos (Markov Games)
Los **Juegos Estocásticos** (Shapley, 1953) extienden los Procesos de Decisión de Markov (MDPs) al ámbito de múltiples agentes interactivos. Se definen formalmente mediante la tupla:
$$SG = \langle P, S, A, T, R, \gamma, \mu \rangle$$

Donde:
*   $P = \{1, \dots, n\}$ es el conjunto de agentes.
*   $S$ es el conjunto de estados del entorno.
*   $A = A_1 \times \dots \times A_n$ es el espacio de **acciones conjuntas**.
*   $T : S \times A \times S \to [0, 1]$ es la función de transición de probabilidad del entorno, tal que $\sum_{s' \in S} T(s' \mid s, a) = 1$ para todo $s \in S, a \in A$.
*   $R = (R_1, \dots, R_n)$ es el vector de funciones de recompensa, donde $R_i : S \times A \times S \to \mathbb{R}$ es la recompensa inmediata del agente $i$.
*   $\gamma \in [0, 1)$ es el factor de descuento temporal.
*   $\mu : S \to [0, 1]$ es la distribución de probabilidad de los estados iniciales.

> 💡 **Jerarquía de Modelos:**
> *   Un juego en forma normal repetido es un Juego Estocástico con **un único estado** ($|S| = 1$).
> *   Un MDP clásico es un Juego Estocástico con **un único agente** ($|P| = 1$).

---

## 2. Independent Q-Learning (IQL)
Propuesto por Ming Tan en 1993, **IQL** es el enfoque más simple para resolver tareas multiagente con aprendizaje por refuerzo.

### A. Intuición teórica
Cada agente $i$ aprende una función de valor local $Q_i(s, a_i)$ que evalúa únicamente sus propias acciones $a_i \in A_i$ en cada estado $s$.
El agente **ignora completamente la existencia de los demás agentes**, tratándolos como parte del entorno físico (ruido ambiental).

### B. Regla de Actualización de Q-Values
En cada paso del episodio, tras elegir $a_i$ en el estado $s$, observar la recompensa local $r_i$ y el siguiente estado $s'$, el agente $i$ actualiza su tabla local mediante la fórmula tradicional de Q-Learning:
$$Q_i(s, a_i) \leftarrow Q_i(s, a_i) + \alpha \left[ r_i + \gamma \max_{a'_i \in A_i} Q_i(s', a'_i) - Q_i(s, a_i) \right]$$

### C. Selección de Acciones
Se adopta una política de exploración $\epsilon$-greedy sobre la tabla local:
*   Con probabilidad $\epsilon$, elige una acción uniforme al azar: $a_i \sim U(A_i)$.
*   Con probabilidad $1 - \epsilon$, elige la acción codiciosa local:
$$a_i^t = \arg\max_{a'_i \in A_i} Q_i(s, a'_i)$$

### D. Pros y Contras de IQL
*   🟩 **Ventajas:**
    1.  **Simplicidad extrema:** Es idéntico a implementar Q-learning de un solo agente para cada jugador de forma aislada.
    2.  **Excelente Escalabilidad:** El tamaño de la tabla Q de cada agente crece linealmente con sus propias acciones $|A_i|$, evitando la explosión exponencial del espacio de acciones conjuntas.
*   🟥 **Desventajas:**
    1.  **No Estacionariedad del Entorno:** Dado que los oponentes también están aprendiendo y modificando sus políticas en paralelo, las transiciones y recompensas desde el punto de vista del agente $i$ varían en el tiempo.
    2.  **Falta de Garantías:** Se rompe la propiedad de Markov del entorno, por lo que **no se garantiza la convergencia a un Equilibrio de Nash**. Puede exhibir inestabilidades y oscilaciones cíclicas permanentes.

---

## 3. Joint-Action Learning con Agent Modeling (JAL-AM)
Propuesto por Claus y Boutilier en 1998, **JAL-AM** aborda directamente la no estacionariedad modelando explícitamente a los rivales.

### A. Intuición teórica
El agente $i$ mantiene una tabla Q sobre las **acciones conjuntas**: $Q_i(s, a) = Q_i(s, (a_i, a_{-i}))$.
Para decidir qué acción individual tomar sin controlar a los oponentes, el agente $i$ construye y actualiza un modelo de creencias empíricas $\pi_j(a_j \mid s)$ sobre la estrategia de cada oponente $j \neq i$ en cada estado $s$.

### B. Modelado del Oponente (Agent Modeling)
Sea $C_{i,j}(s, a_j)$ la cantidad de veces que el agente $i$ ha observado al oponente $j$ jugar la acción $a_j$ en el estado $s$.
La estimación marginal de la política del rival en el estado $s$ es:
$$\pi_j(a_j \mid s) = \frac{C_{i,j}(s, a_j)}{\sum_{a'_j \in A_j} C_{i,j}(s, a'_j)}$$

Bajo la hipótesis de independencia, la probabilidad conjunta de las acciones del resto es:
$$\pi_{-i}(a_{-i} \mid s) = \prod_{j \neq i} \pi_j(a_j \mid s)$$

### C. Valor Promedio / Esperado de la Acción (Average Value)
El agente $i$ calcula el valor esperado de jugar su acción individual $a_i$ en el estado $s$ promediando los Q-values de la acción conjunta ponderados por sus creencias:
$$AV_i(s, a_i) = \sum_{a_{-i} \in A_{-i}} Q_i(s, (a_i, a_{-i})) \pi_{-i}(a_{-i} \mid s)$$

### D. Selección de Acciones
Se realiza exploración $\epsilon$-greedy sobre los valores promedio:
*   Con probabilidad $\epsilon$, elige $a_i \sim U(A_i)$.
*   Con probabilidad $1 - \epsilon$, elige:
$$a_i^t = \arg\max_{a'_i \in A_i} AV_i(s, a'_i)$$

### E. Regla de Actualización de Q-Values
Tras observar la acción conjunta real jugada $a^t = (a_i^t, a_{-i}^t)$, la recompensa $r_i$ y el nuevo estado $s'$, el agente $i$ actualiza la tabla de la acción conjunta:
$$Q_i(s, a^t) \leftarrow Q_i(s, a^t) + \alpha \left[ r_i + \gamma \max_{a'_i \in A_i} AV_i(s', a'_i) - Q_i(s, a^t) \right]$$

---

## 4. Resumen Comparativo de IQL vs. JAL-AM

| Dimensión | Independent Q-Learning (IQL) | Joint-Action Learning (JAL-AM) |
| :--- | :--- | :--- |
| **Entrada de la Tabla Q** | Solo estado y acción local: $Q_i(s, a_i)$ | Estado y acción conjunta: $Q_i(s, (a_i, a_{-i}))$ |
| **Tamaño de la Tabla Q** | Pequeña ($|S| \times |A_i|$) | Exponencial ($|S| \times \prod_p |A_p|$) |
| **Modelado del Rival** | No. Ignora a los demás. | Sí. Estima probabilidades $\pi_{-i}(a_{-i} \mid s)$ vía conteo de acciones. |
| **Criterio de Decisión** | Maximizar $Q_i(s, a_i)$ | Maximizar valor promedio $AV_i(s, a_i)$ |
| **Adaptación a No Estacionariedad**| Lenta y pasiva. | Activa mediante la actualización de las creencias empíricas. |
| **Escalabilidad en Agentes ($N$)** | Muy alta. | Muy baja (sufre la maldición de la dimensionalidad). |
