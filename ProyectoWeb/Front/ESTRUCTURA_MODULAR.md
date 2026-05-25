# Estructura Modular del Proyecto

## Descripción General
El proyecto ha sido refactorizado aplicando el concepto de **modularidad**, separando la lógica en directorios específicos con responsabilidades claras.

## Estructura de Directorios

### `/src/components/` - Componentes con Lógica
Componentes que encapsulan lógica de negocio y estado de la aplicación.

- **Header.jsx** - Componente de navegación principal
  - Gestiona la navegación entre páginas
  - Props: `currentPage`, `onPageChange`

- **HomePage.jsx** - Página de inicio
  - Muestra información de bienvenida
  - Completamente reutilizable

- **FormPersona.jsx** - Componente del formulario de datos
  - Gestiona el formulario de registro
  - Props: `formValues`, `onChange`, `onSubmit`, `onClear`, `status`, `isEditing`

- **RecordsList.jsx** - Componente de lista de registros
  - Muestra los registros guardados
  - Props: `records`, `onEdit`

### `/src/ui/` - Elementos UI (sin lógica)
Componentes visuales reutilizables sin lógica de negocio.

- **Button.jsx** - Botón genérico
- **Input.jsx** - Campo de entrada genérico
- **Select.jsx** - Dropdown genérico
- **StatusMessage.jsx** - Mensaje de estado
- **Card.jsx** - Tarjeta de contenido

### `/src/constants/` - Configuraciones
Valores constantes del proyecto.

- **formConfig.js** - Configuración del formulario
  - `initialForm` - Estado inicial del formulario
  - `campoLabels` - Definición de campos
  - `requiredFields` - Lista de campos obligatorios

- **apiConfig.js** - Configuración de API
  - `API_BASE` - URL base del API
  - `TABLE_NAME` - Tabla de base de datos
  - `HEADERS` - Headers por defecto

### `/src/utils/` - Funciones Utilidad
Funciones auxiliares reutilizables.

- **api.js** - Funciones de llamadas API
  - `apiCall()` - Función genérica para hacer requests

- **validation.js** - Funciones de validación
  - `validateForm()` - Valida los campos obligatorios

## Diferencia entre Elementos y Componentes

### Componentes (`/src/components/`)
- **Con lógica de negocio** y estado
- Pueden usar hooks (useState, useEffect, etc.)
- Conectados a la lógica de la aplicación
- Ejemplos: FormPersona, RecordsList, Header

### Elementos UI (`/src/ui/`)
- **Sin lógica de negocio**
- Solo reciben props y renderizar
- Completamente reutilizables
- Ejemplos: Button, Input, Select, StatusMessage

## Beneficios de esta Estructura

✅ **Modularidad** - Cada archivo tiene una responsabilidad única
✅ **Reutilización** - Elementos UI pueden usarse en múltiples componentes
✅ **Mantenibilidad** - Cambios localizados y fáciles de encontrar
✅ **Testabilidad** - Componentes aislados son más fáciles de probar
✅ **Escalabilidad** - Fácil agregar nuevos componentes o elementos
✅ **Claridad** - Código más legible y organizado
