# 📋 Resumen y Plan de Acción: Obligatorio 1 - Sistemas Multiagente (2026)

Este documento resume de forma estructurada los requisitos y condiciones del **Obligatorio 1** de la materia **Sistemas Multiagente (ORT)**, cruzándolos con la estructura de archivos detectada en tu espacio de trabajo para brindarte una hoja de ruta clara de lo que ya está y lo que falta implementar.

---

## ⏱️ Fechas Clave e Información General

*   **Fecha de Entrega:** **28 de mayo de 2026 hasta las 21:00 horas**.
    *   *Lugar:* Subir a [gestion.ort.edu.uy](https://gestion.ort.edu.uy).
    *   *Formato:* Archivo `.zip` o `.rar` de máximo **40 MB**. Los documentos de texto (el informe) deben estar en formato **PDF** dentro del comprimido.
*   **Fecha de Defensa:** **8 de julio de 2026** (Nota: La letra oficial indica 2025 en la sección de Defensa, pero al ser el obligatorio de 2026, se asume que es un error de tipeo por 2026).
    *   La defensa es **obligatoria y eliminatoria**. La no presentación implica la pérdida total del puntaje. Generalmente presencial, salvo excepciones de defensa remota sincrónica.
*   **Puntaje:** Máximo **30 puntos**, mínimo **1 punto**.
*   **Grupos:** De hasta **3 integrantes** del mismo dictado (Nota: La sección de recordatorios al final menciona "hasta 2 estudiantes", pero el cuerpo de la letra en la pág. 1 aclara formalmente "hasta 3 personas").

---

## 🤖 Uso de Inteligencia Artificial Generativa (IAG)

El uso de IAG está permitido como **apoyo** del proceso de aprendizaje, pero **no sustituye el razonamiento crítico**.
⚠️ **Requisito Obligatorio:** En caso de utilizar herramientas de IAG, se debe **citar adecuadamente la fuente y la forma en que se utilizó** en el informe, detallando:
1.  **Herramientas utilizadas** (ej. Gemini, ChatGPT, etc.).
2.  **Contexto de uso** (ej. generación de ideas, redacción inicial, análisis de datos, corrección de estilo, etc.).
*Cualquier error o alucinación producida por la IA es responsabilidad exclusiva de los estudiantes.*

---

## 🛠️ Requisitos de Desarrollo vs. Estado Actual

El trabajo se divide en dos fases: **Implementación** (sobre la plantilla provista para $N$ agentes) y **Validación** (experimentación comparativa).

### 1. Algoritmos a Implementar

| Algoritmo | Descripción en Letra | Estado en tu Proyecto | Archivo de Referencia |
| :--- | :--- | :--- | :--- |
| **Fictitious Play (FP)** | Aprendizaje basado en creencias históricas de los rivales. | 🟨 Plantilla base creada | [fictitiousplay.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/agents/fictitiousplay.py) |
| **Regret Matching (RM)** | Minimización de arrepentimiento acumulado. | 🟨 Plantilla base creada | [regretmatching.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/agents/regretmatching.py) |
| **Independent Q-Learning (IQL)** | Q-Learning individual tratando a los rivales como parte del entorno. | 🟥 Pendiente | *Crear en `agents/iql.py`* |
| **Joint-Action Learning (JAL-AM)** | Modelado explícito de los oponentes para coordinar acciones conjuntas. | 🟥 Pendiente | *Crear en `agents/jal.py`* |

> ℹ️ **Nota de la Letra:** Toda implementación debe estar pensada para **N agentes** y basarse en la estructura de clases del proyecto.

---

### 2. Ambientes de Validación (Juegos)

Debes validar los algoritmos en (como mínimo) los siguientes ambientes:

| Ambiente / Juego | Tipo / Descripción | Estado en el Workspace | Archivo de Referencia |
| :--- | :--- | :--- | :--- |
| **Matching Pennies (MP)** | Juego de suma cero de 2 jugadores. | 🟩 Implementado | [mp.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games/mp.py) |
| **Rock-Paper-Scissor (RPS)** | Piedra, Papel o Tijera. Suma cero. | 🟩 Implementado | [rps.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games/rps.py) |
| **Blotto** | Juego de asignación de recursos estratégico. | 🟩 Implementado | [blotto.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games/blotto.py) |
| **Foraging** | Ambiente de recolección de comida cooperativo o competitivo. | 🟩 Provisto fuera del módulo | [foraging.py](file:///home/rami/Documents/ORT/sistemas_multiagente/Foraging/games/foraging.py) |

> 💡 **Ambientes Extras Disponibles en el Template:**
> Puedes enriquecer sustancialmente tu informe (lo cual se valorará muy positivamente en la nota) utilizando otros ambientes provistos en tu carpeta `games`:
> *   **Battle of the Sexes (BoS):** [bos.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games/bos.py) - Coordinación clásica.
> *   **Chicken Game:** [chicken.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games/chicken.py) - Halcón-Paloma.
> *   **Cournot Duopoly:** [cournot.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games/cournot.py) - Competencia por cantidades.
> *   **Three Players Game:** [threeplayers.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games/threeplayers.py) - Juego simétrico para 3 jugadores.

---

## 📈 Entregables y Criterios de Evaluación

1.  **Informe de Experimentación (PDF):**
    *   Debe ser detallado y estructurado.
    *   Debe mostrar la experimentación cruzada de todos los algoritmos viables contra sí mismos y contra otros (ej. *FP vs FP*, *FP vs RM*, *FP vs RandomAgent*, *IQL vs IQL*, etc.).
    *   **Altamente Recomendado:** Utilizar gráficas que muestren la evolución de las estrategias y la convergencia a equilibrios.
2.  **Código Fuente:**
    *   Debe subirse a un **repositorio de GitHub público**.
    *   El enlace al repositorio debe incluirse en el informe.

---

## 🚀 Plan de Trabajo Sugerido (Paso a Paso)

### Paso 1: Completar Fictitious Play y Regret Matching
*   Abrir y analizar las plantillas:
    *   [fictitiousplay.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/agents/fictitiousplay.py)
    *   [regretmatching.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/agents/regretmatching.py)
*   Terminar de implementar las mecánicas de actualización de creencias e historial en FP.
*   Implementar el cálculo de arrepentimientos y actualización de probabilidades en RM.

### Paso 2: Implementar IQL y JAL-AM
*   Crear los nuevos archivos en `agents/`:
    *   `iql.py`: Implementar Independent Q-Learning. Cada agente mantiene una tabla Q propia y actualiza sus valores basándose únicamente en sus acciones y recompensas locales.
    *   `jal.py`: Implementar Joint-Action Learning con Agent Modeling. El agente calcula la probabilidad de acción de sus rivales basándose en el conteo de la historia empírica y actualiza la tabla Q sobre el vector de acciones conjunta.
*   Puedes usar de inspiración el cuaderno [IQL.ipynb](file:///home/rami/Documents/ORT/sistemas_multiagente/Foraging/IQL.ipynb) provisto en la carpeta externa.

### Paso 3: Integrar el Ambiente Foraging
*   Actualmente Foraging está fuera de la estructura principal. Mueve o enlaza [foraging.py](file:///home/rami/Documents/ORT/sistemas_multiagente/Foraging/games/foraging.py) al directorio de juegos oficial [games/](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/games) si deseas unificar el proyecto.
*   Analiza [Foraging.ipynb](file:///home/rami/Documents/ORT/sistemas_multiagente/Foraging/Foraging.ipynb) para entender la dinámica de este juego y cómo inicializarlo.

### Paso 4: Ejecución de Experimentos
*   Utiliza el cuaderno [run.ipynb](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/run.ipynb) para diseñar los loops de entrenamiento de enfrentamiento cruzado.
*   Guarda los logs de convergencia y genera los gráficos correspondientes (ej. evolución de las probabilidades de acción en RPS, convergencia al equilibrio de Nash en Matching Pennies).

---

### 📂 Enlaces a Archivos de Configuración del Entorno
*   Gestor de dependencias: [pyproject.toml](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/pyproject.toml)
*   Base del Agente: [agent.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/base/agent.py)
*   Base de los Juegos: [game.py](file:///home/rami/Documents/ORT/sistemas_multiagente/obligatorio_sanes_guerra/base/game.py)
