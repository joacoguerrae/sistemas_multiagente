# 🧪 Preguntas tipo + simulacro

Dos partes: (1) **soluciones trabajadas** de los ejercicios recurrentes clave, y (2) un **simulacro de
parcial** nuevo para practicar.

---

# Parte 1 — Soluciones trabajadas

## <a name="cajas"></a>🔢 Cajas (Minimax vs Expectimax con subjuego de azar) — *Parcial 2020*

**Enunciado (Letra 1):** Cajas `C1={−5,15}`, `C2={30,−12}`, `C3={−16,48}`. A elige caja (MAX), luego B.
En C1 y C3, B elige un número. En C2 hay un Genio: B juega un **juego de suma cero** contra él y usa la
estrategia que **maximiza** el valor. Matriz de B (filas) vs Genio (columnas):

|  | Genio L | Genio R |
|:-:|:-:|:-:|
| **B: L** | 1 | −2/3 |
| **B: R** | 0 | 1/3 |

### Paso 1 — Valor del subjuego C2 (punto de silla)
Sea `p` = prob. de B jugar L. B busca su mixta de equilibrio; iguala el pago del Genio:
$$-1\cdot p + 0\cdot(1-p) \;=\; \tfrac{2}{3}p - \tfrac{1}{3}(1-p) \;\Rightarrow\; p = \tfrac{1}{6}$$
Estrategia de B: `(1/6, 5/6)`. **Valor del juego en C2:** `(1/6)·1 + (5/6)·0 = 1/6 ≈ 0.167`.
(Este valor es el mismo en minimax y expectimax porque B juega Nash contra el Genio en ambos casos.)

### Paso 2 — Minimax (B es adversario en C1, C3 → elige el mínimo)
- `V(C1) = min(−5, 15) = −5`
- `V(C2) = 1/6`
- `V(C3) = min(−16, 48) = −16`
- A maximiza: `max(−5, 1/6, −16) = 1/6` → **A elige C2. Valor minimax = 1/6.**

### Paso 3 — Expectimax (B aleatorio 0.5/0.5 en C1, C3)
- `V(C1) = 0.5·(−5) + 0.5·15 = 5`
- `V(C2) = 1/6` (sigue siendo Nash contra el Genio)
- `V(C3) = 0.5·(−16) + 0.5·48 = 16`
- A maximiza: `max(5, 1/6, 16) = 16` → **A elige C3. Valor expectimax = 16.**

**Moraleja:** la *misma* situación cambia totalmente la decisión de A según se modele al oponente como
**adversarial (MIN)** o **aleatorio (CHANCE)**. Eso es exactamente lo que evalúa el ejercicio.

> Verificación con la Letra 2 (números distintos): `C1={−6,14}`, `C2={50,−20}`, `C3={−15,55}`, matriz
> B `[[0,3],[1,−1]]`. Practicá: hallá el valor de silla de C2 y repetí los pasos 2 y 3.

---

## <a name="normal-form"></a>🧮 Forma normal: "¿qué harán?" (Ventas fraudulentas) — *Parcial 2020*

Matriz (Comprador filas, Vendedor columnas):

|  | Entrega Falso | Entrega Real |
|:-:|:-:|:-:|
| **Paga Falso** | −10, −10 | 50, −50 |
| **Paga Real** | −50, 50 | 10, 10 |

### Resolución
- **Es un dilema del prisionero.** Para el comprador, *Pagar Falso* domina (gana más ante cualquier
  acción del vendedor: −10>−50 y 50>10). Idem para el vendedor por simetría.
- **Único EN = (Falso, Falso) = (−10, −10).**
- `(Real, Real) = (10, 10)` es **Pareto estrictamente superior** al EN, **pero no es EN**.
- **Respuesta:** por racionalidad individual ambos eligen Falso (hacen trampa) y caen en (−10,−10);
  por racionalidad colectiva ambos estarían mejor en (10,10), pero no es estable.

---

## <a name="eval"></a>📐 Función de evaluación (plantilla aplicada a un juego nuevo)

Te dan un juego cualquiera (Pente, Notakto, Dots & Boxes…). Respuesta tipo:

1. **Objetivo del juego** → ¿por puntos? ¿por capturas? ¿de miseria?
2. **Features independientes** (≥2): elegir 2 medidas que aproximen "estar cerca de ganar".
3. **Definir** `Eval(s) = c₁(E₁(ag,s) − E₁(op,s)) + c₂(E₂(ag,s) − E₂(op,s))`.
4. **Probar propiedad 1:** en finales `Eval(win) ≥ Eval(draw) ≥ Eval(loss)`; discutir **normalización**
   para comparar con utilidades de finales (acotar a `(−1,1)` o usar `if final: return Utilidad`).
5. **Propiedades 2 y 3:** barata (computable incremental) y correlacionada con ganar (validable por
   simulación).

**Ejemplo Pente:** `Eval = c₁·(capturas_ag − capturas_op) + c₂·(pares_propios_en_peligro_op −
pares_propios_en_peligro_ag)`. Para "evaluar la jugada (fila 2, col 5)": calcular `Eval` antes y
después de la jugada; si sube, es buena; si no, indicar la jugada que más sube `Eval` (la que captura o
amenaza capturar, o defiende un par propio).

---

## <a name="entrada-al-mercado"></a>🏭 Entrada al mercado (árbol con nodo de azar) — *Parcial 2023*

**Enunciado resumido:** E decide entrar (`e`) o no (`n`). Si entra, M elige guerra (`g`) o compartir
(`c`). Una moneda `(h,t)` con prob. `(p, 1−p)` se tira **antes** y fija las utilidades de M.
- `n` → `(0, 2)` siempre.
- `e`: utilidad de **E** = −1 si `g`, +1 si `c` (siempre).
- Utilidad de **M**: si `h` → −1 (`g`), +1 (`c`); si `t` → **2** (`g`), +1 (`c`).
- E juega primero. `p = 0.5`, info completa.

### Árbol (chance en la raíz → E → M)
```
            chance (moneda)
           /  h:0.5      \ t:0.5
          E                E
        /   \            /   \
      n      e         n      e
   (0,2)     M       (0,2)    M
           /   \            /   \
         g(-1,-1) c(1,1)  g(-1,2) c(1,1)
```

### Resolución por inducción hacia atrás (p = 0.5)
- **Rama h:** si E juega `e`, M elige max(M): `g`→−1 vs `c`→+1 ⇒ M juega **c**, hoja `(1,1)`.
  E compara `e`→1 vs `n`→0 ⇒ E juega **e**. Valor rama h = **(1, 1)**.
- **Rama t:** si E juega `e`, M elige: `g`→2 vs `c`→1 ⇒ M juega **g**, hoja `(−1,2)`.
  E compara `e`→−1 vs `n`→0 ⇒ E juega **n**. Valor rama t = **(0, 2)**.
- **Nodo chance (raíz):** promediar:
  - E: `0.5·1 + 0.5·0 = 0.5`
  - M: `0.5·1 + 0.5·2 = 1.5`
- **Valor del juego = (0.5, 1.5).**

### Parte 2 — si NO conocen las utilidades del otro
- Pasa a ser un juego de **información incompleta / Bayesiano**: cada empresa tiene **"tipos"** (la
  moneda determina el tipo de M) y mantiene **creencias** (probabilidades) sobre el tipo del otro.
- En el árbol aparecen **conjuntos de información** (nodos que el jugador no puede distinguir).
- **Algoritmo:** se resuelve con **equilibrio Bayesiano de Nash** (Harsanyi), o —en el enfoque del
  curso— **aprendiendo al oponente** con un algoritmo de aprendizaje multiagente (p.ej. **Fictitious
  Play**, que estima la estrategia del rival por su frecuencia histórica).

---

# Parte 2 — Simulacro de parcial (armado nuevo, mismo estilo)

> Hacelo cronometrado (~2 h). Soluciones guía al final.

### Ejercicio 1 — Gomoku reducido (función de evaluación) [12 pts]
"Cinco en línea" en tablero 8×8: gana quien primero alinea 4 fichas propias en fila, columna o
diagonal.
1. Definí una función de evaluación paramétrica con **al menos dos funciones básicas independientes**.
2. Demostrá que **ordena correctamente los estados finales**.
3. Mostrá cómo evaluarías una jugada concreta y discutí el efecto de la **normalización**.

### Ejercicio 2 — Dado y cajas (árbol con azar) [12 pts]
Un jugador A elige entre dos sobres. Sobre 1: recibe el resultado de tirar un dado justo (1–6). Sobre 2:
juega un juego de suma cero 2×2 contra un oponente adversario B con matriz (A filas):
`[[4, 0], [1, 3]]`.
1. ¿Qué tipo de nodos tiene el árbol? Dibujalo.
2. Calculá el valor por **Expectimax** (sobre 1 = azar; sobre 2 = oponente racional → punto de silla).
3. ¿Qué sobre elige A?

### Ejercicio 3 — Negociación (forma normal) [8 pts]
Dos socios reparten 100. Matriz dada (inventá una tipo Litigio). Hallá los EN, las estrategias
dominantes y discutí racionalidad individual vs. colectiva (Pareto).

### Ejercicio 4 — Defensa del obligatorio [8 pts]
Describí FP, RM, IQL y JAL-AM: qué observa cada uno, a qué converge y qué viste en MP y RPS. Analizá un
enfrentamiento cruzado (p.ej. FP vs RM) con tus resultados.

---

### ✅ Soluciones guía del simulacro

**Ej1:** `Eval = c₁·(líneas abiertas de 3 propias − del rival) + c₂·(líneas abiertas de 2 propias − del
rival)`. Una "línea abierta de k" = segmento de 4 sin fichas rivales con k propias. Finales: 4 en línea
propia ⇒ término dominante `+∞`; del rival ⇒ `−∞`. Normalizar a `(−1,1)` o usar `if final`.

**Ej2:**
- Sobre 1 (chance): `(1+2+3+4+5+6)/6 = 3.5`.
- Sobre 2 (silla): matriz `[[4,0],[1,3]]`. ¿Hay silla pura? max-min filas: fila1 min=0, fila2 min=1 →
  maximin=1. min-max columnas: col1 max=4, col2 max=3 → minimax=3. `1 ≠ 3` ⇒ **mixto**. Para A, prob
  `q` de fila1: iguala pagos del rival: col1 `4q+1(1−q)` = col2 `0q+3(1−q)` ⇒ `3q+1 = 3−3q` ⇒ `q=1/3`.
  Valor = `4(1/3)+1(2/3) = 6/3 = 2`.
- A compara `3.5` (sobre 1) vs `2` (sobre 2) ⇒ **elige Sobre 1**, valor del juego **3.5**.

**Ej3 / Ej4:** ver plantillas en [02_temas_infaltables.md](02_temas_infaltables.md) (secciones D y E).

---

# Parte 3 — Ejercicio extra: "El Fugitivo" (12 pts, estilo 2026)

Un Fugitivo se mueve por un grafo conexo de N nodos; **K detectives cooperan** para atraparlo.
Por rondas: mueve el Fugitivo (a un nodo adyacente), luego los K detectives (cada uno a un nodo
adyacente; pueden compartir nodo). Captura = al fin de una ronda un detective ocupa el nodo del
Fugitivo. Si el Fugitivo **sobrevive T rondas, gana él**. Info perfecta salvo en la parte 3.

1. **(4 pts)** Modelar como juego alternado de **2 jugadores de suma cero**: jugadores, estados (qué
   variables y por qué), estado inicial, acciones, `Player(s)`, regla de fin, Utilidad.
2. **(5 pts)** Función de evaluación paramétrica (≥2 sumandos) para **Detectives** + probar que es
   buena. Ojo: hay **dos tipos de final** (captura / timeout a las T rondas) y debe ordenar ambos.
   Discutir normalización.
3. **(3 pts)** El Fugitivo ahora se mueve **oculto** (revela posición cada 3 rondas; entre medio solo
   se observa el tipo de transporte usado). ¿Qué cambia en el modelo? ¿Por qué Minimax/MCTS puro ya
   no aplican? ¿Qué algoritmo(s) del curso usaría? Justificar.

### Guía de solución (mirar recién después de intentarlo)

**1.** Jugador `D` = composición de los K detectives (acción = **vector** de K movimientos, como el
jugador G de Pacman 2020); Fugitivo `F` = MAX o MIN según para quién se evalúe. Estado =
(posición de F, posiciones de los K detectives, **contador de ronda t**, fase de la ronda). Sin `t` en
el estado, la regla de fin "sobrevive T rondas" no es expresable — mismo rol que `sense` en Uno.
`Player`: alterna F → D dentro de cada ronda. Fin: captura (gana D) o `t = T` (gana F). Utilidad suma
cero: +1 D si captura, −1 D si timeout.

**2.** Para Detectives (agente = D): p.ej.
`Eval(s) = −c₁·dist_min(s) + c₂·cerco(s) − c₃·(T − t)` con `c₁,c₂,c₃ > 0`, donde `dist_min` =
distancia en el grafo del detective más cercano al Fugitivo, `cerco` = cantidad de nodos adyacentes
al Fugitivo cubiertos por detectives (a distancia ≤ 1), y `T − t` = tiempo restante. Puntos clave:
- El tiempo restante entra con **coeficiente negativo** para D: cuanto más tiempo le queda al
  Fugitivo, peor para los detectives a igual distancia (el profe remarcó que los cᵢ pueden ser
  negativos — acá se usa).
- **Orden de finales:** en captura, `dist_min = 0` y `cerco` máximo ⟹ Eval máxima; en timeout,
  `T − t = 0` pero `dist_min > 0` ⟹ Eval < que en captura. Para garantizar `Eval(captura) ≥
  Eval(intermedio) ≥ Eval(timeout)` **normalizar** a (−1, 1) o usar `if final: return Utilidad`.
- Barata: distancias por BFS precomputable/incremental; correlacionada con ganar: validable simulando
  (si `dist_min` decrece monótonamente, la captura llega antes de T).

**3.** Aparecen **conjuntos de información**: los detectives no distinguen los nodos posibles del
Fugitivo entre revelaciones (el tipo de transporte restringe el soporte — como el "belief" sobre
tipos). Minimax/MCTS puro asumen estado observable ⟹ no aplican directamente sobre el árbol de
info imperfecta. Opciones del curso: **ISMCTS** (determinizar: muestrear una posición consistente
del Fugitivo antes de cada simulación y armar el árbol sobre info sets — sin entrenamiento previo,
como en el Obligatorio 2) o **CFR** (regret contrafactual por info set; garantía de Nash en suma
cero 2p, pero requiere entrenamiento offline y el juego acá puede ser grande). Respuesta redonda:
ISMCTS para jugar ya sin entrenar; CFR si hay presupuesto offline y el tamaño lo permite —
exactamente el trade-off medido en Leduc (Ob2).

---

# Parte 4 — Ejercicio extra: "Reversi" (12 pts, estilo Yovine puro)

Reversi 8×8: colocar ficha que **flanquee** fichas contrarias en línea (horizontal/vertical/diagonal);
las flanqueadas **se dan vuelta**. Solo son legales jugadas que voltean ≥1 ficha; sin jugada legal se
pasa; termina cuando ninguno puede jugar. **Gana quien tiene más fichas**; a igual cantidad, empate.

1. **(3 pts)** Con `F_p(s)` = cantidad de fichas de `p`, probar que `Eval_F(s) = F_a(s) − F_o(s)`
   ordena correctamente los estados finales.
2. **(6 pts)** `Eval_F` es mala a profundidad baja (quien domina en fichas en el medio juego suele
   perder). (a) ¿Qué propiedad falla y por qué no contradice 1? (b) Proponer eval paramétrica ≥2
   sumandos que lo corrija. *Ayuda: hay casillas que no pueden ser volteadas nunca más.*
3. **(3 pts)** Jugada en la diagonal adyacente a una esquina vacía que voltea 3 fichas y habilita al
   oponente a tomar la esquina: analizarla a profundidad 1 y 2. ¿Qué agrega la profundidad 2?

### Pauta de solución (voz del prototipo oficial — mirar después de intentarlo)

**1.** Gana quien tiene más fichas ⟹ en un final `s`: si es *win* para el agente, `F_a(s) > F_o(s)`
⟹ `Eval_F(s) > 0`; si *draw*, `F_a = F_o` ⟹ `Eval_F = 0`; si *loss*, `Eval_F < 0`. Por lo tanto
`Eval_F(win) > Eval_F(draw) > Eval_F(loss)` — ordena igual que la Utilidad (acá con orden estricto,
mejor aún que en Blokus, donde el bono podía empatar el 0). Además es computable incrementalmente:
al jugar una ficha que voltea `k`, la diferencia cambia en `±(2k+1)`. ∎

**2a.** Falla la **propiedad 3**: la correlación fuerte con la probabilidad real de ganar en estados
**no finales**. No contradice 1 porque la propiedad 1 habla *solo de estados finales*: ordenar bien
los finales es necesario pero no suficiente. En Reversi las fichas son volátiles (una jugada puede
voltear muchas), así que `F_a − F_o` a mitad de partida es mala predictora del resultado — maximizar
fichas temprano reduce jugadas legales propias y regala volteos masivos al final. (Distinguir
propiedades 1 vs 3 es exactamente lo que pide la pregunta.)

**2b.** `Eval(s) = c₁·(M_a(s) − M_o(s)) + c₂·(E_a(s) − E_o(s)) + c₃·(F_a(s) − F_o(s))`, con:
- `M_p` = **movilidad** (cantidad de jugadas legales de `p`) — más opciones = más control (misma
  feature que en Nocca-Nocca, Ob2, donde la movilidad complementa);
- `E_p` = **fichas estables** de `p` (las que ya no pueden ser volteadas: esquinas y bordes
  consolidados) — es la ayuda del enunciado; son "puntos ya cobrados";
- `F_p` = fichas totales, con `c₃` chico (o incluso **negativo** en el medio juego — el profe
  remarcó en clase que los coeficientes pueden ser negativos; acá es real: tener menos fichas
  volátiles temprano correlaciona con ganar).
Ordena finales: en un final no hay jugadas legales (`M = 0`) y toda ficha es estable (`E_p = F_p`),
así que `Eval(final) = (c₂+c₃)(F_a − F_o)` — mismo signo que `Eval_F` ⟹ hereda la propiedad 1 si
`c₂+c₃ > 0`. Normalización a `(−1,1)` (o `if final: return Utilidad`) para comparar con finales.

**3.** A **profundidad 1** solo se evalúa el estado tras la jugada del agente: `F_a − F_o` sube
(+3 volteadas, +1 colocada) y la esquina sigue vacía ⟹ `E` no cambia y la jugada **parece buena**
(salvo que la eval penalice explícitamente ocupar casillas X con esquina vacía — feature válida
pero hay que haberla puesto). A **profundidad 2** el nivel MIN incluye la respuesta del oponente:
toma la esquina ⟹ `E_o` salta (esquina + fichas que consolida) y suele recuperar fichas ⟹ la eval
del nieto cae y la jugada se revela mala. **Qué agrega la profundidad 2:** la búsqueda descubre el
costo diferido que las features estáticas de profundidad 1 no codifican — mismo fenómeno que
dama/torre (Clase 9) y que la profundidad 1 vs 2 de Puntos y Cuadrados (2022).
