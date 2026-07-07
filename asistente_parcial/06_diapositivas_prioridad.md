# 🚨 Prioridad de diapositivas — modo emergencia (8 días)

Parcial: **08/07/2026, individual, 40 puntos** (confirmado en `Sistemas_multiagente_0.pdf`; coincide con
la fecha de defensa del obligatorio). Hoy tenés **8 días**. Esto reemplaza el plan de 3 semanas: acá va
el triage real de los **19 archivos** de `diapositivas/`, verificado archivo por archivo (contenido real,
no solo el nombre).

## 🎁 El hallazgo que te ahorra tiempo: hay duplicados exactos

**4 de las 19 diapositivas son copias casi idénticas de otras 4** (mismo contenido, a veces MD5
idéntico, solo cambia la fecha del pie de página). No hace falta leer las dos veces:

| Leé este… | …y salteá este (es el mismo contenido) |
|---|---|
| `Sistemas_multiagente_2.pdf` | ~~"Teoría de juegos - Juegos ordinales de una jugada.pdf"~~ |
| `Sistemas_multiagente_4.pdf` | ~~"Teoria de juegos Estrategias mixtas o estocasticas.pdf"~~ (MD5 idéntico) |
| `Sistemas_multiagente_4_bis.pdf` | ~~"Equilibrios Correlacionados.pdf"~~ (casi idéntico, 1 slide de más en el standalone — opcional) |
| `Sistemas_multiagente_5.pdf` | ~~"Ficticious Play.pdf"~~ (MD5 idéntico) |

Con esto, de 19 archivos **solo necesitás abrir 15**. Los pesados en teoría (`teoria_juegos_conceptos.md`,
`teoria_fictitious_play.md`, `teoria_regret_matching.md`) ya sintetizan justamente estos duplicados, así
que si tenés poco tiempo también podés leer el `.md` en vez del PDF.

---

## 📋 Tabla completa — las 19 diapositivas, veredicto por veredicto

| # | Archivo | Tema real (verificado) | Prioridad | Por qué |
|:-:|---|---|:-:|---|
| 0 | `Sistemas_multiagente_0.pdf` | Logística del curso (evaluación, fechas, bibliografía) | ⚪ Prescindible | Cero contenido de examen. (Ya te saqué el dato útil: parcial 8/7, individual, 40 pts.) |
| 1 | `Sistemas_multiagente_1.pdf` | Introducción: agente-ambiente, qué es un sistema multiagente, preguntas de diseño (¿cuántos agentes? ¿observabilidad? ¿utilidad?) | ⚪ Prescindible | Es motivación/marco, sin fórmulas ni algoritmos evaluables. Skim de 2 min si querés contexto. |
| 2 | `Sistemas_multiagente_2.pdf` | **Forma normal**: (P,A,R), dominancia estricta/débil, IDSDS/IDWDS, Nash puro/mixto, Matching Pennies | 🔴 **Sí o sí** | Base de todo el tipo **D** (Nash/dominancia/Pareto) — 2/5 parciales, y necesaria para entender A y C. |
| 4 | `Sistemas_multiagente_4.pdf` | Estrategias mixtas, mejor respuesta, existencia de Nash, **Teorema Minimax** (von Neumann) + programación lineal | 🔴 **Sí o sí** | El Teorema Minimax es la base teórica de *todos* los ejercicios de "Cajas"/juegos de suma cero. |
| 4_bis | `Sistemas_multiagente_4_bis.pdf` | Equilibrio Correlacionado (Aumann): ejemplo, definición formal, relación con Nash y Pareto | 🟡 Media | No es tema frecuente en parciales por sí solo, pero es la meta a la que converge Regret Matching — mencionalo en la defensa. |
| 5 | `Sistemas_multiagente_5.pdf` | Fictitious Play: conteo de acciones, ejemplo numérico, convergencia | 🔴 **Sí o sí** | Uno de los 4 algoritmos del obligatorio — cae en la defensa (tipo E). |
| 6 | `Sistemas_multiagente_6.pdf` | **Regret Matching**: arrepentimiento instantáneo/acumulado, estrategia proporcional a regrets, FP vs RM vs "agente ingenuo" | 🔴 **Sí o sí** | Ídem — algoritmo del obligatorio + base conceptual de CFR (ver #12). |
| 7 | `Sistemas_multiagente_7.pdf` | **Juegos Estocásticos**: tupla ⟨P,S,A,T,R,γ,μ⟩, historias/episodios, retorno esperado, **IQL** (pseudocódigo completo), **JAL-GT** (resuelve con teoría de juegos, ej. Minimax-Q), **JAL-AM** (modela al rival, fórmula de AV) | 🔴 **SÍ O SÍ — máxima prioridad** | Es la fuente exacta de 2 de los 4 algoritmos del obligatorio (IQL, JAL-AM) + la variante JAL-GT que no tenías documentada. Puntos garantizados en la defensa si lo dominás. |
| 8 | `Sistemas_multiagente_8.pdf` | Minimax/expectimax formal: árbol de juego, recurrencia de valor, propiedades de Minimax (mejor respuesta, cota inferior), ExpectiMiniMax | 🟢 Skim dirigido | Muy solapado con lo que ya cubrimos (transcripción de Clase8/9). Andá directo a "Propiedades de Minimax" y "ExpectiMiniMax" — el resto ya lo sabés. |
| 9 | `Sistemas_multiagente_9.pdf` | Poda alfa-beta, función de evaluación (3 propiedades + normalización), ejemplo Ta-Te-Ti completo, expectimax | 🔴 **Sí o sí** | El tema que **más cae en el parcial**. Ya lo trabajamos a fondo vía transcripción — date una pasada rápida por el PDF para ver la notación limpia. |
| 9_bis | `Sistemas_multiagente_9_bis.pdf` | Pseudocódigo: loop planificar/jugar + función recursiva `minimax(G,d)` | 🟢 Skim (5 min) | Continuación directa de la misma clase que #9. Sin teoría nueva. |
| 10 | `Sistemas_multiagente_10.pdf` | **Monte Carlo Rollout + MCTS** (selección/expansión/simulación/backup, fórmula UCT) | 🔴 **Sí o sí** | Única fuente de MCTS; es "función de evaluación" (tema #1) llevada a otro método — buen material para un ejercicio tipo "otra forma de estimar el valor sin Eval a mano". |
| 11 | `Sistemas_multiagente_11.pdf` | **Maxn**: minimax generalizado a N>2 jugadores, juegos de suma constante, poda superficial | ⚪ Prescindible (si sobra tiempo, 10 min) | Fechado 2025 — posible material reciclado, no confirmado que se dicte este año. No es tema histórico de parcial (el foco siempre fue reducir a 2 jugadores, ver Pacman en `02_temas_infaltables.md`). |
| 12 | `Sistemas_multiagente_12.pdf` | **CFR** (Counterfactual Regret Minimization): infosets, regret por infoset, chance sampling, ejemplo Kuhn Poker | 🔴 **Sí o sí** | Extiende Regret Matching a información imperfecta — exactamente lo que se necesita para "qué pasa si no conocen las utilidades del otro" (ver Entrada al Mercado, parcial 2023). Alto potencial de caer. |
| — | `ta-te-ti.pdf` | Minimax aplicado a Ta-Te-Ti: `Eval(n) = M(n) − O(n)`, árbol de 2 plies con valores, poda alfa-beta marcada | 🔴 **Sí o sí** (son 3 slides) | Combo exacto de los 3 temas que más caen: función de evaluación + minimax + poda, con números reales. Rapidísimo de leer. |

---

## ✍️ Dónde hacer ejercicios (y qué hay en cada uno)

Ya inventarié el contenido real de los dos PDFs de práctica en papel:

**`practicos/ejercicios/Ejercicios 1.pdf`** (forma normal — hacer después de leer decks 2 y 4):
1. Anto y Gonza salen a cenar — armar matriz de utilidad desde preferencias ordinales + IDSDS/IDWDS/Nash.
2. Nash y Pareto — matriz 3×2 dada: IDSDS/IDWDS/Nash + comparación con Pareto.
3. Valor de estrategias mixtas sobre la matriz anterior — verificar si un perfil dado es EN.
4. Nash puros y mixtos en una matriz 2×2 — hallar y verificar.

**`practicos/ejercicios/Ejercicios 2.pdf`** (puente forma normal → árboles — hacer después de decks 5/6/8/9):
1. EN mixto en una matriz 2×2 sin EN puro — hallarlo vía Fictitious Play y verificarlo.
2. Suma cero 2×2 — EN puro (no hay), vía FP, vía Minimax.
3. El mismo juego llevado a **forma alternada** (árboles "A primero"/"B primero"): Expectimax uniforme, MaxN, comparar con Nash, ventaja de jugar segundo.
4. Juego secuencial de 3 jugadores: valor con **MaxN**, **Expectimax**, y **"MaxNash"** (subjuego simultáneo resuelto por Nash). — Esto conecta directo con Maxn (deck 11), así que si hacés este ejercicio ya cubriste lo esencial de Maxn sin necesidad de leerlo.

**Además, practicá en papel:**
- Los ejercicios de función de evaluación de `01_analisis_parciales.md` (Blokus, Notakto, Dots&Boxes, Pente) → después de deck 9 + ta-te-ti.pdf.
- El simulacro completo de `03_preguntas_tipo_y_simulacro.md` → al final, integrando todo.
- Tu propio informe del obligatorio (FP/RM/IQL/JAL-AM) → después de deck 7, para la defensa.

> No hace falta correr `Ejercicios.ipynb` ni `Ejercicios (cont).ipynb` — son las mismas prácticas en
> versión notebook; con los PDF alcanza dado que el parcial es escrito.

---

## 🎯 Temas fundamentales a saber (cruce final, con lo nuevo de deck 7/10/12)

Los 5 pilares de `02_temas_infaltables.md` siguen siendo el corazón (A: función de evaluación, B:
modelado, C: minimax/expectimax, D: forma normal, E: defensa). A eso se agregan, confirmados ahora en
diapositivas reales:

- **Juegos Estocásticos formales** (deck 7): la tupla `⟨P,S,A,T,R,γ,μ⟩`, y sobre todo **3 algoritmos**
  con pseudocódigo exacto: IQL, JAL-GT (resuelve el juego en forma normal de los Q-values, ej. Minimax-Q
  de Littman), JAL-AM (modela al rival, decide por valor promedio `AV`). Ver sección E ampliada.
- **Monte Carlo Tree Search** (deck 10): alternativa a la función de evaluación manual — 4 fases
  (selección/expansión/simulación/backup) + fórmula UCT. Ver nueva sección F.
- **CFR** (deck 12): generaliza Regret Matching a árboles con información imperfecta vía regret
  *contrafactual* por conjunto de información. Ver nueva sección G — y releé la respuesta sobre CFR que
  ya charlamos para el Ejercicio 2 del parcial 2023.

Fueron agregadas como secciones nuevas en [02_temas_infaltables.md](02_temas_infaltables.md).
