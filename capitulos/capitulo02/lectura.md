# **Datos, Operadores y la Lógica de las Decisiones**

## **Introducción: La Materia Prima del Algoritmo**

En el capítulo anterior definimos que **un proceso industrial transforma _entradas_ en _salidas_**. En el **mundo digital**, **esa materia prima** no es acero o plástico, **son datos**.

Para una persona profesional en Ingeniería Industrial, entender los tipos de datos es tan crítico como entender las propiedades de los materiales.

- Si intentas soldar madera con metal, la estructura falla. De igual forma, si intentas sumar un "Nombre" con un "Precio", el algoritmo colapsa. Porque uno es un texto y el otro un número.

- Es como mezclar fluidos en una tubería. Si mezclas agua y aceite, no obtienes una solución homogénea. Si intentas guardar un texto largo en una variable diseñada para un número pequeño, provocarás un desbordamiento (derrumbe) del sistema. Es como intentar almacenar agua en una bolsa de tela, que no está diseñada para esto. Pero en cambio si uno quiere almacenar un líquido debe contar con un recipiente adecuado para líquidos.

- Es intentar forzar una pieza cuadrada en un orificio redondo. Intentar procesar una fecha (ej. "2024-01-01") como si fuera un número entero para restar, generará un error de cálculo o detendrá el programa.  Aunque esto suene absurdo, en el ejercicio profesional al revisar análisis numéricos, se encuentran errores así, que producen “información errónea” lo que conlleva una mala toma de decisiones. Quizá uno de los principales objetivos de realizar programas o automatizaciones, que nos sirva para la adecuada toma de decisiones.

En esta semana, vamos a introducir la clasificación de estos datos, a manipularlos mediante operadores y, lo más importante, iniciamos el aprendizaje del lenguaje que nos ayudará en la toma de decisiones automáticas: el **Álgebra Booleana**, la base de todos los sistemas de control, como los  PLCs en la industria moderna entre otros elementos propios de la Ingeniería Industrial.


## **Conceptos Clave**

Antes de profundizar, definamos el vocabulario técnico que nos acompañará:

- **Variable:** Contenedor nombrado que almacena un valor [mutable](https://dle.rae.es/mutable) en la memoria.

- **Tipo de Dato:** Clasificación que define qué clase de valor tiene una variable y nos define qué operaciones se pueden realizar con ella (ej. Entero, Texto).

- **Valor:** El dato específico contenido dentro de una variable en un momento dado.

- **Operador:** Símbolo que indica una acción a realizar (sumar, comparar, negar, etc.).

- **Jerarquía de Operadores:** El orden estricto en el que la computadora resuelve las operaciones matemáticas y lógicas.

- **Álgebra Booleana:** Rama matemática que trabaja con variables binarias (Verdadero/Falso).

- **Sistema de Control / PLC:** _Programmable Logic Controller_. Dispositivos industriales que ejecutan acciones físicas basadas en lógica booleana.

- **SQL:** _Structured Query Language_. Lenguaje estándar para bases de datos. (ver [enlace](https://www.soydba.es/la-pronunciacion-de-sql-es-kiu-el-o-sicuel/))

- **UpperCamelCase:** Estilo de escritura donde cada palabra inicia con mayúscula (Ej: `ClienteNuevo`). Usado comúnmente para Clases en la mayor parte de los lenguajes de programación, siempre se debe seguir las reglas de cada lenguaje.

- **lowerCamelCase:** La primera palabra en minúscula y las siguientes en mayúscula (Ej: `calcularImpuesto`). Usado en Java/JavaScript para describir variables o acciones (funciones, métodos o procedimientos).

- **snake\_case:** Palabras separadas por guiones bajos (Ej: `costo_total`). **Estándar en Python**.


## **Variables y Estándares**

### **Concepto de Variable**

Una variable es un espacio de almacenamiento en la memoria, con un nombre simbólico, cuyo valor puede cambiar durante la ejecución a través de una dirección de memoria. Esta definición es algo técnica, por eso utilizaremos la siguiente analogía:

_Imagina una caja en una estantería etiquetada como_ `inventario_actual`_._ 

_Hoy la caja puede contener el número 100._ 

_Mañana, tras un despacho, esa misma caja (variable) contendrá el número 80._ 

_La caja (el espacio en memoria) es la misma; el contenido (valor) cambia._


### **La Importancia de los estándares de nomenclatura**

En ingeniería, el orden es la seguridad. Llamar a una variable `x` o `dato1` es tan peligroso como etiquetar una tubería química como "Tubo A". Nadie sabrá qué contiene en el futuro.

Debemos usar nombres descriptivos y seguir las convenciones del lenguaje:

1. **Python (nuestro curso):** Usa `snake_case`. Todo en minúsculas separado por guiones bajos.

   - _Bien:_ `temperatura_horno`, `velocidad_banda`.

   - _Mal:_ `TempHorno`, `variable1`.

2. **Java / JavaScript:** Usa `lowerCamelCase`.

   - _Ejemplo:_ `clienteActivo`, `idProducto`.

3. **SQL (Bases de Datos):** A menudo usa `UPPER_CASE` para comandos y `snake_case` para tablas.

   - _Ejemplo:_ `SELECT * FROM ordenes_compra`.

**Regla de Oro:** El código se lee más veces de las que se escribe. Un nombre claro ahorra horas de depuración.


## **Tipos de Datos (La "Forma" de la Caja)**

Elegir el **tipo de dato incorrecto** puede causar desde errores visuales hasta **catástrofes de cálculo**.


### **Enteros (Integer / int)**

Números sin parte decimal.

- **Uso:** Contar unidades discretas (piezas, personas, iteraciones). No existen "1.5 personas".

- **El caso "Gangnam Style":** En 2014, el video de "Gangnam Style" rompió YouTube. El contador de visitas estaba programado usando un entero de 32 bits con signo, cuyo valor máximo es 2,147,483,647. Cuando el video superó esa cifra, el contador se desbordó y empezó a mostrar números negativos. YouTube tuvo que actualizar urgentemente su arquitectura a enteros de 64 bits (que permiten trillones de visitas). _Moraleja: Subestimar el tamaño de tus datos es un riesgo de ingeniería._


### **Flotantes (Float / double)**

Números con decimales.

Como ingenieros, a menudo asumimos que la computadora es perfecta calculando. Sin embargo, cuando trabajamos con decimales, la computadora "miente" ligeramente debido a cómo almacena los números. Es vital entender la diferencia entre **Punto Flotante** y **Decimal Exacto**.

**A. Punto Flotante (**`Float`**)** Las computadoras no cuentan en base 10 (como los humanos), sino en base 2 (binario).

- **El Problema:** Hay números que son simples en base 10, pero "infinitos" en base 2. Por ejemplo, el número `0.1` (un décimo). Al igual que `1/3` en nuestra calculadora da `0.33333...` infinito, para la computadora `0.1` es una fracción binaria periódica infinita. La computadora tiene que "cortar" esa secuencia en algún punto para guardarla.

- **El Resultado:** Al cortar, se pierde una fracción infinitesimal de información.

  - _Prueba:_ Si preguntas a Python `0.1 + 0.2`, la respuesta **no** será `0.3`. Será `0.30000000000000004`.

* **Uso en Ingeniería:** Se usan `floats` para cálculos científicos, física o simulaciones donde la velocidad es crítica y un error de 0.000000001 es aceptable (por ejemplo, medir la temperatura de un horno, donde el sensor ya tiene un error mayor que el de la computadora).

**B. Decimal (**`Decimal`**)** Es un tipo de dato especial que almacena los números de forma exacta, tal como los escribimos en papel, sacrificando velocidad de procesamiento.

- **Uso en Ingeniería:** Cálculos financieros, inventarios de alto valor o tolerancias de manufactura ultra-precisas (nano-ingeniería), donde perder un centavo o un micrón es inaceptable.


### **Cadenas de Texto (String / str)**

Secuencias de caracteres alfanuméricos.

- **Uso:** Identificadores, códigos de barras, nombres, direcciones, comentarios, etc..

- **Nota:** El código "123" (texto) no es igual al número 123. No puedes sumar "10" + "10", el resultado sería "1010" (concatenación), no 20.


### **Booleanos (Boolean / bool)**

Valores de verdad lógica.

- **Uso:** Estados binarios (Encendido/Apagado, Válvula Abierta/Cerrada, 1/0). Solo admite `True` o `False`.

- **Nota:** Si observan, muchos interruptores o botones de encendido el “logo” es una mezcla entre  0 y 1.


### **Tipos Especializados y Personalizados**

Más allá de los básicos, existen tipos complejos:

- **Temporales:** `Date`, `Time`, `Datetime` (vitales para calcular Takt Time).

- **Geográficos:** Coordenadas GPS (Latitud, Longitud).

- **Objetos Personalizados:** Como ingenieros, podemos crear nuestros propios tipos. Podemos definir un tipo de dato `Pedido` que contenga dentro: fecha, cliente y lista de productos. La imaginación y la necesidad del problema son el límite.


#### **La Ingeniería y la Teoría del Caos: ¿Por qué nos importa la precisión?**

Podrías pensar: _"¿Qué importa un error de 0.0001 en una simulación?"_. La respuesta yace en la **Teoría del Caos**, un concepto que toda persona en ingeniería debe conocer, en especial quien trabajaba con simulaciones, como en la Ingeniería Industrial, para entender la estabilidad de los sistemas.

**El Efecto Mariposa** En 1961, el matemático y meteorólogo **Edward Lorenz** estaba simulando modelos climáticos en una computadora. Un día, quiso repetir una predicción. En lugar de ingresar el dato completo de la simulación anterior (`0.506127`), ingresó una versión redondeada (`0.506`) para ahorrar tiempo, asumiendo que una diferencia de una milésima no afectaría el resultado.

Al volver, encontró algo impactante: el clima simulado era **completamente diferente**. Ese minúsculo cambio inicial había crecido exponencialmente hasta alterar todo el sistema.

Lorenz describió esto con una metáfora famosa: _"El aleteo de una mariposa en Brasil puede provocar un tornado en Texas semanas después"_.

**Aplicación para la persona profesional en Ingeniería Industrial** Esto se conoce técnicamente como **Sensibilidad a las Condiciones Iniciales**.

1. **Simulaciones de Planta:** Si estás simulando una línea de producción de 10 años y usas datos de entrada con pequeños errores de redondeo (usando el tipo de dato incorrecto), tu proyección de costos a 10 años podría estar equivocada por millones de dólares.

2. **Control de Calidad:** En procesos químicos, una variación de 0.01% en la mezcla inicial puede resultar en un producto final inservible (polímeros que no curan, alimentos que se degradan).

3. **Lección:** La elección del tipo de dato (`Float` vs `Decimal`) y la precisión de tus algoritmos no es un detalle técnico menor; es lo que previene que el caos se apodere de tus predicciones.


## **Operadores: La Maquinaria de Transformación**

### **A. Operadores Aritméticos**

- `+` (Suma), 

- `-` (Resta), 

- `*` (Multiplicación), 

- `/` (División).


#### **El Operador Módulo (**`%`**)**

Devuelve el **residuo** de una división entera. A menudo es difícil de visualizar, pero es utilísimo:

- **Ejemplo 1 (Mantenimiento):** `pieza_numero % 1000 == 0`: "Cada 1000 piezas exactas, detener para lubricar".

- **Ejemplo 2 (Empaque):** Tienes 53 botellas y cajas de 6. `53 % 6 = 5`. Significa que te sobran 5 botellas que no llenan una caja completa.

- **Ejemplo 3 (Turnos):** Asignar tareas cíclicas. Si tienes 3 operarios (0, 1, 2), la tarea número `n` le toca al operario `n % 3`.


### **B. Operadores Relacionales (De Comparación)**

Comparan dos valores y **siempre** devuelve un booleano (`True` / `False`). Son los "ojos" del algoritmo, porque nos va servir determinar si debemos realizar una acción o si debemos continuar con una repetición de procesos.

- `>` (Mayor que), `<` (Menor que).

- `>=` (Mayor o igual), `<=` (Menor o igual).

- `==` (Igual a), `!=` (Diferente de).


## **Jerarquía de Operaciones**

La computadora no adivina, sigue reglas estrictas. El orden de resolución es:

1. **Paréntesis** `( )`: _Siempre rompen la jerarquía. Úsalos para dar claridad._

2. **Aritméticos**: `*`, `/`, `%` (primero), luego `+`, `-`.

3. **Relacionales**: `>`, `<`, `==`.

4. **Lógicos**: `NOT` (primero), luego `AND`, finalmente `OR`.
