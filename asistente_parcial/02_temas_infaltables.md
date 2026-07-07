# 🎯 Temas infaltables (con teoría + cómo se contesta)

Ordenados por probabilidad de que caigan. Para cada uno: la teoría mínima imprescindible y la
**receta de respuesta** que esperan los docentes.

---

## A. Función de evaluación  🔴 CAE SIEMPRE

### Qué es
Cuando el árbol de juego es demasiado grande para llegar a las hojas, se **corta a una profundidad
máxima** y, en los nodos no terminales donde se agota la profundidad, se sustituye la utilidad real
por una **estimación**: la función de evaluación `Eval(s)`.

### Forma canónica (memorizar)
Para juegos de **suma cero**, se define como una **suma lineal de features**, contrapuestas
agente vs. oponente:

$$\text{Eval}(s) = \sum_i c_i \,\big(E_i(\text{agente}, s) - E_i(\text{oponente}, s)\big)$$

- `Eᵢ` = una característica medible del estado (p.ej. en ajedrez: nº de damas, de torres…; en
  Ta-Te-Ti: nº de líneas potencialmente ganadoras).
- `cᵢ` = peso (puede ser **negativo** si tener más de esa feature es *malo*).
- La estructura agente − oponente hace que las features que ambos tienen **se cancelen** (si los dos
  tienen dama, no aporta), lo cual es coherente con suma cero.

### Las 3 propiedades de una "buena función de evaluación" (ESTO es lo que piden demostrar)
1. **Ordena correctamente los estados finales:** `Eval(win) ≥ Eval(draw) ≥ Eval(loss)`. Es decir,
   ordena los finales igual que la **Utilidad** (1, 0, −1 en suma cero).
2. **Es barata de computar:** su costo debe ser **muy inferior** al de evaluar el subárbol que
   reemplaza (si no, no sirve de atajo).
3. **Está fuertemente correlacionada con la probabilidad real de ganar.** Esto NO se prueba a mano:
   se **valida simulando** (si el agente mantiene `Eval` siempre estrictamente positiva en un episodio,
   gana).

### ⚠️ El detalle que separa el 7 del 10: la normalización
La propiedad 1 puede **fallar** porque los árboles están desbalanceados: podés tener que comparar un
**estado final** (utilidad ∈ {−1,0,1}) con un **estado no final** evaluado por `Eval` (que podría dar
100). Si `Eval` no está acotada, un estado intermedio "bueno" podría puntuar más que un final
ganador → error. Soluciones:
- **Normalizar** `Eval` al rango `(−1, 1)`, para que cualquier estado intermedio quede *entre* perder
  y ganar.
- O usar un **`if`**: `if s es final: return Utilidad(s); else: return Eval(s)`.
- O agregar un término dominante (peso "astronómico", `±∞`) que se active solo en finales.

### Receta de respuesta (plantilla)
> 1. Identifico el objetivo del juego (¿gana el que tiene más puntos? ¿el que captura más? ¿el que
>    NO completa la línea?).
> 2. Si es **por puntos**, la base trivial es `Eval = puntos_agente − puntos_oponente` (ordena finales
>    por definición). Si no, elijo features que aproximen "estar cerca de ganar".
> 3. Escribo `Eval(s) = Σ cᵢ (Eᵢ(ag) − Eᵢ(op))` con al menos 2 features independientes (lo piden
>    explícito en 2022/2023).
> 4. **Demuestro propiedad 1:** muestro que en win `Eval≥0`, draw `Eval=0`, loss `Eval≤0` (y hablo de
>    normalización para comparar con finales).
> 5. Menciono propiedades 2 (barata, computable incremental) y 3 (correlación, validable por simulación).

### Ejemplo modelo — Ta-Te-Ti
`Eval(s) = (#líneas potencialmente ganadoras de X) − (#líneas potencialmente ganadoras de O)`, donde
una "línea potencialmente ganadora" para X es una fila/columna/diagonal **sin ninguna O**. Normalizada
por 1/8 (hay 8 líneas). Ordena finales: ganar deja líneas completas a favor, perder lo contrario.
→ Ver también Blokus en [01](01_analisis_parciales.md) (`Eval = C_o − C_a`).

---

## C. Minimax, Expectimax y poda α-β  🔴 CAE CASI SIEMPRE

### Minimax (suma cero, 2 jugadores alternados, info perfecta)
$$V(s) = \begin{cases}
\text{Utilidad}(s) & s \text{ terminal}\\
\max_{a} V(\text{Suc}(s,a)) & \text{Player}(s) = \text{MAX (agente)}\\
\min_{a} V(\text{Suc}(s,a)) & \text{Player}(s) = \text{MIN (oponente)}
\end{cases}$$

Con profundidad limitada, se reemplaza el caso terminal por: si `profundidad = 0`, devolver `Eval(s)`.

### Expectimax / nodos de azar (chance)
Cuando hay **azar** (dados, monedas, oponente que juega al azar), se agregan **nodos chance** que
**promedian** por la probabilidad:
$$V(\text{chance}) = \sum_{r} P(r)\, V(\text{Suc}(s, r))$$

- **Expectiminimax** = mezcla de niveles MAX, MIN y CHANCE (típico de Backgammon: MAX → chance(dados)
  → MIN → chance).
- Si el oponente NO es adversarial sino aleatorio (p.ej. "elige con 0.5"), su nodo se trata como
  **chance**, no como MIN.

### Poda alfa-beta (α-β)
- Permite **no explorar** ramas que no pueden cambiar la decisión. Es **exacta**: da el mismo valor
  que minimax, sin aproximar.
- `α` = mejor (mayor) cota inferior garantizada para MAX en el camino; `β` = mejor (menor) cota
  superior para MIN. **Se poda cuando `α ≥ β`** (la intersección de `[≥α]` y `[≤β]` es vacía o un punto).
- **Depende del orden** de recorrido: con buen orden poda mucho más (por eso se ordenan las acciones,
  a veces aleatoriamente para no ser predecible).
- Se puede **combinar** con función de evaluación (α-β sobre valores estimados): perdés exactitud pero
  ganás velocidad.

### Receta para un ejercicio de árbol
> 1. Identificar el **tipo de juego** (suma cero, alternado, con/sin azar, info perfecta/imperfecta).
> 2. Etiquetar nodos: MAX (agente), MIN (oponente), CHANCE (azar/aleatorio).
> 3. Escribir la **recurrencia** correspondiente.
> 4. Resolver de las hojas hacia arriba (inducción hacia atrás), promediando en los chance.
> 5. Indicar la **acción/estrategia** que elige el agente en la raíz (el `argmax`).

---

## B. Modelado de juegos secuenciales / alternados  🔴 ALTA

Un juego alternado se modela con la tupla de: **jugadores `P`**, **estados `S`** (con `s_init`),
**acciones `A`**, **función sucesor `Suc(s,a)`**, **función `Player(s)`** (quién juega en `s`),
**regla de fin** y **`Utilidad`** en los terminales.

Casos clásicos que ya cayeron:
- **Orden de turno variable (Uno):** lo único que cambia es `Player(s)`, que pasa a depender de
  variables del estado (`sense`, `last-player`, `top-card`). La definición de `V_π` **no cambia**.
- **Reducción multiagente → 2 jugadores (Pacman):** componer todos los agentes adversarios
  inteligentes en un único jugador `G` cuya acción es el **vector** de acciones individuales; los
  agentes aleatorios pasan a ser **parte del estado**. Así un juego de N agentes se resuelve con
  minimax de 2 jugadores manteniendo suma cero.

> 💡 **Alternativa: Maxn (`Sistemas_multiagente_11.pdf`).** En vez de reducir a 2 jugadores, se puede
> generalizar minimax directamente a N: cada nodo devuelve un **vector** de N utilidades (una por
> jugador) y el jugador que mueve en ese nodo elige la acción que maximiza **su propia** componente del
> vector. Solo funciona bien con poda superficial (no hay poda profunda como en α-β de 2 jugadores,
> porque maximizar mi componente no me da cota sobre las componentes ajenas). Útil si te piden modelar
> un juego de 3+ jugadores *sin* reducirlo a 2 (ver Ejercicios 2, problema 4).

### Receta
> Definir explícitamente: jugadores, estado (qué variables guarda y por qué), `s_init`, acciones,
> `Suc`, `Player`, regla de fin, `Utilidad`. Ejemplificar con un estado concreto.

---

## D. Juegos en forma normal — Nash, dominancia, Pareto  🟡 MEDIA (clave en 2020)

### Definiciones que hay que tener
- **Juego en forma normal:** `Γ = ⟨P, A, R⟩` (jugadores, acciones conjuntas, recompensas).
- **Estrategia mixta** `π_p ∈ Δ(A_p)`: distribución sobre acciones. Pura = un punto.
- **Mejor respuesta (BR):** `π_p` maximiza el valor esperado dado `π_{-p}`. **Siempre existe una BR pura.**
- **Equilibrio de Nash (EN):** cada jugador juega BR del resto; nadie gana desviándose
  unilateralmente. **Teorema de Nash:** todo juego finito tiene al menos un EN (puro o mixto).
- **Dominancia:** `a` domina **estrictamente** a `b` si da más utilidad ante *toda* acción del rival;
  **débilmente** si da ≥ siempre y > en al menos un caso. Eliminación iterativa: **IDSDS** (estricta),
  **IDWDS** (débil).
- **Óptimo de Pareto:** un perfil es Pareto superior a otro si **nadie está peor y alguien mejor**.
- **Suma cero + Teorema Minimax (von Neumann):** `max_{π1} min_{π2} V = min_{π2} max_{π1} V = V*`.
  Todo perfil que resuelve el minimax es EN; todos los EN tienen el mismo valor `V*`.

### El argumento estándar que esperan ("¿qué harán los jugadores?")
> Por **racionalidad individual**, los jugadores van al **Equilibrio de Nash**. Pero a menudo existe
> un perfil **Pareto superior** que NO es EN: por **racionalidad colectiva** ambos estarían mejor ahí,
> pero no es estable porque alguien tiene incentivo a desviarse. → Este es el corazón del **dilema del
> prisionero** (Ventas fraudulentas 2020) y del Litigio.

### Cómo encontrar EN mixto en un 2×2 (punto de silla / indiferencia)
Igualar los pagos esperados del rival ante cada una de sus acciones para hallar la probabilidad que lo
deja **indiferente**. Ej. (Cajas/Genio): para `p` = prob. de B jugar L, planteás
`−1·p + 0·(1−p) = (2/3)·p − (1/3)·(1−p)` → `p = 1/6`. (Ver worked example en [03](03_preguntas_tipo_y_simulacro.md#cajas).)

---

## E. Defensa del obligatorio  🔴 ALTA (puntos "regalados" si lo preparás)

Tu obligatorio 2026 implementa **4 algoritmos** (más una variante) sobre **N agentes** en el marco
formal de **Juegos Estocásticos** (`Sistemas_multiagente_7.pdf`), y los valida en varios ambientes.
Tenés que poder **describir cada algoritmo, su objetivo y los resultados/convergencias observadas**.

### El marco: Juego Estocástico (Markov Game)
$$SG = \langle P, S, A, T, R, \gamma, \mu \rangle$$
`P` agentes, `S` estados (con `EsFinal: S→𝔹`), `A = A_1×…×A_n` acciones conjuntas, `T` transición,
`R: S×A×S→ℝⁿ` recompensas, `γ` descuento, `μ` distribución inicial. Una **historia**
`h_t = s⁰a⁰…s^{t-1}a^{t-1}s^t` es una secuencia jugada; un **episodio** es una historia que termina en
`EsFinal`. El valor de agente `i` se define recursivamente vía `Q_i(h,a)` — misma lógica que un MDP,
pero con acción **conjunta**.

### Los algoritmos (resumen para defender)

| Algoritmo | Qué observa | Idea | Converge a… |
| :--- | :--- | :--- | :--- |
| **Fictitious Play (FP)** | Acciones de todos (agent modeling) + su matriz completa | Asume rival estacionario; estima su mixta por **frecuencia histórica** y juega **mejor respuesta** | EN en suma-cero 2p, juegos de potencial y resolubles por dominancia (puede ciclar — Shapley) |
| **Regret Matching (RM)** | Su estrategia + su vector de **regrets** | Juega proporcional a los **regrets positivos acumulados** | El **promedio** converge a **Equilibrio Correlacionado** (= EN en suma-cero 2p) |
| **IQL** (Independent Q-Learning) | Solo su `(s, aᵢ, rᵢ, s')` | Q-learning ignorando a los demás (rivales = entorno): `Q_i(s,a_i) ← Q_i(s,a_i) + α[r_i + γ·max Q_i(s',·) − Q_i(s,a_i)]` | **Sin garantías** (entorno no estacionario); simple y escalable |
| **JAL-GT** (Joint-Action Learning, teoría de juegos) | Acción conjunta `a=(a_i,a_{-i})` | Mantiene `Q_j(s,a)` para todos; en cada estado arma el juego en forma normal `Γ_s` dado por los Q-values y lo **resuelve** (`Solve(Γ_s)`→ un equilibrio); ej. **Minimax-Q** (Littman 1994) para suma-cero 2p | Prescribe cómo comportarse *en equilibrio*; no siempre aprendible solo con `Q_i(s,a)` |
| **JAL-AM** (Joint-Action Learning, agent modeling) | Acción conjunta + modela al rival | Q sobre **acción conjunta** + creencia empírica `π_{-i}(a_{-i}\|s)`; decide por **valor promedio** `AV_i(s,a_i) = Σ_{a_{-i}} Q_i(s,(a_i,a_{-i}))·π_{-i}(a_{-i}\|s)` | Mejor ante no-estacionariedad que IQL; **explota exponencialmente** con N (tabla sobre acción conjunta) |

> Tu obligatorio pide específicamente **FP, RM, IQL y JAL-AM** — si mencionás JAL-GT es para mostrar que
> entendés que es la variante "resuelve el juego" de la que JAL-AM es la variante "modela empíricamente al rival".

### Ambientes de validación (saber qué EN se espera en cada uno)
- **Matching Pennies (MP):** suma cero, EN mixto `(½,½)`, valor 0.
- **Rock-Paper-Scissors (RPS):** suma cero, EN mixto `(⅓,⅓,⅓)`, valor 0.
- **Blotto:** asignación de recursos.
- **Foraging:** recolección; recompensa **0 salvo al final** (episodios largos → conecta con el problema
  de profundidad de minimax).

### Qué gráficas mostrar (pedido explícito del docente en clase)
1. **Evolución de la recompensa/retorno promedio** por episodio.
2. **Distancia a la política de equilibrio conocida** a lo largo del tiempo (si conocés el EN de MP/RPS,
   graficá `‖π̂_t − π*‖` — debería tender a 0 si converge).
3. ⚠️ **Histograma de las acciones realmente jugadas vs. la política *promedio* aprendida.** Ojo con
   este punto: en Regret Matching, la acción jugada en el instante `t` se **muestrea** de `π̂_t` (la
   política *actual*, que puede estar concentrada en una sola acción por un rato), mientras que lo que
   converge al Equilibrio Correlacionado es el **promedio** `π̄_t`. Si solo mirás la acción jugada podés
   creer erróneamente que "no converge" — hay que aclarar esta distinción si te preguntan.
4. Comparaciones cruzadas: FP vs FP, FP vs RM, FP vs Random, IQL vs IQL, JAL-AM vs IQL, etc.
5. En Foraging: variar cantidad de agentes (2 vs 3) y tamaño de tablero, comparar curvas de IQL vs JAL-AM.

### Qué decir de los resultados (esquema)
> "Enfrenté FP vs FP, FP vs RM, FP vs Random, IQL vs IQL, etc. En MP y RPS las **frecuencias empíricas
> convergen al EN mixto uniforme** (gráfica de probabilidades → ⅓/⅓/⅓). RM converge en promedio al EN
> (aclarando la diferencia entre política actual y promedio). IQL muestra **oscilaciones** por
> no-estacionariedad. JAL-AM se adapta mejor pero no escala. Mostré la convergencia con gráficas de
> evolución de estrategias y distancia al equilibrio conocido."

> ⚠️ Releé **tu** informe y tus gráficas antes del parcial: la pregunta E es sobre **tus** números.
> Repo de los algoritmos: `obligatorio/obligatorio_sanes_guerra/agents/` y `run.ipynb`.

---

## F. Monte Carlo Rollout / MCTS  🟡 MEDIA (nuevo, `Sistemas_multiagente_10.pdf`)

Alternativa a diseñar `Eval(s)` a mano: **estimar el valor simulando**.

- **Rollout:** desde el estado a evaluar, jugar una partida completa siguiendo una **política simple**
  (a menudo aleatoria) hasta un estado terminal, y usar la utilidad real obtenida como estimación del
  valor. Se puede promediar sobre muchas simulaciones para reducir varianza.
- **MCTS (Monte Carlo Tree Search):** construye incrementalmente un árbol parcial mediante 4 fases,
  repetidas muchas veces:
  1. **Selección:** bajar por el árbol ya construido eligiendo hijos según una fórmula que balancea
     explotar (buen valor estimado) y explorar (poco visitado) — típicamente **UCT**:
     $$UCT(s,a) = \bar{V}(s,a) + c\sqrt{\frac{\ln N(s)}{N(s,a)}}$$
     (`V̄` = valor promedio estimado, `N(s)` visitas al nodo, `N(s,a)` visitas a esa acción, `c` constante
     de exploración).
  2. **Expansión:** agregar al árbol un nuevo nodo hijo no visitado.
  3. **Simulación (rollout):** desde ese nuevo nodo, jugar hasta el final con una política simple.
  4. **Backpropagation:** propagar el resultado hacia la raíz, actualizando `N` y `V̄` de cada nodo en el camino.
- **Por qué importa para el parcial:** es una respuesta válida (y distinta a diseñar features a mano) a
  "¿cómo evaluarías un estado sin una función de evaluación manual?" — mencionalo como alternativa
  cuando un juego sea demasiado complejo para features simples (fue la base de AlphaGo, mencionado en
  la Clase9 junto a la función de evaluación clásica de ajedrez de Turing).

---

## G. CFR — Counterfactual Regret Minimization  🟡 MEDIA-ALTA (nuevo, `Sistemas_multiagente_12.pdf`)

Generaliza **Regret Matching** (que opera sobre un único estado/forma normal) a **árboles de juego con
información imperfecta** (conjuntos de información), como Kuhn Poker.

- **Idea central:** en vez de un regret global, se lleva un **Regret Matching independiente por cada
  conjunto de información (infoset)**, y el arrepentimiento se pondera por la probabilidad
  **contrafactual** de llegar a ese infoset (la probabilidad de alcanzarlo asumiendo que el jugador en
  cuestión *sí* intenta llegar, ignorando sus propias probabilidades de elección en el camino).
- **Chance sampling:** para reducir cómputo, en cada iteración se muestrea solo una realización de los
  nodos de azar (en vez de recorrer todas), y se actualizan los regrets a lo largo de ese único camino muestreado.
- **Garantía:** el promedio de las estrategias converge a **Nash en juegos de suma cero de 2 jugadores**
  con información imperfecta (la misma garantía de RM, pero llevada a la forma extensiva).
- **Conexión directa con el parcial:** es la herramienta correcta cuando un ejercicio dice *"¿qué pasa
  si los jugadores no conocen las utilidades del otro?"* (ver Entrada al Mercado, parcial 2023, y la
  discusión completa en la conversación sobre CFR — resumen: CFR ⟺ RM por info-set con regret
  contrafactual, garantía fuerte solo en suma-cero 2p, en general-sum el promedio converge a un
  equilibrio grueso correlacionado (CCE) y no necesariamente a Nash).
