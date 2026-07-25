# **Actividad Práctica 01**

### **Parte A: Caso de Estudio "Lógica de Arranque"**

**Contexto:** Usted diseña la seguridad de un motor. **Variables:**

- A: Voltaje Correcto.

- B: Temperatura Segura.

- C: Botón de Parada de Emergencia Activado.

**Regla:** "Arranca SI hay voltaje Y temperatura segura, PERO SOLAMENTE SI la parada de emergencia NO está activada."

**Ejercicio:**

1. Expresión: `(A AND B) AND (NOT C)`

2. Construya la Tabla de Verdad (8 combinaciones) y encuentre la única fila donde el resultado final es `True`.


### **Parte B: Ejercicios de Lógica Mental**

Evalúe las siguientes expresiones y determine si el resultado final es **Verdadero** o **Falso**:

1. `(10 > 5) AND (3 == 3)`

2. `(50 < 10) OR (100 == 100)`

3. `NOT (20 > 5)`

4. `(10 + 5 == 15) AND (NOT (1 > 0))`

5. _Contexto:_ `Nivel_Tanque = 90`, `Valvula_Abierta = True`.

   - Expresión: `(Nivel_Tanque > 80) AND (Valvula_Abierta == True)`


