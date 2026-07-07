# 🎓 Asistente de Parcial — Sistemas Multiagente (ORT)

Kit de estudio armado a partir del cruce de **todos los parciales (2020–2023) + soluciones** con
las **19 diapositivas del curso** (verificadas una por una), transcripciones de clase, la letra del
obligatorio 2026 y el material complementario del repo.

> ⚠️ **Parcial: 08/07/2026, individual, 40 puntos.** Modo emergencia activo — ver
> [04_plan_de_estudio.md](04_plan_de_estudio.md) para el plan día a día.

---

## 📁 Contenido de esta carpeta

| Archivo | Para qué sirve |
| :--- | :--- |
| [01_analisis_parciales.md](01_analisis_parciales.md) | Desglose ejercicio por ejercicio de los 5 parciales, con el tema y el enfoque de resolución de cada uno. |
| [02_temas_infaltables.md](02_temas_infaltables.md) | Los temas que **siempre caen**, con la teoría mínima y el "cómo se contesta" (incluye Juegos Estocásticos/IQL/JAL, MCTS y CFR). |
| [03_preguntas_tipo_y_simulacro.md](03_preguntas_tipo_y_simulacro.md) | Banco de preguntas tipo + un simulacro de parcial completo con soluciones. |
| [04_plan_de_estudio.md](04_plan_de_estudio.md) | **Plan día a día para 8 días**, priorizado por probabilidad de que caiga. |
| [05_formulario.md](05_formulario.md) | Formulario / chuleta: minimax, expectimax, función de evaluación, Nash, dominancia, Pareto, FP, RM, IQL, JAL. |
| [06_diapositivas_prioridad.md](06_diapositivas_prioridad.md) | Triage verificado de las 19 diapositivas: cuáles leer sí o sí, cuáles son duplicados, cuáles son prescindibles, y dónde hacer ejercicios. |
| [07_resumen_obligatorios.md](07_resumen_obligatorios.md) | **Defensa**: resumen de MIS dos obligatorios (Ob1: FP/RM/IQL/JAL; Ob2: MCTS/CFR/ISMCTS) con los números reales de los informes y respuestas modelo. |

---

## 🧭 Veredicto rápido: ¿qué estudiar sí o sí?

El patrón de los 5 parciales es muy estable. Un parcial tipo tiene **3 a 4 ejercicios** que salen
casi siempre de este menú:

| # | Tipo de ejercicio | Frecuencia | Prioridad |
| :-: | :--- | :--- | :--- |
| **A** | **Función de evaluación** de un juego de tablero + demostrar que es "buena" | **5/5 parciales** (a veces 2 veces) | 🔴 MÁXIMA |
| **B** | **Modelado de un juego secuencial/alternado** (estados, acciones, `Player`, utilidad) | 3/5 | 🔴 ALTA |
| **C** | **Árbol de juego + Minimax / Expectimax** (con nodos de azar / info imperfecta) | 4/5 | 🔴 ALTA |
| **D** | **Juego en forma normal**: Nash + dominancia + Pareto (racionalidad individual vs. colectiva) | 2/5 (2020) | 🟡 MEDIA |
| **E** | **Defensa del obligatorio** (algoritmos y resultados implementados) | 2/5 (2022, 2023) y creciendo | 🔴 ALTA |

**Conclusión:** si dominás (A) función de evaluación, (C) minimax/expectimax sobre árboles y (E) tu
obligatorio (FP/RM/IQL/JAL), tenés cubierto el grueso del parcial. (B) y (D) son la teoría de
soporte que hace falta para resolver (A) y (C) bien.

---

## 📚 Mapa material ↔ tema (verificado archivo por archivo, ver [06](06_diapositivas_prioridad.md))

| Tema | Dónde estudiarlo en el repo |
| :--- | :--- |
| Forma normal, Nash, mixtas, minimax theorem | `Sistemas_multiagente_2.pdf` + `_4.pdf` (= duplicados de las "Teoría de juegos") |
| Minimax, poda α-β, función de evaluación, expectimax | `transcripciones/limpias/Clase8.txt` y `Clase9.txt`, `_8.pdf`, `_9.pdf`, `ta-te-ti.pdf` |
| Fictitious Play | `_5.pdf` (= duplicado de "Ficticious Play.pdf") |
| Regret Matching + Eq. Correlacionado | `_6.pdf`, `_4_bis.pdf` (= duplicado de "Equilibrios Correlacionados.pdf") |
| **Juegos Estocásticos, IQL, JAL-GT, JAL-AM** | `Sistemas_multiagente_7.pdf` ← fuente exacta, con pseudocódigo de los 3 |
| Monte Carlo Rollout / MCTS | `Sistemas_multiagente_10.pdf` |
| **CFR** (Counterfactual Regret Minimization) | `Sistemas_multiagente_12.pdf` — infosets, regret contrafactual, ejemplo Kuhn Poker |
| Maxn (minimax a N jugadores) | `Sistemas_multiagente_11.pdf` (dudoso si se dictó este año — ver 06) |
| Dominancia / Pareto (código) | `practicos/ejercicios/dominance.py`, `pareto.py`, `nasheq.py`, `fictplay.py` |
| Referencia formal | `material_complementario/marl-book.pdf` (Albrecht, Christianos, Schäfer — caps. 1, 3, 4, 5, 6) |

> Nota sobre la **defensa del obligatorio**: los parciales 2022/2023 piden defender *Kuhn/Leduc*
> (esa edición usaba poker + CFR). **Tu obligatorio 2026 es distinto**: FP, RM, IQL y JAL-AM
> validados en MP, RPS, Blotto y Foraging — esa es la base de tu pregunta E. Pero ojo: **CFR sí es
> parte del programa 2026** (deck 12, independiente del obligatorio) y puede aparecer como su propio
> tema en un ejercicio de información imperfecta. Ver [02_temas_infaltables.md](02_temas_infaltables.md#e-defensa-del-obligatorio).
