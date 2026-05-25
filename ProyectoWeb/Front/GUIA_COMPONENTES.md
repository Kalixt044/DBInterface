# Guía de Uso de Componentes

## Componentes (Con Lógica)

### Header
```jsx
import Header from './components/Header';

<Header 
  currentPage={page} 
  onPageChange={setPage} 
/>
```
**Responsabilidades:**
- Renderiza la navegación
- Gestiona cambios de página
- Muestra el estado actual de la navegación

---

### HomePage
```jsx
import HomePage from './components/HomePage';

<HomePage />
```
**Responsabilidades:**
- Muestra la página de inicio
- Renderiza tarjeta de bienvenida
- Completamente independiente

---

### FormPersona
```jsx
import FormPersona from './components/FormPersona';

<FormPersona
  formValues={formValues}
  onChange={handleChange}
  onSubmit={handleSubmit}
  onClear={handleClear}
  status={status}
  isEditing={editingIndex !== null}
/>
```
**Responsabilidades:**
- Renderiza el formulario
- Valida a través de components hijos
- Maneja cambios de campos
- Muestra mensajes de estado

---

### RecordsList
```jsx
import RecordsList from './components/RecordsList';

<RecordsList 
  records={records} 
  onEdit={handleEdit} 
/>
```
**Responsabilidades:**
- Muestra lista de registros
- Permite edición de registros
- Muestra mensaje cuando no hay registros

---

## Elementos UI (Sin Lógica)

### Button
```jsx
import Button from './ui/Button';

<Button 
  onClick={handleClick} 
  className="btn btn--primary"
>
  Guardar
</Button>
```
**Props:**
- `children` - Contenido del botón
- `onClick` - Manejador de click
- `type` - Tipo de botón (button, submit, reset)
- `className` - Clases CSS

---

### Input
```jsx
import Input from './ui/Input';

<Input
  id="email"
  name="email"
  label="Correo Electrónico"
  type="email"
  value={email}
  onChange={handleChange}
  required={true}
/>
```
**Props:**
- `id` - ID del input
- `name` - Nombre del input
- `label` - Etiqueta del campo
- `type` - Tipo de input
- `value` - Valor actual
- `onChange` - Manejador de cambio
- `required` - Es obligatorio

---

### Select
```jsx
import Select from './ui/Select';

<Select
  id="genero"
  name="genero"
  label="Género"
  value={genero}
  options={['M', 'F', 'O']}
  onChange={handleChange}
/>
```
**Props:**
- `id` - ID del select
- `name` - Nombre del select
- `label` - Etiqueta del campo
- `value` - Valor seleccionado
- `options` - Array de opciones
- `onChange` - Manejador de cambio
- `required` - Es obligatorio

---

### StatusMessage
```jsx
import StatusMessage from './ui/StatusMessage';

<StatusMessage message="Registro guardado exitosamente" />
```
**Props:**
- `message` - Texto del mensaje (null no renderiza nada)

---

### Card
```jsx
import Card from './ui/Card';

<Card
  title="Título de la tarjeta"
  text="Texto descriptivo"
  imageUrl="https://ejemplo.com/imagen.jpg"
  meta={{
    badges: ['React', 'Vite'],
    date: '2026-04-28'
  }}
/>
```
**Props:**
- `title` - Título de la tarjeta
- `text` - Texto descriptivo
- `imageUrl` - URL de la imagen
- `meta` - Objeto con `badges` (array) y `date` (string)

---

## Funciones Utilidad

### apiCall
```jsx
import { apiCall } from './utils/api';

// GET
const data = await apiCall('table/personas');

// POST
const result = await apiCall('table/personas/insert', 'POST', formData);

// PUT
await apiCall(`table/personas/${id}`, 'PUT', updateData);

// DELETE
await apiCall(`table/personas/${id}`, 'DELETE');
```

### validateForm
```jsx
import { validateForm } from './utils/validation';

const validation = validateForm(formValues);
if (!validation.isValid) {
  console.log(validation.message); // "Por favor completa los campos obligatorios."
}
```

---

## Constantes y Configuración

### formConfig
```jsx
import { 
  initialForm,
  campoLabels,
  requiredFields 
} from './constants/formConfig';

// initialForm: Estado inicial del formulario
// campoLabels: Definición de todos los campos
// requiredFields: Lista de campos obligatorios
```

### apiConfig
```jsx
import { 
  API_BASE,
  TABLE_NAME,
  HEADERS 
} from './constants/apiConfig';

// API_BASE: 'http://localhost:8000/api'
// TABLE_NAME: 'personas'
// HEADERS: Headers por defecto para requests
```

---

## Patrón de Uso en App.jsx

```jsx
import Header from './components/Header';
import HomePage from './components/HomePage';
import FormPersona from './components/FormPersona';
import RecordsList from './components/RecordsList';
import { initialForm } from './constants/formConfig';
import { validateForm } from './utils/validation';

function App() {
  // Estado
  const [page, setPage] = useState('home');
  const [formValues, setFormValues] = useState(initialForm);
  
  // Handlers
  const handleChange = (event) => { /* ... */ };
  const handleSubmit = (event) => { /* ... */ };
  
  // Render
  return (
    <div>
      <Header currentPage={page} onPageChange={setPage} />
      
      {page === 'home' ? (
        <HomePage />
      ) : (
        <>
          <FormPersona 
            formValues={formValues}
            onChange={handleChange}
            onSubmit={handleSubmit}
          />
          <RecordsList records={records} />
        </>
      )}
    </div>
  );
}
```
