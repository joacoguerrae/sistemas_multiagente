# 🎯 Resumen de MIS obligatorios — para la defensa del parcial

Basado en el informe entregado de Ob2 (`obligatorio2-sma-guerra-sanes/Informe...pdf`) y el notebook
final de Ob1 (`obligatorio_1/.../run_joaco.ipynb`). La pregunta de defensa histórica pide exactamente
esto: **qué implementaste, qué funciones de evaluación/algoritmos usaste, qué resultados obtuviste y
cómo los explicás** (2022: "describa las funciones de evaluación, objetivos y resultados"; 2023:
"analice los resultados en Kuhn2, Kuhn3 y Leduc con los diferentes algoritmos").

---

## OBLIGATORIO 1 — Aprendizaje en juegos repetidos (FP, RM, IQL, JAL-AM)

**Qué:** 4 algoritmos para N agentes + Random como baseline, validados en MP, RPS, Blotto, BoS,
Chicken y Foraging. Torneos round-robin + gráficas de convergencia de políticas.

### Resultados por juego (números tuyos, memorizables)

| Juego | Resultado clave | El "por qué" (esto es lo que puntúa) |
|---|---|---|
| **RPS** | FP y RM convergen al Nash `(⅓,⅓,⅓)` (obtuvimos `[0.33,0.34,0.33]`). **IQL y JAL colapsan a Rock con 99%** | Q-learning asume entorno **estacionario**; con dos aprendiendo a la vez esa hipótesis se rompe → colapso casi determinista lejos del equilibrio |
| **MP** | FP y RM → `(½,½)`. En el torneo **IQL/JAL le ganan a FP (+0.33)** y FP pierde (−0.33); RM queda ≈0 contra ellos | FP **modela al rival**: contra un rival casi determinista intenta explotarlo, se vuelve predecible y termina explotado. RM no modela → mantiene su mixta estable y no es explotable |
| **Blotto** | 21 acciones. FP y RM dominan el torneo (+0.090/+0.075); IQL/JAL intermedios; Random pierde (−0.30) | FP/RM no convergen a una táctica única sino a una **distribución sobre un subconjunto de tácticas efectivas** — no hay estrategia dominante pura en Blotto |
| **BoS** (coordinación) | FP y RM coordinan **casi instantáneo** en un equilibrio puro (Opera). El "2 vs 1" del heatmap FP-RM refleja la **asimetría del equilibrio**, no que un algoritmo sea mejor | A cuál de los 2 EN puros se llega depende de la **inicialización**, no del algoritmo. IQL/JAL también coordinan pero rinden ~0.98 (menos del máximo) por la **exploración residual del ε-greedy** |
| **Chicken** (anti-coord.) | **IQL/JAL dominan** (5.83/5.75) y FP/RM quedan últimos (2.84/3.45) | El colapso determinista de IQL/JAL acá **juega a favor**: convergen a una acción fija, FP responde con la mejor respuesta que le deja el pago chico (2) y ellos se llevan 7. IQL vs JAL caen en (L,L)=6,6. Moraleja: **ser predecible se paga distinto según el juego** |
| **Foraging** (único con estados) | Con 2000 episodios **IQL y JAL alcanzan reward 1.0** (Random 0.72); curvas casi idénticas, estables tras ~1000 episodios | Es el único ambiente donde Q-learning tiene sentido: hay **estados y horizonte** — y solo IQL/JAL-AM aplican (tablas Q indexadas por estado). Acá se invierte el veredicto de los matriciales |

### Conclusión global Ob1 (contala así)
> "FP y RM son los más sólidos en juegos matriciales: convergen al Nash en suma cero y coordinan en
> BoS; su debilidad es Chicken, donde ser predecible los vuelve explotables. IQL y JAL no sirven para
> matriciales de un estado (la no-estacionariedad rompe Q-learning y colapsan a políticas
> deterministas), pero son los únicos que funcionan cuando hay estados: en Foraging llegan al óptimo."

---

## OBLIGATORIO 2 — Búsqueda y aprendizaje en juegos alternados (MCTS, CFR, ISMCTS)

**Qué:** 3 algoritmos + MiniMax/Random provistos como referencia. Dos familias: **info perfecta**
(MiniMax/MCTS en Tic-Tac-Toe y Nocca-Nocca) e **info imperfecta** (CFR/ISMCTS en Kuhn 2P, Kuhn 3P,
Leduc). Siempre se jugó **en ambas posiciones** y se promedió; se midió **tiempo por partida**.

### Tic-Tac-Toe (control, resoluble)
- MiniMax d1→d3: derrota 0.15→**0.00**, pero tiempo 4ms→170ms (**sin poda α-β y clonando el entorno
  por nodo, el costo explota**).
- MCTS: con 50 sims ya 0.975 de victoria; **los rollouts extra tienen rendimiento decreciente** —
  conviene gastar presupuesto en simulaciones, no en rollouts.
- Torneo: ambos aplastan a Random y entre sí **empatan** (juego resuelto). **Abrir da ventaja medible**.

### Nocca-Nocca (grande: 320 acciones → la eval es central)  ⭐ pregunta tipo 2022
- MiniMax(d1) +0.85 en ~1s/partida; MiniMax(d2) +1.00 pero **21.8s (~22×)** → profundidades mayores
  impracticables sin poda. MCTS +0.50 con mitad de empates por truncamiento (`max_steps=40`).
- **Función de evaluación agregada** (¡saber los 3 sumandos!):
  1. **Progreso** de las piezas hacia la fila objetivo (peso mayor, 0.5),
  2. **Control de la pila** (solo las piezas arriba pueden moverse),
  3. **Movilidad** (cantidad de movimientos legales).
- **Experimento de ablación** (comparamos heurísticas inyectadas en el agente): vs Random → progreso
  1.00, completa 0.83, **movilidad sola 0.00**; duelos directos → completa > progreso > movilidad.
  **Ranking: movilidad < progreso ≤ completa.**
- Conclusión de diseño: **lo que guía a MiniMax es el progreso**; la movilidad solo aporta como
  complemento dentro de la eval combinada, no como criterio único.

### Kuhn Poker 2P (Nash conocido: V* = −1/18 ≈ −0.0556 para el que abre)  ⭐ pregunta tipo 2023
- **CFR converge al Nash**: recompensa final de P0 = **−0.035 ≈ −1/18**, con **12 info sets**.
- La estrategia aprendida **reproduce la teoría**: **farol con J ≈ 1/3** (0.315 tras pass), **value bet
  con K** (0.998 tras pass), Q pasiva/iguala. → "no solo el valor numérico: el equilibrio cualitativo".
- ISMCTS(400) rinde más vs Random (+0.33 vs +0.13 de CFR) pero es **órdenes de magnitud más caro**
  (57s vs 0.12s el matchup) y sin garantía de Nash.
- **Posición**: P0 (abre) −0.111, P1 +0.0125 → **abrir es desventajoso en Kuhn**, signo consistente con
  el −1/18 teórico.

### Kuhn Poker 3P
- **No existe un Nash único.** CFR N-agente entrena estable: 48 info sets por agente, reparto en
  self-play que **suma ≈ 0**.
- **Efecto de posición/orden claro**: ningún asiento es uniformemente mejor, pero **el último en hablar
  tiende a beneficiarse**.
- CFR **explota** a 2 Random (+0.372); contra 2 ISMCTS queda parejo (−0.09) — en 3 jugadores el
  desenlace depende de las estrategias concretas de los rivales.

### Leduc (6 cartas, 2 rondas, carta comunitaria — un orden de magnitud más grande)
- CFR: ~72 info sets, entrenamiento 17→75s (50→200 iter). Vence a Random ya con pocas iteraciones.
- **ISMCTS(100) le gana al CFR entrenado (−0.73)** — ¡saber explicarlo!: **no contradice la teoría**;
  el CFR está **subentrenado** (200 iteraciones para un juego mucho mayor; la garantía de Nash es
  asintótica), mientras ISMCTS hace **búsqueda completa en cada decisión** sin entrenamiento previo.
- **No-monotonicidad** (100 iter → 0.317 pero 200 iter → 0.185 vs Random): es **varianza de
  evaluación** (pocas partidas, recompensas en fichas de rango amplio), no degradación del algoritmo —
  la *explotabilidad* de CFR sí baja monótonamente.

### Conclusiones globales Ob2 (las 5 del informe, contalas así)
1. **El eje es el trade-off cómputo↔calidad**, y cada algoritmo lo paga distinto: MiniMax en
   **profundidad**, MCTS/ISMCTS en **simulaciones por jugada**, CFR en **entrenamiento offline** (una
   vez, luego juega instantáneo).
2. **Las funciones de evaluación son críticas en juegos grandes** (Nocca-Nocca): progreso domina,
   movilidad sola no alcanza.
3. **CFR es el método de referencia para info imperfecta** con tiempo de entrenamiento (Nash en Kuhn
   2P, estable en 3P); ISMCTS es la alternativa potente sin entrenamiento, más cara por jugada.
4. **La posición influye en todos los juegos**: abrir es ventaja en los de tablero y **desventaja en
   Kuhn**; en 3P el orden reparte ventajas de forma no trivial.
5. **Honestidad sobre la varianza**: varios experimentos usan pocas partidas por costo; se leen
   **tendencias y orden relativo** contrastados con la teoría, no decimales.

---

## ⚡ Preguntas probables y respuesta en 3 líneas

1. **"¿Por qué IQL/JAL no convergen a Nash en RPS/MP pero FP/RM sí?"** — Q-learning asume entorno
   estacionario; con ambos aprendiendo, la política del rival cambia y el supuesto se rompe → colapsan
   a acciones deterministas. FP (modela frecuencias) y RM (regrets) están diseñados para juegos
   repetidos: FP converge a Nash en suma-cero 2p y el promedio de RM al conjunto de equilibrios
   correlacionados (= Nash en suma-cero 2p).
2. **"¿Por qué ISMCTS le ganó a CFR en Leduc si CFR 'converge a Nash'?"** — Garantía asintótica: 200
   iteraciones son pocas para ~72 info sets; ese CFR está lejos de converger. ISMCTS no necesita
   entrenamiento porque busca (determinizando el estado oculto) en cada jugada — paga el costo por
   decisión en vez de offline.
3. **"Describa su función de evaluación y muestre que es buena"** — Nocca-Nocca: agregada = progreso
   (0.5) + control de pila + movilidad; el ranking por ablación (movilidad<progreso≤completa) valida
   los pesos. Ordena finales porque el progreso es máximo exactamente al alcanzar la fila objetivo
   (ganar); barata (se computa del estado); correlacionada con ganar (validado: d1 ya gana 85%).
4. **"¿Qué efecto tuvo la posición?"** — Tablero: abrir da ventaja medible (TTT y Nocca). Kuhn: abrir
   es desventajoso (−1/18; medimos P0 −0.111 / P1 +0.013). Kuhn 3P: sin Nash único, el último en
   hablar tiende a beneficiarse. Por eso todos los matchups se jugaron en ambas posiciones promediando.
5. **"¿FP o RM: cuál es 'mejor'?"** — Convergen a lo mismo en suma-cero, con mecanismos distintos (FP
   modela al rival y necesita ver sus acciones + su matriz; RM solo necesita sus propios regrets). La
   diferencia práctica: FP es explotable cuando modelar al rival lo vuelve predecible (Chicken, MP vs
   IQL); RM se mantiene ≈0 contra esos mismos rivales.
6. **"¿Por qué el reward de IQL/JAL en BoS es ~0.98 y no el máximo?"** — Exploración residual del
   ε-greedy: ε decae pero no llega a 0, así que con cierta probabilidad siguen jugando la acción
   descoordinada.
