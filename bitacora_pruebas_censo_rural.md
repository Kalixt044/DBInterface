# Bitácora de pruebas ejecutadas — Censo Rural

## 1. Información general
- Proyecto: Censo Rural
- Fecha de ejecución: 2026-08-30
- Alcance: backend API y lógica de cálculo de edad del desktop
- Entorno: Python 3.12 + pytest con FastAPI TestClient

## 2. Resultado general
Se ejecutaron pruebas funcionales sobre:
- la lógica de cálculo de edad en la versión de escritorio,
- la API CRUD de la versión web,
- manejo de errores básicos y validación de entradas.

## 3. Resumen de resultados
- Total de pruebas ejecutadas: 6
- Pruebas aprobadas: 6
- Pruebas fallidas: 0
- Estado general: aprobado

## 4. Casos ejecutados
- CT-01: cálculo de edad válido
- CT-02: fecha inválida
- CT-03: inserción de registro
- CT-04: retorno 400 por payload inválido
- CT-05: retorno 404 por registro inexistente
- CT-06: actualización y eliminación del registro

## 5. Observaciones
- La lógica de cálculo de edad del archivo desktop funciona con los valores esperados.
- La API CRUD cumple con las operaciones básicas de creación, consulta, actualización y eliminación.
- Las validaciones de error responden correctamente con códigos HTTP esperados.

## 6. Conclusión
Las pruebas ejecutadas validan el comportamiento principal del software y cumplen con la intención del plan de pruebas. Se recomienda continuar con pruebas de integración visual y de regresión para cubrir la interfaz web completa.
