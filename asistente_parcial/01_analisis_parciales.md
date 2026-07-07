# 📋 Análisis de los parciales (2020 → 2023)

Desglose ejercicio por ejercicio. Para cada uno: **tema**, **qué se pide** y **enfoque de
resolución**. Los tipos (A–E) son los de la tabla del [README](README.md#-veredicto-rápido-qué-estudiar-sí-o-sí).

---

## 🗓️ Parcial 2020 — Letra 1 (17/12/2020)

| Ej | Juego / contexto | Tipo | Qué pide |
| :-: | :--- | :--- | :--- |
| 1 | **Uno** (cartas que cambian el orden de turno) | **B** | Qué cambia en la formulación; cómo modelar estados y la función `Player`. Ejemplificar. |
| 2 | **Blokus** | **A** | Definir función de evaluación y **verificar que es buena**. |
| 3 | **Ventas fraudulentas** (matriz 2×2) | **D** | ¿Qué hará el usuario? Justificar (Nash + Pareto). |
| 4 | **Cajas** (C1,C2,C3 + Genio) | **C** | Calcular valor del juego con **Minimax** y **Expectimax**; qué caja elige A. |

**Claves de resolución:**
- **Ej1 (Uno):** la formulación matemática de `V_π` NO cambia. Lo que cambia es la función
  `Player(s)`, que deja de ser "el siguiente" y pasa a depender de variables del estado: `sense`
  (sentido de giro ±1), `last-player` y `top-card`. Casos: *saltar* → `(last-player + 2·sense) mod N`;
  *jugar de nuevo* → `last-player`; *dar vuelta* → se invierte `sense` en `Suc`; default →
  `(last-player + 1·sense) mod N`. (Solución oficial en `parciales/Parciales 1 y 2 - Soluciones.pdf`.)
- **Ej2 (Blokus):** `Eval(s) = C_o(s) − C_a(s)` (cuadrados sin colocar del oponente menos los del
  agente). Se demuestra que ordena igual que la utilidad: win → Eval≥0, draw → Eval=0, loss → Eval≤0.
- **Ej3:** es un **dilema del prisionero** disfrazado. El único EN es **(Falso, Falso) = (−10,−10)**;
  (Real, Real) = (10,10) es **Pareto superior pero no es EN**. Racionalidad individual ⇒ ambos
  hacen trampa.
- **Ej4 (Cajas):** ver worked example completo en [03](03_preguntas_tipo_y_simulacro.md#cajas).

---

## 🗓️ Parcial 2020 — Letra 2 (17/12/2020)

| Ej | Juego / contexto | Tipo | Qué pide |
| :-: | :--- | :--- | :--- |
| 1 | **Pacman** (1 Pacman, N ghosts inteligentes + random) | **B** | Plantear como Minimax de **2 jugadores** (acciones, jugadores, estados, utilidades). |
| 2 | **Blokus** | **A** | Igual que Letra 1. |
| 3 | **Litigio** (Andrea/Bettina) | **D** | ¿Qué harán? Nash + dominancia + Pareto. |
| 4 | **Cajas** (otros números) | **C** | Minimax vs Expectimax. |

**Claves:**
- **Ej1 (Pacman):** reducción multiagente → 2 jugadores. `P` = Pacman; `G = (g1,…,gN)` =
  composición de **todos los fantasmas inteligentes** (juegan "simultáneamente", acción de G = vector
  de acciones). Los fantasmas **random son parte del estado, no jugadores**. Utilidad de suma cero:
  comen a Pacman ⇒ `Σ 1/N = 1` para G; gana Pacman ⇒ 1 para P; random come a Pacman ⇒ empate (0).
- **Ej3 (Litigio):** dos EN — (70-30, R) y (80-20, R). **80-20 domina débilmente** para Andrea;
  Bettina rechaza. Pero (50-50, A) es **Pareto superior** (racionalidad colectiva) y no es EN.
- Mismo molde que Letra 1: 1 modelado + 1 eval + 1 forma normal + 1 minimax/expectimax.

---

## 🗓️ Parcial 2021 (09/12/2021)

| Ej | Juego / contexto | Tipo | Qué pide |
| :-: | :--- | :--- | :--- |
| 1 | **Notakto** (Ta-Te-Ti de "miseria") | **A + C** | (1) Eval que ordene los finales; (2) argumentar que con MiniMax el primer jugador gana (árbol). |
| 2 | **Backgammon** | **C + A** | (1) Tipo de juego + recurrencia MiniMax **con azar** + árbol de 2 turnos; (2) eval paramétrica motivada. |
| 3 | **Notakto multi-tablero** (OPCIONAL) | **A** | Eval apropiada + argumento. |

**Claves:**
- **Ej1 (Notakto):** juego de *miseria* (el que completa una línea **pierde**). La eval debe penalizar
  acercarse a completar líneas. Hay que **argumentar la estrategia ganadora** (X en el centro + salto
  de caballo) desarrollando parte del árbol y mostrando que la eval la "elige".
- **Ej2 (Backgammon):** es un **juego estocástico de 2 jugadores de suma cero** (hay azar = dados).
  Recurrencia = **Expectiminimax**: niveles MAX, MIN y **nodos de azar (chance)** que promedian por la
  probabilidad de cada tirada. El árbol de 2 turnos debe mostrar: MAX → chance(dados) → MIN → chance.
  La eval paramétrica: combinación lineal de features (fichas afuera, fichas comidas en la barra,
  fichas solas/vulnerables, torres/bloques). **No** piden demostrar que es buena, solo motivarla.

---

## 🗓️ Parcial 2022 (15/12/2022)

| Ej | Juego / contexto | Tipo | Qué pide |
| :-: | :--- | :--- | :--- |
| 1 | **Puntos y Cuadrados** (Dots & Boxes 3×3) | **A + C** | Eval paramétrica con **≥2 funciones básicas independientes**; demostrar que ordena finales; aplicarla variando **profundidad (1 y 2)** usando **simetrías**. |
| 2 | **Kuhn Poker** | **C** | Dibujar el árbol; calcular valores **minimax** y estrategia del agente. |
| 3 | **Defensa del obligatorio** | **E** | Describir las funciones de evaluación usadas, objetivos y resultados. |

**Claves:**
- **Ej1:** "**dos funciones básicas independientes**" → p.ej. `f1 = cuadrados cerrados por agente −
  por oponente` y `f2 = − (lados que dejan un cuadrado a 3 lados, o sea que regalan punto)`. Hay que
  ponderarlas `Eval = c1·f1 + c2·f2`. La parte de **profundidad 1 vs 2** muestra cómo cambia la
  decisión al ver más adelante; las **simetrías** reducen el árbol (tableros equivalentes por rotación/reflexión).
- **Ej2 (Kuhn):** árbol con información imperfecta (cada uno ve solo su carta). Para minimax se arma el
  árbol de las acciones pasar/apostar con las hojas según la tabla de resultados.

---

## 🗓️ Parcial 2023 (06/12/2023)

| Ej | Juego / contexto | Tipo | Puntos | Qué pide |
| :-: | :--- | :--- | :-: | :--- |
| 1 | **Pente** (capturas, 12×12) | **A** | 12 | Eval paramétrica de **≥2 sumandos** + probar que es buena; **evaluar una jugada concreta** (fila 2, col 5) y decir dónde jugaría. |
| 2 | **Entrada al mercado** (Empresa vs Monopolio + moneda) | **C + D** | 12 | (1) Árbol + valor del juego con `p=0.5`, info completa; (2) qué cambia si **no** conocen las utilidades + **qué algoritmo** usar. |
| 3 | **Defensa del obligatorio** (Kuhn2, Kuhn3, Leduc) | **E** | 6 | Resultados con cada algoritmo (partes A y B) + qué hizo en la parte C. |

**Claves:**
- **Ej1 (Pente):** eval con al menos 2 sumandos, p.ej. `c1·(pares propios capturables del rival) +
  c2·(capturas acumuladas) − (lo simétrico para el rival)`. Lo nuevo es **evaluar una jugada
  específica**: calcular Eval antes/después y justificar si mejora.
- **Ej2 (mercado):** chance node (moneda h/t con p,1−p) al inicio → **Expectiminimax**. Con `p=0.5` se
  resuelve por inducción hacia atrás y se promedia. La parte 2 (no conocen utilidades) = **información
  incompleta** → juego Bayesiano / o aprender al rival (FP / RL). Worked example en
  [03](03_preguntas_tipo_y_simulacro.md#entrada-al-mercado).
- **Ej3:** ⚠️ Esa edición usaba un obligatorio de **poker (Kuhn/Leduc + CFR)**. El **tuyo (2026)** es
  **FP/RM/IQL/JAL en MP/RPS/Blotto/Foraging** → adaptá esta defensa a tus algoritmos y resultados.

---

## 🔬 Patrones que se repiten (lo que el cruce deja claro)

1. **La función de evaluación es el corazón del parcial.** Siempre hay que (a) definirla paramétrica
   como suma lineal de features `Eval(s) = Σ cᵢ·(Eᵢ(agente,s) − Eᵢ(oponente,s))` y (b) **demostrar que
   es buena** (ordena finales win ≥ draw ≥ loss). Saber esto de memoria.
2. **Los juegos siempre son nuevos / inventados** (Uno, Blokus, Notakto, Pente, Dots & Boxes…). No
   importa el juego: importa aplicar **el mismo método**. No hay que "saberse" los juegos.
3. **Suma cero + alternados** es el marco dominante; el azar (dados, monedas) aparece seguido →
   **Expectiminimax / nodos chance**.
4. **Forma normal (Nash/dominancia/Pareto)** aparece como "¿qué harán los jugadores?" con una matriz,
   y la respuesta casi siempre contrasta **racionalidad individual (EN) vs colectiva (Pareto)**.
5. **La defensa del obligatorio vale puntos fijos** y es de las preguntas más fáciles de preparar
   *de antemano* porque depende de tu propio trabajo.
