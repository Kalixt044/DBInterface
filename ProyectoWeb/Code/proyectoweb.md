# Propuesta de cambio: eliminar campo Edad del formulario

## Objetivo

Omitir el campo `edad` del formulario y calcularlo automáticamente con base en la `fecha_nacimiento` tomando como referencia la fecha actual.

## Situación actual

- En `Front/src/constants/formConfig.js` existe el campo `edad` en `initialForm` y `campoLabels`.
- El formulario (`Front/src/components/FormPersona.jsx`) construye los campos desde `campoLabels`, por lo que actualmente muestra el campo `Edad`.
- En `Front/src/App.jsx`, el objeto `formValues` se envía al backend tal como fue ingresado, sin ningún cálculo automático de edad.
- El backend en `Back/app/routes/crud.py` inserta y actualiza los registros con los datos recibidos, incluyendo `edad` si viene en el payload.
- La tabla de la base de datos en `Back/app/services/database.py` define la columna `edad` con un `CHECK` para valores entre 0 y 120.

## Cambios necesarios

### 1. Frontend: eliminar el campo de la UI

Modificar `Front/src/constants/formConfig.js`:
- Eliminar `edad` de `initialForm`.
- Eliminar el objeto `{ name: 'edad', label: 'Edad', type: 'number' }` de `campoLabels`.

Este cambio hará que el campo `Edad` desaparezca del formulario sin afectar el resto de campos.

### 2. Frontend: calcular la edad automáticamente antes de enviar

Modificar `Front/src/App.jsx` para:
- Añadir una función utilitaria `computeAge(fechaNacimiento)` que transforme la fecha en edad.
- Aplicar esa función a `formValues.fecha_nacimiento` antes de llamar a `validateForm` y antes de enviar los datos al backend.
- En `handleSubmit`, construir el objeto a enviar como:
  - `const submissionData = { ...formValues, edad: computeAge(formValues.fecha_nacimiento) }`
- En caso de edición (`PUT`), usar el mismo `submissionData`.

Esto asegura que la edad se derive de forma consistente en el cliente.

### 3. Frontend: ajustar validación si es necesario

Revisar `Front/src/utils/validation.js`:
- Actualmente solo valida campos obligatorios y no requiere `edad`.
- Si se agregara validación de `fecha_nacimiento`, debe considerar que `edad` ya no es ingresado manualmente.

### 4. Backend: asegurar que la edad no dependa de un campo ingresado por el usuario

Opción mínima y recomendada:
- Mantener la columna `edad` en la tabla `personas`.
- Actualizar `Back/app/routes/crud.py` para que, antes de `insert_record` o `update_record`, calcule `edad` a partir de `fecha_nacimiento`.
- Ignorar el valor `edad` enviado por el cliente y reemplazarlo con el valor calculado.

Esto protege el backend ante datos malformados o falsificados.

Opción alternativa (más estructural):
- Eliminar la columna `edad` de la tabla `personas`.
- Calcular la edad al generar las respuestas en la API o en el frontend cuando se muestran registros.

### 5. Documentación y ejemplos

Actualizar ejemplos de payload/documentación si los hubiera, por ejemplo en `Back/postman_collection.md`, para indicar que el JSON ya no debe incluir `edad`.

## Archivos clave afectados

- `Front/src/constants/formConfig.js`
- `Front/src/components/FormPersona.jsx` (indirectamente, porque usa `campoLabels`)
- `Front/src/App.jsx`
- `Front/src/utils/validation.js` (solo si se ajusta validación adicional)
- `Back/app/routes/crud.py`
- `Back/app/services/database.py` (si se decide mantener o eliminar la columna `edad`)
- `Back/postman_collection.md` (documentación de ejemplo)

## Propuesta de implementación paso a paso

1. Eliminar el campo `edad` del `formConfig`.
2. Crear la función `computeAge` en `App.jsx`.
3. Ajustar `handleSubmit` para enviar `submissionData` con la edad calculada.
4. Probar el formulario para confirmar que la edad ya no se ingresa manualmente.
5. Actualizar el backend para recalcular edad en las rutas `POST /insert` y `PUT /{id}`.
6. Validar un registro creado y un registro editado para verificar que la edad es correcta.

## Estado de implementación

- El campo `edad` fue eliminado del frontend en `Front/src/constants/formConfig.js`.
- La edad ahora se calcula automáticamente en `Front/src/App.jsx` antes de enviar los datos.
- El backend en `Back/app/services/database.py` recalcula `edad` a partir de `fecha_nacimiento` en `insert_record` y `update_record`.
- Se actualizó el ejemplo de payload en `Back/postman_collection.md` para no enviar `edad` manualmente.

## Cálculo recomendado de edad

Una forma segura de calcular la edad es:

```js
function computeAge(fechaNacimiento) {
  if (!fechaNacimiento) return null;
  const today = new Date();
  const birthDate = new Date(fechaNacimiento);
  let age = today.getFullYear() - birthDate.getFullYear();
  const monthDiff = today.getMonth() - birthDate.getMonth();
  const dayDiff = today.getDate() - birthDate.getDate();
  if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
    age -= 1;
  }
  return age;
}
```

## Nota final

El cambio principal es en el frontend: eliminar el campo visible y derivar `edad` desde `fecha_nacimiento`. La mejora recomendada es también validar/calcular la edad en el backend para mantener la integridad de los datos.

---


