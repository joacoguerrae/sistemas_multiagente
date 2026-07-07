# 🗓️ Plan de estudio — modo emergencia (8 días)

⚠️ **Actualizado**: el parcial es el **08/07/2026** (individual, 40 pts) y hoy tenés **8 días**. Este
plan reemplaza la versión anterior de 3 semanas. Es día a día, con lo que **sí o sí** hay que cubrir
marcado, y lo prescindible ya descartado (ver el triage completo en
[06_diapositivas_prioridad.md](06_diapositivas_prioridad.md)). Asumí ~3-4h/día; cada día tiene un
"si te sobra tiempo" al final para no perder el rato si vas más rápido.

Formato de práctica: **solo papel**, nada de correr notebooks — coherente con que el parcial es escrito.

---

### Día 1 — Forma normal (la base)
- [ ] Leer `Sistemas_multiagente_2.pdf` (forma normal, dominancia, IDSDS/IDWDS, Nash) — **no** leas
      también el standalone "Juegos ordinales", es el mismo contenido.
- [ ] Leer `Sistemas_multiagente_4.pdf` (estrategias mixtas, Teorema Minimax + LP) — ídem, saltear
      "Estrategias mixtas o estocásticas.pdf".
- [ ] Estudiar [02_temas_infaltables.md §D](02_temas_infaltables.md#d-juegos-en-forma-normal--nash-dominancia-pareto--media-clave-en-2020).
- [ ] Hacer **Ejercicios 1.pdf** completo (4 problemas — ver detalle en [06](06_diapositivas_prioridad.md)).
- Si sobra tiempo: `Sistemas_multiagente_4_bis.pdf` (Equilibrio Correlacionado).

### Día 2 — Algoritmos de aprendizaje (parte 1) + práctica de árboles
- [ ] Leer `Sistemas_multiagente_5.pdf` (Fictitious Play) y `Sistemas_multiagente_6.pdf` (Regret Matching).
- [ ] Estudiar el formulario correspondiente en [05_formulario.md](05_formulario.md).
- [ ] Hacer **Ejercicios 2.pdf, problemas 1 y 2** (EN mixto vía FP, suma cero vía Minimax).
- [ ] Repasar Ventas Fraudulentas y Litigio (parcial 2020) en [03](03_preguntas_tipo_y_simulacro.md#normal-form).

### Día 3 — Juegos Estocásticos: IQL, JAL-GT, JAL-AM (🔴 crítico para la defensa)
- [ ] Leer `Sistemas_multiagente_7.pdf` completo — es denso pero es la fuente exacta de 2 de los 4
      algoritmos del obligatorio. Prestá atención a la tupla `⟨P,S,A,T,R,γ,μ⟩` y a las 3 variantes
      (IQL / JAL-GT / JAL-AM).
- [ ] Estudiar la sección E ampliada de [02_temas_infaltables.md](02_temas_infaltables.md#e-defensa-del-obligatorio).
- [ ] **Releer tu propio informe del obligatorio** y tus gráficas: preparate para explicar, con tus
      números, la evolución de la recompensa, la distancia a la política de equilibrio conocida, y el
      histograma de acciones jugadas vs. la política promedio (esto último importa: en Regret Matching
      la acción jugada en el instante t NO es la política promedio — no te confundas si te preguntan por qué).
- [ ] Hacer **Ejercicios 2.pdf, problemas 3 y 4** (árboles, MaxN, Expectimax, "MaxNash").

### Día 4 — Minimax / Expectimax / poda alfa-beta (el tema que más cae)
- [ ] Leer `ta-te-ti.pdf` (3 slides, hacelo primero — es el combo función-de-evaluación + minimax + poda
      con números reales).
- [ ] Skim dirigido de `Sistemas_multiagente_8.pdf`: solo las secciones "Propiedades de Minimax" y
      "ExpectiMiniMax".
- [ ] Repasar `Sistemas_multiagente_9.pdf` (poda alfa-beta, función de evaluación, expectimax) — ya
      tenés esto trabajado a fondo, es repaso rápido de la notación.
- [ ] Estudiar a fondo [02 §A](02_temas_infaltables.md#a-función-de-evaluación--cae-siempre) y
      [02 §C](02_temas_infaltables.md#c-minimax-expectimax-y-poda-α-β--cae-casi-siempre).
- [ ] Rehacer a mano, sin mirar solución: **Blokus** y **Notakto** (ver [01](01_analisis_parciales.md)).
- [ ] Rehacer **Cajas** (2020 L1 y L2) completo — subjuego de silla + minimax + expectimax
      ([03](03_preguntas_tipo_y_simulacro.md#cajas)).

### Día 5 — Función de evaluación avanzada + información imperfecta
- [ ] Leer `Sistemas_multiagente_10.pdf` (Monte Carlo Rollout + MCTS/UCT).
- [ ] Leer `Sistemas_multiagente_12.pdf` (CFR: infosets, regret contrafactual, Kuhn Poker).
- [ ] Estudiar las nuevas secciones F y G de [02_temas_infaltables.md](02_temas_infaltables.md).
- [ ] Rehacer **Dots & Boxes** (2022) y **Pente** (2023) a mano — ver [01](01_analisis_parciales.md).
- [ ] Rehacer **Entrada al Mercado** (2023) completo, incluyendo la parte de info incompleta + CFR
      ([03](03_preguntas_tipo_y_simulacro.md#entrada-al-mercado)).
- Si sobra tiempo: `Sistemas_multiagente_9_bis.pdf` (pseudocódigo, 5 min) y `Sistemas_multiagente_11.pdf`
  (Maxn, 10 min — opcional, ya lo tocaste indirectamente en Ejercicios 2 problema 4).

### Día 6 — Simulacro completo
- [ ] Simulacro cronometrado (~2h, sin apuntes): [03 Parte 2](03_preguntas_tipo_y_simulacro.md#parte-2--simulacro-de-parcial-armado-nuevo-mismo-estilo).
- [ ] Corregir con las soluciones guía. Anotar los 2-3 errores más importantes.
- [ ] Repasar específicamente esos puntos débiles detectados (releer la sección correspondiente de
      [02_temas_infaltables.md](02_temas_infaltables.md)).

### Día 7 — Repaso integral + defensa
- [ ] Repasar [05_formulario.md](05_formulario.md) completo — debería estar casi memorizado a esta altura.
- [ ] Segunda pasada por los puntos débiles del simulacro.
- [ ] Ensayar en voz alta la defensa del obligatorio: un párrafo por algoritmo (FP/RM/IQL/JAL-AM/JAL-GT
      si aplica) + un párrafo por ambiente (MP/RPS/Blotto/Foraging) con qué se esperaba y qué obtuviste.
- [ ] Repasar el checklist anti-error de [05](05_formulario.md#checklist-anti-error-tonto).
- [ ] Dormir bien. En serio — a esta altura rinde más descansar que forzar una lectura más.

### Día 8 — Día del parcial
- [ ] Solo repaso liviano a la mañana: formulario + checklist anti-error. **Nada de material nuevo.**
- [ ] Recordatorio final: identificar SIEMPRE primero el tipo de juego (suma cero/general-sum, con/sin
      azar, info perfecta/imperfecta) antes de resolver cualquier ejercicio de árbol.

---

## ⏱️ Si te atrasás (qué cortar primero, en este orden)

1. `Sistemas_multiagente_11.pdf` (Maxn) — ya cubierto indirectamente por Ejercicios 2 problema 4.
2. `Sistemas_multiagente_9_bis.pdf` (pseudocódigo) — no agrega teoría nueva.
3. El skim de `Sistemas_multiagente_8.pdf` — muy solapado con el deck 9 que ya dominás.
4. `Sistemas_multiagente_4_bis.pdf` (Equilibrio Correlacionado) — mencionalo de pasada, no es foco histórico.
5. El día 5 completo si hace falta comprimir — CFR y MCTS suman pero A (eval) + C (minimax) + E (defensa)
   son los que garantizan aprobar.

**Núcleo innegociable si el tiempo se reduce a la mitad:** Día 1 (forma normal) + Día 4 (minimax/eval) +
Día 3 (defensa: deck 7 + tu informe) + Día 6 (simulacro). Eso es lo que garantiza aprobar.
