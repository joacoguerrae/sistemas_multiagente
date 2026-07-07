# 📑 Formulario / chuleta

Todo lo que conviene tener "en la punta de la lengua". Símbolos: `ag` = agente (MAX), `op` = oponente
(MIN), `s` = estado, `a` = acción, `π` = estrategia.

---

## Búsqueda adversarial

**Minimax (suma cero, 2 jug., info perfecta):**
```
V(s) = Utilidad(s)                          si s terminal
     = max_a V(Suc(s,a))                     si Player(s) = MAX
     = min_a V(Suc(s,a))                     si Player(s) = MIN
```
**Con profundidad d limitada:** si `d = 0` y `s` no terminal → `V(s) = Eval(s)`.

**Expectimax / Expectiminimax (con azar):** agregar nodos CHANCE:
```
V(chance) = Σ_r P(r) · V(Suc(s, r))
```
Oponente **aleatorio** ⇒ tratarlo como CHANCE (promedio), **no** como MIN.

**Poda α-β:** `α` = mejor cota inferior de MAX, `β` = mejor cota superior de MIN. **Podar si α ≥ β.**
Es exacta (= minimax). Su eficiencia **depende del orden** de recorrido.

---

## Función de evaluación

**Forma canónica:** `Eval(s) = Σᵢ cᵢ · (Eᵢ(ag, s) − Eᵢ(op, s))`

**Buena función de evaluación (3 propiedades):**
1. **Ordena finales:** `Eval(win) ≥ Eval(draw) ≥ Eval(loss)` (igual que Utilidad).
2. **Barata:** costo ≪ costo de evaluar el subárbol.
3. **Correlacionada** con P(ganar) (se valida simulando).

**Normalización:** acotar `Eval` a `(−1, 1)` o usar `if s final: return Utilidad(s) else: return Eval(s)`
para que ningún estado intermedio supere a un final ganador.

---

## Teoría de juegos (forma normal)

**Juego:** `Γ = ⟨P, A, R⟩`. **Mixta:** `π_p ∈ Δ(A_p)`, `Σ π_p(a)=1`.

**Valor esperado:** `V_p(π) = Σ_{a∈A} π(a) R_p(a)`, con `π(a) = Π_p π_p(a_p)`.

**Mejor respuesta:** `π_p ∈ BR_p(π_{-p})` si maximiza `V_p`. *Siempre existe una BR pura.*

**Equilibrio de Nash:** `π*_p ∈ BR_p(π*_{-p}) ∀p`. *(Nash: todo juego finito tiene ≥1 EN.)*

**Dominancia:** `a` domina estricta a `b` si `R_p(a, ·) > R_p(b, ·)` ∀ acción del rival (débil: ≥ y > en
≥1). Eliminación iterativa: IDSDS (estricta), IDWDS (débil).

**Pareto superior:** nadie peor y alguien mejor. **Óptimo de Pareto:** nada lo domina en Pareto.

**Teorema Minimax (von Neumann, suma cero 2 jug.):**
`max_{π1} min_{π2} V₁ = min_{π2} max_{π1} V₁ = V*`. Todo perfil minimax es EN; todos los EN valen `V*`.

**EN mixto en 2×2 (indiferencia):** elegir la prob. del rival que iguala los pagos esperados de tus
acciones (y viceversa).

**Argumento estándar:** racionalidad **individual** → EN; suele existir un perfil **Pareto superior**
que **no** es EN → racionalidad **colectiva** (dilema del prisionero).

---

## Juegos estocásticos (marco del obligatorio)

`SG = ⟨P, S, A, T, R, γ, μ⟩`. Forma-normal repetida = SG con `|S|=1`; MDP = SG con `|P|=1`.

**Fictitious Play (FP):** estima la mixta del rival por **frecuencia histórica** `π̂_q(a) =
count(a)/Σcount`, juega **mejor respuesta**. Observa: acciones de todos + su matriz. Converge a EN en
suma-cero 2p, potenciales y resolubles por dominancia (puede ciclar, Shapley).

**Regret Matching (RM):** regret instantáneo `g_p(a') = R_p(a', a_{-p}) − R_p(a)`; acumulado `G_p`.
Estrategia `π̂_p(a') = max(G_p(a'),0) / Σ max(G_p,0)` (uniforme si denom ≤ 0). El **promedio** converge
a **Equilibrio Correlacionado** (= EN en suma-cero 2p).

**Equilibrio Correlacionado (Aumann):** `Σ_a π(a) R_p(ξ_p(a_p), a_{-p}) ≤ Σ_a π(a) R_p(a)` ∀p, ∀modificador
`ξ_p`. Conjunto **convexo** que **contiene** a todos los EN.

**IQL:** `Q_i(s,a_i) ← Q_i(s,a_i) + α[r_i + γ max_{a'} Q_i(s',a') − Q_i(s,a_i)]`. Ignora a los demás.
Sin garantías (no estacionario), escala bien.

**JAL-AM:** Q sobre acción conjunta `Q_i(s,(a_i,a_{-i}))`; valor promedio
`AV_i(s,a_i) = Σ_{a_{-i}} Q_i(s,(a_i,a_{-i})) · π_{-i}(a_{-i}|s)`; decide `argmax_{a_i} AV_i`.
Modela al rival; explota exponencialmente con N.

**EN de los ambientes:** MP → `(½,½)`, V=0. RPS → `(⅓,⅓,⅓)`, V=0.

---

## Checklist anti-error tonto

- [ ] ¿El oponente es adversarial (MIN) o aleatorio (CHANCE)? No confundir.
- [ ] ¿Normalicé la `Eval` antes de compararla con utilidades de finales?
- [ ] ¿Justifiqué que la `Eval` ordena `win ≥ draw ≥ loss`?
- [ ] En forma normal: ¿distinguí EN (individual) de Pareto (colectivo)?
- [ ] ¿Identifiqué bien el **tipo de juego** (suma cero / alternado / con azar / info imperfecta)?
- [ ] En la defensa: ¿hablo de **mis** algoritmos y resultados (FP/RM/IQL/JAL), no de Kuhn/Leduc?
