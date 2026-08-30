# Mejoras a aplicar en el Frontend

## Críticas

- [ ] **Navbar invisible en mobile** — `Header.jsx` no renderiza el botón hamburguesa; CSS oculta `nav__menu` en <768px sin forma de abrirlo.
- [ ] **Sin carga inicial de datos** — `App.jsx` nunca trae registros existentes del backend al montar.
- [ ] **Sin funcionalidad de eliminar** — No hay botón ni lógica para borrar registros.
- [ ] **`!important` en index.css (líneas 177-187)** — Rompe la cascada del design system; forzar colores con `!important` indica conflicto entre CSS.
- [ ] **Sin Error Boundary** — Cualquier error de renderizado tira toda la app.
- [ ] **Campos requeridos sin atributo `required`** — `FormPersona.jsx` marca 5 campos como requeridos en validación JS pero `Input.jsx` / `Select.jsx` nunca reciben `required=true`.

## Altas

- [ ] **Falta estados de carga/error** — `RecordsList.jsx` no tiene loading ni error state; formulario sin spinner en submit.
- [ ] **StatusMessage inaccesible** — Sin `role="alert"` ni `aria-live`.
- [ ] **Sin paginación** — La lista muestra todos los registros de una vez.
- [ ] **`key={index}` en RecordsList (línea 12)** — Usar `record.id` en su lugar.
- [ ] **`form.html` obsoleto** — Archivo legacy con lógica duplicada; eliminar o archivar.
- [ ] **CSS duplicados** — `styles.css`, `form.css`, `index.css` se pisan entre sí; unificar design system.

## Medias

- [ ] **Sin PropTypes / validación de props** — Ningún componente valida sus props.
- [ ] **`API_BASE` hardcodeada** — Usar `import.meta.env.VITE_API_BASE`.
- [ ] **Footer con año hardcodeado 2026** — Usar `new Date().getFullYear()`.
- [ ] **`useMemo` innecesario** — `pageTitle` en `App.jsx` (líneas 73-75) es cómputo trivial.
- [ ] **Sin React Router** — Navegación manual con `useState` impide deep linking y browser history.
- [ ] **Botón "Modo oscuro" no funcional** — No tiene `onClick` ni estado.
- [ ] **Links del footer con `href="#"`** — Sin navegación real.
- [ ] **`Card.jsx` sin usar** — `HomePage.jsx` construye su propio card manualmente.

## Bajas

- [ ] **Sin sanitización de inputs** — `validation.js` no escapa ni valida formatos.
- [ ] **Sin favicon ni meta description** — `index.html` incompleto.
- [ ] **`console.error` en producción** — `App.jsx` línea 52.
- [ ] **URL de imagen hardcodeada** — `picsum.photos` en `HomePage.jsx`.
- [ ] **Estilos sin responsividad fina** — Formularios, record cards y touch targets mejorables.
- [ ] **Sin tests** — A pesar de documentarse como "testeable".
- [ ] **Sin TypeScript** — Todos los archivos son `.jsx` sin tipos.
- [ ] **Sin ESLint / Prettier** — Sin herramientas de formato estático.
- [ ] **Sin carga diferida (lazy loading)** — `React.lazy` + `Suspense` no utilizado.

