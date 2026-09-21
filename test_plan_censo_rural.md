# Plan de pruebas — Proyecto Censo Rural

Fecha: 2026-08-30

## 1. Resumen ejecutivo
- Objetivo: definir la estrategia de pruebas para las versiones web y de escritorio del sistema Censo Rural.
- Alcance: validación funcional, de integración, de validación de entrada, de regresión y de rendimiento.
- Base documental: [agosto_4Sem.txt](agosto_4Sem.txt), [sem1_mes18.txt](sem1_mes18.txt) y la estructura real del proyecto.

## 2. Alcance
- Versión desktop: validación del flujo de captura, cálculo de edad, formato y almacenamiento en CSV.
- Versión web: validación del formulario, API, persistencia en SQLite y operaciones CRUD.

## 3. Criterios de validación
- comprobar que se cumplen los requisitos funcionales del sistema,
- verificar el manejo de errores ante datos inválidos,
- asegurar la persistencia y trazabilidad de la información,
- documentar la ejecución de pruebas y su estado final.

## 4. Entorno de pruebas
- Desarrollo local con Linux.
- Python 3.12 o superior.
- FastAPI para la API web.
- React para la interfaz web.
- SQLite como base de datos para pruebas.
- CSV para la versión desktop.
- Datos de prueba controlados, no sensibles.

## 5. Estrategia de pruebas
- Funcionales: validan que cada requisito del sistema se cumple.
- De integración: verifican la comunicación frontend-backend.
- De validación: controlan entradas vacías o mal formateadas.
- De regresión: aseguran que las funcionalidades críticas sigan funcionando.
- De rendimiento: evalúan la respuesta frente a volumen moderado de datos.

## 6. Matriz de cobertura

| ID | Requisito | Versión | Tipo de prueba |Prioridad|
|---|---|---|---|---|
| TC-01 | Registro válido | Escritorio | Funcional | Alta |
| TC-02 | Cálculo de edad | Escritorio | Funcional | Alta |
| TC-03 | Fecha inválida | Escritorio | Validación | Alta |
| TC-04 | Guardado en CSV | Escritorio | Integración | Alta |
| TC-05 | Campos obligatorios | Escritorio | Funcional | Alta |
| TC-06 | Registro válido en web | Web | Funcional | Alta |
| TC-07 | Validación formulario web | Web | Validación | Alta |
| TC-08 | Consulta de registros | Web | Funcional | Alta |
| TC-09 | Actualización | Web | Funcional | Alta |
| TC-10 | Eliminación | Web | Funcional | Alta |
| TC-11 | Error 404 | Web | Integración | Media |
| TC-12 | Error 400 | Web | Integración | Media |
| TC-13 | Persistencia SQLite | Web | Integración | Alta |
| TC-14 | Regresión | Web / Escritorio | Regresión | Media |
| TC-15 | Rendimiento | Web / Escritorio | Rendimiento | Media |

## 7. Casos de prueba

### TC-01: Registro exitoso en escritorio
- Objetivo: verificar que se guarda un registro válido.
- Resultado esperado: la información queda almacenada y el sistema muestra confirmación.

### TC-02: Cálculo de edad en escritorio
- Objetivo: verificar que la edad es coherente con la fecha de nacimiento.
- Resultado esperado: el valor calculado coincide con la realidad.

### TC-03: Fecha inválida en escritorio
- Objetivo: comprobar que no se acepta una fecha mal escrita.
- Resultado esperado: se bloquea la operación y se informa al usuario.

### TC-04: Guardado en CSV
- Objetivo: validar la persistencia en archivo CSV.
- Resultado esperado: el registro queda incluido en la estructura esperada.

### TC-05: Campos obligatorios faltantes
- Objetivo: verificar que no se graba información incompleta.
- Resultado esperado: no se ejecuta la operación y se muestra un mensaje de error.

### TC-06: Registro exitoso en web
- Objetivo: comprobar el flujo completo del formulario y la API.
- Resultado esperado: la operación responde correctamente y persiste el registro.

### TC-07: Validación de formulario web
- Objetivo: asegurar que se rechaza la información incompleta.
- Resultado esperado: se devuelve error y no se genera el registro.

### TC-08: Consulta de registros web
- Objetivo: verificar que la API entrega la información correcta.
- Resultado esperado: la consulta retorna registros existentes.

### TC-09: Actualización de registro
- Objetivo: validar que una modificación queda guardada.
- Resultado esperado: el registro cambia de forma consistente.

### TC-10: Eliminación de registro
- Objetivo: comprobar que un registro puede borrarse.
- Resultado esperado: el dato deja de aparecer en la consulta.

### TC-11: Error 404
- Objetivo: validar la respuesta del sistema ante registros inexistentes.
- Resultado esperado: respuesta de error con mensaje claro.

### TC-12: Error 400
- Objetivo: comprobar el manejo de datos incompletos o inválidos.
- Resultado esperado: respuesta 400 con detalle del problema.

### TC-13: Persistencia SQLite
- Objetivo: verificar la integridad del almacenamiento en base de datos.
- Resultado esperado: el registro queda visible en la tabla correspondiente.

### TC-14: Prueba de regresión
- Objetivo: confirmar que las pruebas críticas siguen funcionando tras cambios.
- Resultado esperado: sin regresiones en el flujo principal.

### TC-15: Rendimiento moderado
- Objetivo: considerar comportamiento bajo carga controlada.
- Resultado esperado: respuesta estable sin bloqueos importantes.

## 8. Riesgos y contingencias
- Fechas mal digitadas.
- Datos incompletos.
- Duplicidad de documentos.
- Diferencias entre entorno local y producción.
- Inconsistencias entre CSV y SQLite.

Contingencias:
- preparar datos de prueba controlados,
- ejecutar validaciones previas antes de cada prueba,
- documentar incidencias y aplicar correcciones,
- repetir pruebas tras cambios en la lógica.

## 9. Entregables
- plan de pruebas,
- matriz de cobertura,
- casos de prueba,
- bitácora de ejecución,
- informe de resultados,
- trazabilidad requisitos-pruebas.

## 10. Conclusión
El plan propuesto es adecuado para este proyecto porque cubre las pruebas funcionales reales del sistema, la validación de entrada, la persistencia y la integración de las capas desktop y web. Se alinea con la estructura del software y con los requisitos del censo rural.

---
Documento base ajustado para evidencias de pruebas del sistema Censo Rural.
