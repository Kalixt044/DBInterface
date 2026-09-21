# Documento de evidencias para pruebas del software Censo Rural

## 1. Información general
- Proyecto: Censo Rural
- Fecha: 2026-08-30
- Versión del documento: 1.0
- Alcance: versión de escritorio y versión web
- Objetivo: documentar la forma en que se van a ejecutar, registrar y justificar las pruebas del software, manteniendo trazabilidad con los requisitos funcionales y no funcionales.

> Este documento responde las preguntas orientadoras para la evidencia de pruebas sin incluir videos, capturas ni archivos físicos de ejecución. Se centra en la planificación, trazabilidad y cumplimiento del plan GA9-220501096-AA3-EV01.

---

## 2. ¿Qué software se está probando?

Se prueba el sistema Censo Rural en dos versiones:

1. Versión de escritorio
   - Desarrollada en Python con interfaz gráfica.
   - Permite registrar datos personales.
   - Calcula la edad a partir de la fecha de nacimiento.
   - Formatea texto y guarda información en CSV.
   - Tiene integración con SQLite para la persistencia de datos.

2. Versión web
   - Backend con FastAPI.
   - Frontend con React.
   - Permite consultar, insertar, actualizar y eliminar registros.
   - Tiene validación de campos y mensajes de estado para la operación del formulario.

---

## 3. ¿Qué se busca evidenciar con las pruebas?

Las pruebas tienen como propósito demostrar que:
- el sistema registra correctamente la información del censo,
- la validación funciona con datos correctos e incorrectos,
- la lógica de cálculo de edad es coherente,
- la persistencia se realiza en SQLite o CSV según la versión,
- el backend y la interfaz web responden correctamente ante errores,
- la trazabilidad entre requisitos y pruebas queda documentada.

---

## 4. ¿Qué requisitos funcionales se validan?

### Requisitos funcionales principales
- RF-01: El sistema debe permitir registrar una persona.
- RF-02: Debe validar que los campos obligatorios estén diligenciados.
- RF-03: Debe guardar la información en una estructura persistente.
- RF-04: Debe calcular la edad a partir de la fecha de nacimiento.
- RF-05: Debe aceptar los tipos de documento requeridos por el proyecto.
- RF-06: Debe permitir consultar registros existentes.
- RF-07: Debe permitir actualizar registros.
- RF-08: Debe permitir eliminar registros.
- RF-09: Debe mostrar mensajes de éxito y error.
- RF-10: La interfaz debe ser clara y usable.

### Requisitos no funcionales a considerar
- RNF-01: La lógica debe ser consistente y determinista.
- RNF-02: La persistencia debe mantenerse segura y ordenada.
- RNF-03: El sistema debe soportar escenarios normales y de error.
- RNF-04: La experiencia de usuario debe ser comprensible y controlada.

---

## 5. ¿Qué elementos se prueban en la versión de escritorio?

Se prueba lo siguiente:
- ingreso de datos en el formulario Tkinter,
- validación de fechas y texto,
- cálculo de la edad,
- formulario de registro con campos obligatorios,
- almacenamiento en CSV,
- tratamiento de errores en entradas inválidas,
- integración entre interfaz y almacenamiento,
- limpieza del formulario después de una operación exitosa.

---

## 6. ¿Qué elementos se prueban en la versión web?

Se prueba lo siguiente:
- carga del formulario de registro,
- validación de campos obligatorios,
- envío del formulario al backend,
- respuestas correctas de la API,
- lectura, actualización y eliminación de registros,
- persistencia en SQLite,
- manejo de errores HTTP,
- visualización del estado del formulario,
- integración frontend-backend.

---

## 7. ¿Qué preguntas orientan la validación del comportamiento del software?

### 7.1 ¿El sistema registra correctamente la información?
Sí, siempre que los datos sean válidos y los campos obligatorios estén completos. La prueba se centra en verificar que la información ingresada queda almacenada sin pérdidas ni inconsistencias.

### 7.2 ¿La edad calculada es correcta?
La lógica debe calcular la diferencia entre la fecha actual y la fecha de nacimiento, ajustando el caso en que aún no se haya cumplido el cumpleaños del año actual.

### 7.3 ¿La validación de campos funciona?
La prueba debe comprobar que se impide el registro si faltan datos obligatorios o si se envían valores con formato inválido.

### 7.4 ¿La API responde conforme a la operación solicitada?
La API debe devolver respuestas exitosas para registros válidos y mensajes claros para errores, como datos vacíos, identificadores inexistentes o solicitudes incorrectas.

### 7.5 ¿La persistencia es consistente?
La información registrada debe poder consultarse, actualizarse y eliminarse según la operación solicitada, sin perder integridad.

### 7.6 ¿Se detectan errores de entrada?
Sí. Se debe verificar el comportamiento frente a fechas inválidas, campos vacíos, tipos de documento no permitidos, registros inexistentes, y requisitos faltantes.

### 7.7 ¿La lógica es consistente entre versión web y escritorio?
Ambas versiones deben cumplir la misma intención funcional: registrar, validar, persistir y consultar datos del censo rural con comportamiento coherente.

---

## 8. ¿Cómo se garantiza la trazabilidad del software?

La trazabilidad se realizará así:
- cada caso de prueba se asocia a un requisito funcional o no funcional,
- se documenta el identificador, el objetivo, los datos de prueba, los pasos, el resultado esperado y el estado final,
- cada prueba se clasifica según versión: escritorio, web o ambas,
- se registra si el caso fue aprobado, fallido o no ejecutado,
- los riesgos y contingencias se documentan para respaldar decisiones y ajustes.

---

## 9. Criterios de aceptación

Se considera aceptada la prueba cuando:
- el registro funciona correctamente en la versión de escritorio y web,
- los campos obligatorios se validan correctamente,
- la edad se calcula sin errores lógicos,
- la API responde según lo esperado,
- la persistencia permite consultar, actualizar y eliminar registros,
- no se presentan fallos críticos en el flujo normal del sistema.

---

## 10. Ambiente de pruebas y datos

### Entorno
- Sistema operativo: Linux
- Python 3.12+
- FastAPI para backend web
- React para frontend
- SQLite para almacenamiento
- Navegador para validación de la web
- CSV como almacenamiento del escritorio

### Datos de prueba
- registro válido con datos completos,
- registro con fecha de nacimiento válida,
- registro con fecha inválida,
- registro con campos obligatorios vacíos,
- registro con documento duplicado,
- registro con nombre o dirección en formatos distintos,
- registro con información incompleta para consultar o eliminar.

---

## 11. Riesgos y contingencias

### Riesgos principales
- formatos de fecha inconsistentes,
- campos obligatorios faltantes,
- datos duplicados,
- diferencias entre entorno local y producción,
- inconsistencias entre CSV y SQLite,
- errores de integración entre frontend y backend.

### Contingencias
- usar datos de prueba controlados y no sensibles,
- preparar archivos CSV y tablas SQLite con datos limpios,
- ejecutar la prueba en entorno local antes de generar evidencia formal,
- validar la API antes de probar la interfaz,
- registrar incidencias para seguimiento y corrección.

---

## 12. Matriz de trazabilidad

| Requisito | Versión | Tipo de prueba | Resultado esperado |
|---|---|---|---|
| RF-01 Registro de persona | Escritorio y Web | Funcional | Se crea el registro correctamente |
| RF-02 Validación | Escritorio y Web | Funcional | Se bloquea la operación si faltan datos |
| RF-03 Persistencia | Escritorio y Web | Integración | Los datos quedan almacenados |
| RF-04 Cálculo de edad | Escritorio y Web | Funcional | La edad calculada es correcta |
| RF-05 Tipo de documento | Escritorio y Web | Validación | Se aceptan o rechazan según la regla |
| RF-06 Consulta | Web | Funcional | Se listan correctamente los registros |
| RF-07 Actualización | Web | Funcional | El dato cambia correctamente |
| RF-08 Eliminación | Web | Funcional | El registro desaparece del sistema |
| RF-09 Mensajes | Escritorio y Web | UI/UX | Se muestran mensajes claros |
| RNF-01 Consistencia | Escritorio y Web | No funcional | La lógica devuelve resultados estables |

---

## 13. Conclusión

La evidencia de pruebas requerida para GA9-220501096-AA3-EV01 debe quedar documentada como un proceso trazable, con relación directa entre requisitos, pruebas y resultados esperados. Este documento establece la base para la evidencia formal del comportamiento del software del censo rural en sus dos versiones: escritorio y web.

---

## 14. Documentos relacionados
- [test_plan_censo_rural.md](test_plan_censo_rural.md)
- [plan_pruebas_censo_rural.md](plan_pruebas_censo_rural.md)


---------*******----------*******--------*****-*****------*****

# Plan de pruebas del software Censo Rural

## 1. Información general
- Proyecto: Censo Rural
- Fecha: 2026-08-30
- Versión del documento: 1.0
- Tipo de software: sistema de registro y gestión de datos poblacionales rurales
- Versiones a probar:
  - Escritorio (Python)
  - Web (FastAPI + React)
- Objetivo: verificar la funcionalidad, la integridad y la usabilidad del sistema según los requisitos del proyecto.

---

## 2. Objetivo del plan

El plan de pruebas tiene como propósito validar que el sistema:
- registra correctamente la información del censo,
- valida oportunamente los datos obligatorios,
- calcula la edad de manera consistente,
- guarda la información en la estructura de persistencia correcta,
- responde apropiadamente ante entradas válidas e inválidas,
- ofrece una experiencia funcional y estable tanto en la versión desktop como en la web.

---

## 3. Alcance

### 3.1 Versión de escritorio
Se validan:
- formulario de registro,
- cálculo de edad,
- formato de entradas,
- validación de fechas,
- almacenamiento en CSV,
- manejo de errores,
- flujo general de la operación.

### 3.2 Versión web
Se validan:
- formulario de ingreso,
- validación visual y lógica,
- consumo de la API,
- operaciones CRUD,
- manejo de errores HTTP,
- consulta, edición y eliminación de registros,
- comportamiento del sistema con entradas incorrectas.

---

## 4. Referencias
- Requisitos del proyecto en [agosto_4Sem.txt](agosto_4Sem.txt)
- Documento base [test_plan_censo_rural.md](test_plan_censo_rural.md)
- Estructura funcional del proyecto:
  - [DesktopProyect](DesktopProyect)
  - [ProyectoWeb/Back](ProyectoWeb/Back)
  - [ProyectoWeb/Front](ProyectoWeb/Front)

---

## 5. Ambiente de pruebas

### 5.1 Entorno local
- Sistema operativo: Linux
- Python 3.12+
- SQLite para pruebas
- Servidor FastAPI local
- Navegador para pruebas web
- Datos de prueba aislados y no sensibles

### 5.2 Datos de prueba recomendados
- registro válido con información completa,
- registro con fecha de nacimiento válida,
- registro con fecha inválida,
- registro con campos obligatorios vacíos,
- registro con documento duplicado,
- registro con formato de email incorrecto,
- registro con nombre y dirección en mayúsculas y minúsculas.

### 5.3 Preparación del entorno
- verificar la base de datos,
- comprobar la conexión del backend con SQLite,
- cargar datos iniciales para pruebas de consulta y actualización,
- limpiar archivos CSV antes de una ejecución,
- restaurar la base de datos antes de cada ronda de pruebas.

---

## 6. Estrategia de pruebas

### 6.1 Pruebas funcionales
Validan que cada requisito del sistema se cumpla tanto en desktop como web.

### 6.2 Pruebas de integración
Verifican la comunicación entre frontend y backend, especialmente para la versión web.

### 6.3 Pruebas de validación de entrada
Controlan campos vacíos, formato incorrecto y valores no permitidos.

### 6.4 Pruebas de regresión
Se ejecutan después de cambios en lógica o en la interfaz para asegurar que no se rompió la funcionalidad base.

### 6.5 Pruebas de rendimiento
Se evalúa la respuesta del sistema frente a consultas y registros en volumen moderado.

### 6.6 Pruebas de seguridad básica
Se revisa la integridad de la persistencia y la validación de entradas.

---

## 7. Criterios de entrada y salida

### Criterios de entrada
- el sistema está instalado y ejecutándose,
- la base de datos está disponible,
- los datos de prueba están cargados,
- las funciones de registro, consulta y actualización están accesibles.

### Criterios de salida
- el registro se realiza según la lógica esperada,
- las operaciones fallidas generan mensajes claros,
- la consulta devuelve información consistente,
- la evidencia queda registrada con resultado y observaciones.

---

## 8. Matriz de cobertura de pruebas

| ID | Requisito | Módulo | Tipo de prueba | Prioridad | Estado |
|---|---|---|---|---|---|
| TC-01 | Registro de persona | Escritorio | Funcional | Alta | Pendiente |
| TC-02 | Cálculo de edad | Escritorio | Funcional | Alta | Pendiente |
| TC-03 | Fecha inválida | Escritorio | Validación | Alta | Pendiente |
| TC-04 | Guardado en CSV | Escritorio | Integración | Alta | Pendiente |
| TC-05 | Campos obligatorios | Escritorio | Funcional | Alta | Pendiente |
| TC-06 | Registro web válido | Web | Funcional | Alta | Pendiente |
| TC-07 | Validación de formulario | Web | Validación | Alta | Pendiente |
| TC-08 | Consulta de registros | Web | Funcional | Alta | Pendiente |
| TC-09 | Actualización de registro | Web | Funcional | Alta | Pendiente |
| TC-10 | Eliminación de registro | Web | Funcional | Alta | Pendiente |
| TC-11 | Error 404 | Web | Integración | Media | Pendiente |
| TC-12 | Error 400 | Web | Integración | Media | Pendiente |
| TC-13 | Persistencia en SQLite | Web | Integración | Alta | Pendiente |
| TC-14 | Regresión | Web/Escritorio | Regresión | Media | Pendiente |
| TC-15 | Rendimiento moderado | Web/Escritorio | Rendimiento | Media | Pendiente |

---

## 9. Casos de prueba propuestos

### TC-01: Registro exitoso en escritorio
- Objetivo: verificar que el sistema registra una persona con datos válidos.
- Requisito asociado: RF-01
- Precondiciones: formulario abierto con datos completos.
- Pasos:
  1. Ingresar nombre, apellido, documento y fecha de nacimiento.
  2. Ejecutar guardar registro.
- Resultado esperado: se guarda la información y se muestra confirmación.

### TC-02: Cálculo de edad en escritorio
- Objetivo: comprobar que la edad se calcula correctamente.
- Requisito asociado: RF-04
- Pasos:
  1. Ingresar una fecha de nacimiento válida.
  2. Ejecutar el cálculo.
- Resultado esperado: la edad calculada coincide con la diferencia real de años.

### TC-03: Fecha inválida en escritorio
- Objetivo: validar que la aplicación rechaza fechas mal formateadas.
- Requisito asociado: RF-04
- Pasos:
  1. Ingresar una fecha con formato inválido.
  2. Intentar guardar.
- Resultado esperado: el sistema impide la operación y muestra error.

### TC-04: Guardado en CSV
- Objetivo: confirmar la persistencia del registro en archivo CSV.
- Requisito asociado: RF-03
- Pasos:
  1. Registrar un dato válido.
  2. Revisar el archivo de salida.
- Resultado esperado: el registro aparece en el archivo con la estructura correcta.

### TC-05: Campos obligatorios faltantes
- Objetivo: verificar la validación del formulario.
- Requisito asociado: RF-02
- Pasos:
  1. Dejar vacío un campo obligatorio.
  2. Intentar guardar.
- Resultado esperado: la operación queda bloqueada con mensaje de error.

### TC-06: Registro exitoso en web
- Objetivo: validar el flujo del formulario hasta la API.
- Requisito asociado: RF-01
- Precondiciones: API en funcionamiento y formulario cargado.
- Pasos:
  1. Completar el formulario con datos válidos.
  2. Enviar la información.
- Resultado esperado: respuesta exitosa y registro persistido.

### TC-07: Validación de formulario web
- Objetivo: comprobar que los campos obligatorios del formulario se validan.
- Requisito asociado: RF-02
- Pasos:
  1. Dejar vacío un campo requerido.
  2. Enviar el formulario.
- Resultado esperado: no se crea el registro y se muestra un mensaje de error.

### TC-08: Consulta de registros web
- Objetivo: verificar la lectura de los datos existentes.
- Requisito asociado: RF-06
- Pasos:
  1. Consultar la lista de registros.
- Resultado esperado: los datos aparecen en el listado con formato correcto.

### TC-09: Actualización de registro web
- Objetivo: validar la edición de un registro existente.
- Requisito asociado: RF-07
- Pasos:
  1. Seleccionar un registro.
  2. Modificar los datos.
  3. Confirmar la actualización.
- Resultado esperado: la información queda modificada y persistida.

### TC-10: Eliminación de registro web
- Objetivo: validar la borrado del registro.
- Requisito asociado: RF-08
- Pasos:
  1. Seleccionar un registro.
  2. Ejecutar eliminación.
- Resultado esperado: el registro ya no aparece en la consulta.

### TC-11: Error 404 para registro inexistente
- Objetivo: probar la respuesta del sistema cuando no se encuentra el registro.
- Requisito asociado: RF-06, RF-07, RF-08
- Pasos:
  1. Consultar o editar un ID inexistente.
- Resultado esperado: respuesta 404 con mensaje de no encontrado.

### TC-12: Error 400 por payload incompleto
- Objetivo: verificar manejo de error ante datos incompletos.
- Requisito asociado: RF-02
- Pasos:
  1. Enviar un JSON incompleto o estructura incorrecta.
- Resultado esperado: respuesta 400 con mensaje claro.

### TC-13: Persistencia en SQLite
- Objetivo: confirmar que los datos quedan guardados en la base de datos.
- Requisito asociado: RF-03
- Pasos:
  1. Registrar un registro.
  2. Consultar la tabla correspondiente.
- Resultado esperado: la base de datos refleja el registro creado.

### TC-14: Prueba de regresión
a- Objetivo: asegurar que funcionalidades críticas no se rompen al cambiar el sistema.
- Requisito asociado: RF-01 a RF-09
- Pasos:
  1. Ejecutar pruebas clave del registro, validación y consulta.
- Resultado esperado: todas las pruebas base siguen funcionando.

### TC-15: Prueba de rendimiento
- Objetivo: evaluar la respuesta del sistema con una cantidad moderada de registros.
- Requisito asociado: RNF-01, RNF-03
- Pasos:
  1. Cargar un conjunto moderado de registros.
  2. Ejecutar consultas y creación de nuevos datos.
- Resultado esperado: el sistema responde sin bloqueos significativos.

---

## 10. Riesgos y contingencias
- fechas con formato incorrecto,
- datos duplicados,
- inconsistencias de datos entre CSV y SQLite,
- cambios en la lógica de cálculo de edad,
- mala conexión del backend con la base de datos,
- errores de interfaz por validaciones insuficientes.

Contingencias:
- preparar una base de prueba estandarizada,
- limpiar datos antes de cada ciclo,
- validar la estructura del CSV y la tabla SQLite,
- documentar incidencias y aplicar correcciones,
- ejecutar pruebas de regresión después de ajustes funcionales.

---

## 11. Artefactos esperados
- plan de pruebas,
- matriz de cobertura,
- casos de prueba,
- bitácora de ejecución,
- informe de resultados,
- trazabilidad entre requisitos y pruebas.

---

## 12. Conclusión

El plan propuesto es adecuado para el proyecto, porque cubre la funcionalidad principal del sistema, la validación de entradas, la persistencia, la integración entre capas y la trazabilidad de requisitos. Además, se ajusta al alcance real del software observado en la versión desktop y la versión web.

---

## 13. Documentos relacionados
- [documento_evidencias_pruebas_censo_rural.md](documento_evidencias_pruebas_censo_rural.md)
- [test_plan_censo_rural.md](test_plan_censo_rural.md)

- Requisito asociado: RF-03
- Pasos:
  1. Registrar un dato.
  2. Consultarlo nuevamente.
- Resultado esperado: el dato persiste y se recupera con la misma estructura.

### 9.14 Caso de prueba TC-14: Prueba de regresión
- Objetivo: asegurar que cambios recientes no afectan flujos críticos.
- Requisito asociado: RNF-01
- Pasos:
  1. Revisar registro, consulta y actualización.
- Resultado esperado: el sistema funciona de manera estable.

### 9.15 Caso de prueba TC-15: Carga moderada
- Objetivo: revisar comportamiento general con volumen de datos moderado.
- Requisito asociado: RNF-03
- Pasos:
  1. Registrar varios registros consecutivos.
  2. Consultar la lista con varios elementos.
- Resultado esperado: las operaciones se ejecutan sin fallas graves ni tiempos excesivos.

---

## 10. Riesgos y contingencias

### Riesgos principales
- Inconsistencia en los nombres de campos entre CSV y SQLite.
- Validación insuficiente de documentos duplicados o emails repetidos.
- Uso de fechas con formato incorrecto.
- Diferencias entre datos locales y datos de producción simulada.
- Errores de integración entre frontend y backend.

### Contingencias
- Mantener un conjunto de datos de prueba controlados.
- Hacer limpieza de base de datos antes de la ejecución.
- Verificar la estructura de la tabla antes de ejecutar CRUD.
- Validar el comportamiento por capas: formulación, API y persistencia.
- Establecer un criterio de evaluacion para casos fallidos.

---

## 11. Artefactos esperados

- Documento de requerimientos del sistema.
- Matriz de trazabilidad de requisitos a pruebas.
- Plan de pruebas del proyecto.
- Registro de resultados por caso de prueba.
- Documento de conclusiones del proceso de pruebas.

---

## 12. Cronograma sugerido

| Fase | Actividad | Duración estimada |
|---|---|---|
| Fase 1 | Revisión de requisitos y alcance | 1 sesión |
| Fase 2 | Diseño de casos de prueba | 1 sesión |
| Fase 3 | Preparación del ambiente | 1 sesión |
| Fase 4 | Ejecución de pruebas desktop | 1 sesión |
| Fase 5 | Ejecución de pruebas web | 1 sesión |
| Fase 6 | Cierre e informe final | 1 sesión |

---

## 13. Conclusión

El plan de pruebas del software Censo Rural contempla la validación realista de las dos versiones del sistema, asegurando que la lógica de negocio, la persistencia y la interacción del usuario cumplan con los requisitos del proyecto. Este documento sirve como base para la ejecución técnica y la trazabilidad del comportamiento del software en la fase de verificación.












