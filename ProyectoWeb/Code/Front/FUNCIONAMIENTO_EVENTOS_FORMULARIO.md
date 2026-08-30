# Funcionamiento de eventos del componente FormPersona

Este documento describe cómo se gestionan los eventos del formulario principal de la aplicación, basado en el componente `src/components/FormPersona.jsx` y el manejo de estado en `src/App.jsx`.

## Componentes implicados

- `src/components/FormPersona.jsx`: renderiza el formulario y recibe las funciones de evento como props.
- `src/ui/Input.jsx`: renderiza los campos de texto y delega `onChange`.
- `src/ui/Select.jsx`: renderiza el campo de selección y también delega `onChange`.
- `src/App.jsx`: define los controladores reales de los eventos y mantiene el estado del formulario.
- `src/utils/validation.js`: valida los valores antes de enviar.

## Props clave en `FormPersona`

- `formValues`: objeto con el estado actual de los campos del formulario.
- `onChange`: función que se ejecuta cuando cambia un campo del formulario.
- `onSubmit`: función que se ejecuta al enviar el formulario.
- `onClear`: función que se ejecuta al pulsar el botón "Limpiar".
- `status`: mensaje de estado que se muestra en pantalla.
- `isEditing`: indicador para alternar el texto del botón entre "Guardar" y "Actualizar".

## Eventos principales

### 1. `onChange` en los campos del formulario

- Los campos del formulario (`Input` y `Select`) usan la propiedad `onChange={onChange}`.
- Cuando el usuario escribe o selecciona un valor, `handleChange` en `src/App.jsx` se ejecuta.
- `handleChange` toma `event.target.name` y `event.target.value` y actualiza el estado:
  - `setFormValues((current) => ({ ...current, [name]: value }))`
- Esto convierte los campos en componentes controlados: React siempre usa `formValues[...]` como valor.

### 2. `onSubmit` en el formulario

- `FormPersona` aplica `onSubmit={onSubmit}` en el elemento `<form>`.
- En `App.jsx`, `handleSubmit` hace lo siguiente:
  1. Llama a `event.preventDefault()` para evitar la recarga de la página.
  2. Valida `formValues` con `validateForm(formValues)`.
  3. Si la validación falla, actualiza `status` con el mensaje de error y detiene el envío.
  4. Si está en modo edición (`editingIndex !== null`), hace un `PUT` a la API para actualizar el registro.
  5. Si no está en modo edición, hace un `POST` para crear un nuevo registro.
  6. Actualiza `records` con la respuesta o el nuevo registro local.
  7. Actualiza el mensaje `status` según el resultado.
  8. Si se guarda correctamente, reinicia `formValues` usando `initialForm`.

### 3. `onClick` del botón Limpiar

- El botón secundario en `FormPersona` usa `type="button"` y `onClick={onClear}`.
- `handleClear` en `App.jsx` hace:
  - `setFormValues(initialForm)` para resetear todos los campos.
  - `setEditingIndex(null)` para salir del modo edición.
  - `setStatus('Formulario limpiado.')` para mostrar un mensaje al usuario.

## Flujo de eventos completo

1. El usuario navega a la página de formulario.
2. El formulario se renderiza con valores de `formValues` desde `App.jsx`.
3. Al escribir en un campo o cambiar la selección:
   - `Input`/`Select` disparan `onChange`.
   - `handleChange` actualiza el estado local del formulario.
4. Al pulsar el botón "Guardar" o "Actualizar":
   - El formulario dispara `onSubmit`.
   - `handleSubmit` valida y persiste los datos en el backend.
   - El estado de la aplicación se actualiza según éxito o error.
5. Al pulsar "Limpiar":
   - Se reinician los campos y el mensaje de estado.

## Modo edición

- Si el usuario selecciona un registro para editar (`handleEdit` en `RecordsList`), `App.jsx` hace:
  - `setFormValues(records[index])`
  - `setEditingIndex(index)`
  - `setStatus('Edita el registro y guarda los cambios.')`
  - `setPage('form')`
- Entonces, el formulario se carga con los valores del registro seleccionado y el botón se muestra como "Actualizar".

## Mensajes de estado

- `FormPersona` incluye el componente `StatusMessage` con `message={status}`.
- Esto permite mostrar retroalimentación de validación, guardado exitoso, actualización o limpieza.

## Consideraciones adicionales

- El formulario usa campos controlados, por lo que cualquier cambio queda sincronizado con el estado de React.
- `event.preventDefault()` en `handleSubmit` es crítico para evitar recargas indeseadas.
- Las operaciones de la API (`POST`/`PUT`) se manejan en `App.jsx`, no dentro de `FormPersona`.
- El componente `FormPersona` es presentacional: no contiene lógica de negocio, solo delega eventos hacia `App.jsx`.
