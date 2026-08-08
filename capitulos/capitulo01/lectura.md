# **La Ingeniería Industrial y el Pensamiento Algorítmico**

## **El role de la persona profesional en Ingeniería Industrial como agente de transformación digital**

Bienvenidas y bienvenidos al curso _Fundamentos para Tecnologías Digitales_. En el entorno actual, la ingeniería industrial no se limita a la gestión física de la planta; requiere integrar herramientas computacionales para modelar, analizar y mejorar los procesos productivos.

Es fundamental hacer una distinción desde el primer día: 

**Programar no es lo mismo que codificar**

- **Codificar** \
  Es traducir instrucciones a un lenguaje específico (como Python) para que una computadora pueda ejecutar dichas instrucciones.

- **Programar** \
  Es un ejercicio mental de análisis ordenado. Es la capacidad de entender un problema, desglosarlo y diseñar una solución lógica y estructurada.

<img src="imagenes/ProgramarNoEsCodificar.png" alt="Programar No Es Codificar" width="100%">


**¿Por qué es vital esto para una persona profesional en  Ingeniería Industrial?** 

Aunque no te dediques al desarrollo de software, la programación estructura tu mente para el análisis de procesos (una habilidad indispensable en la Ingeniería Industrial). La programación te enseña a pensar en flujos de trabajo, manejo de excepciones (¿qué pasa si la máquina falla?) y optimización de recursos. Como ingeniera(o), estas capacidades te permitirán automatizar decisiones operativas y fortalecer tu rol como agente de transformación digital.

**Enfoque del curso:**

Durante estas primeras semanas, nos centraremos exclusivamente en el **análisis y el diseño** de la solución. Primero aprenderemos a resolver el problema en papel (diagramas y lógica) y, una vez que la solución sea sólida, la llevaremos al entorno computacional para su ejecución mediante un lenguaje de programación.


## **Conceptos Clave**

Antes de avanzar, vamos a definir el vocabulario esencial que utilizaremos en este capítulo y en el resto del curso, la idea es comunicarnos con :

- **Dato vs. Información:**

  - **Dato:** Es un valor crudo sin contexto. _Ejemplo: "180"_ (Por sí solo no dice nada).

  - **Información:** Es el dato procesado y con contexto que permite tomar decisiones. _Ejemplo: "La temperatura del horno es 180°C"_, lo cual nos indica que está operando normalmente.

- **Algoritmo:** Es una secuencia finita y ordenada de pasos para resolver un problema. Que si utilizamos los mismos datos, obtendremos la misma información. Debe ser repetible generando los mismos resultados.

- **Programa:** Es un algoritmo escrito en un lenguaje que una computadora puede interpretar y ejecutar.

- **Lenguaje de Programación:** Es el conjunto de reglas sintácticas (gramática) y semánticas (significado) que permiten a los humanos dar instrucciones a las computadoras.

- **Pensamiento Computacional:** Es la metodología de resolución de problemas que implica expresar las soluciones de tal manera que una computadora pueda ejecutarlas.


## **¿Qué es el Pensamiento Computacional?**

El Pensamiento Computacional es el cimiento sobre el cual se construye cualquier solución tecnológica. Sin este proceso mental, intentar escribir código es como intentar construir un edificio sin planos: el resultado será inestable y propenso a fallas.

<img src="imagenes/PensamientoComputacional.png" alt="PensamientoComputacional" width="100%">

### **La Inteligencia Artificial y el Programador**

Hoy en día existen herramientas de Inteligencia Artificial (IA) capaces de generar código. Podrías preguntarte: **_"¿Para qué aprender a programar si la IA lo hace por mí?"_.**

La respuesta es crítica para tu futuro profesional: **La IA es una herramienta, no el arquitecto.**

1. **Diseño de Soluciones:** Si no sabes diseñar la lógica de la solución, no sabrás qué pedirle a la IA. Una especificación vaga genera un código deficiente.

2. **Validación y Corrección:** Las IA cometen errores (alucinaciones). Si no tienes la habilidad de leer, entender y depurar la lógica, no podrás validar si el código que te entregó la herramienta es seguro para un entorno industrial.

3. **Especificaciones Precisas:** Al saber programar, puedes dar instrucciones técnicas exactas a las herramientas de IA, obteniendo resultados superiores.


### **Los 4 Pilares del Pensamiento Computacional en Ingeniería**

Para diseñar algoritmos exitosos, aplicamos cuatro pasos:

1. **Descomposición:** Romper un problema complejo en partes más manejables.

   - Por ejemplo,  si debes "Optimizar el área de despachos", no atacas todo el problema a la vez. Lo descompones en: recepción de pedidos, picking (recolección), embalaje y carga en camiones.

2. **Reconocimiento de Patrones:** Identificar similitudes con problemas resueltos anteriormente.

   - Si notas que el inventario se descuadra todos los viernes. Reconocer un patrón: el cambio de turno de los viernes no está registrando las mermas correctamente, similar a lo que pasaba en el almacén B el año pasado.

3. **Abstracción:** Filtrar la información irrelevante y centrarse en lo importante para el modelo.

   - Para calcular la eficiencia de una banda transportadora, necesitas saber la velocidad de la banda y la cantidad de unidades por minuto. No necesitas saber el color de la banda ni la marca del motor. Abstraer es simplificar.

4. **Diseño de Algoritmos:** Crear la serie de pasos para resolver el problema paso a paso.

<img src="imagenes/Los4Pilares.png" alt="Los4Pilares" width="100%">

## **El Algoritmo: La Receta del Proceso**

Imagina que estás escribiendo el "Procedimiento Estándar de Operación" (SOP) para encender una caldera. No puedes decir "enciéndela con cuidado". Debes decir: 

1. Abra la válvula de gas. 

2. Verifique la presión. 

3. Active el piloto 

**Eso es un algoritmo**

Un algoritmo productivo debe cumplir características estrictas:

- **Preciso:** Cada paso es claro y sin ambigüedades.

- **Finito:** Tiene un inicio y un fin; no se queda procesando infinitamente.

- **Definido (Determinista):** Si ingresamos las mismas entradas (Inputs) mil veces, debemos obtener exactamente la misma salida (Output) mil veces.

<img src="imagenes/QueEsUnAlgoritmo.png" alt="QueEsUnAlgoritmo" width="100%">

### **El Modelo Entrada - Proceso - Salida (IPO) y el Valor Agregado**

Este modelo es universal tanto en informática como en manufactura. El objetivo final de cualquier proceso es generar **Valor Agregado**.

| Etapa                 | En Informática (Algoritmo)                                             | En Ingeniería Industrial (Fábrica)                                  |
| --------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Entrada (Input)**   | Datos brutos, variables, lecturas de sensores, pulsaciones de teclado. | Materia prima, insumos, energía, órdenes de producción.             |
| **Proceso (Process)** | Cálculos matemáticos, lógica de decisión, transformación de datos.     | Transformación física, ensamblaje, tratamiento químico, mecanizado. |
| **Salida (Output)**   | Información útil, reportes, alertas, gráficos.                         | Producto terminado, subensamble listo, desperdicio controlado.      |

Como ingenieros, diseñamos algoritmos para que la "Salida" sea información de valor que permita tomar decisiones o controlar el proceso físico.

<img src="imagenes/ModeloIPO.png" alt="ModeloIPO" width="100%">
