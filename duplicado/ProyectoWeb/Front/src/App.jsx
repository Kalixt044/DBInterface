import { useMemo, useState } from 'react';

const initialForm = {
  primer_nombres: '',
  segundo_nombre: '',
  primer_apellido: '',
  segundo_apellido: '',
  documento: '',
  numero_identificacion: '',
  domicilio: '',
  fecha_nacimiento: '',
  edad: '',
  sexo: '',
  numero_celular: '',
  direccion: '',
  barrio: '',
  email: ''
};

const campoLabels = [
  { name: 'primer_nombres', label: 'Primer Nombres *' },
  { name: 'segundo_nombre', label: 'Segundo Nombre' },
  { name: 'primer_apellido', label: 'Primer Apellido *' },
  { name: 'segundo_apellido', label: 'Segundo Apellido' },
  { name: 'documento', label: 'Documento *', type: 'select', options: ['CC', 'TI', 'CE', 'PA'] },
  { name: 'numero_identificacion', label: 'Número Identificación *' },
  { name: 'domicilio', label: 'Domicilio' },
  { name: 'fecha_nacimiento', label: 'Fecha Nacimiento', type: 'date' },
  { name: 'edad', label: 'Edad', type: 'number' },
  { name: 'sexo', label: 'Sexo', type: 'select', options: ['M', 'F', 'O'] },
  { name: 'numero_celular', label: 'Número Celular' },
  { name: 'direccion', label: 'Dirección *' },
  { name: 'barrio', label: 'Barrio' },
  { name: 'email', label: 'Email', type: 'email' }
];

const API_BASE = 'http://localhost:8000/api';
const TABLE_NAME = 'personas';
const HEADERS = { 'Content-Type': 'application/json', 'Accept': 'application/json' };

async function apiCall(endpoint, method = 'GET', data = null) {
  const url = `${API_BASE}/${endpoint}`;
  const options = { method, headers: HEADERS };
  if (data) options.body = JSON.stringify(data);

  const response = await fetch(url, options);
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || error.message || `HTTP ${response.status}`);
  }
  return response.json();
}

function App() {
  const [page, setPage] = useState('home');
  const [formValues, setFormValues] = useState(initialForm);
  const [records, setRecords] = useState([]);
  const [status, setStatus] = useState('');
  const [editingIndex, setEditingIndex] = useState(null);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormValues((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!formValues.primer_nombres || !formValues.primer_apellido || !formValues.documento || !formValues.numero_identificacion || !formValues.direccion) {
      setStatus('Por favor completa los campos obligatorios.');
      return;
    }

    try {
      if (editingIndex !== null && records[editingIndex]?.id) {
        const recordToUpdate = records[editingIndex];
        await apiCall(`table/${TABLE_NAME}/${recordToUpdate.id}`, 'PUT', formValues);
        setRecords((current) => current.map((record, index) => index === editingIndex ? { ...record, ...formValues } : record));
        setStatus('Registro actualizado en backend.');
        setEditingIndex(null);
      } else {
        const result = await apiCall(`table/${TABLE_NAME}/insert`, 'POST', formValues);
        setRecords((current) => [...current, { ...formValues, id: result.id ?? Date.now() }]);
        setStatus('Registro guardado en backend.');
      }
    } catch (error) {
      console.error('Error guardando en backend:', error);
      setStatus(`No se pudo guardar: ${error.message}`);
      return;
    }

    setFormValues(initialForm);
  };

  const handleEdit = (index) => {
    setFormValues(records[index]);
    setEditingIndex(index);
    setStatus('Edita el registro y guarda los cambios.');
    setPage('form');
  };

  const handleClear = () => {
    setFormValues(initialForm);
    setEditingIndex(null);
    setStatus('Formulario limpiado.');
  };

  const pageTitle = useMemo(() => {
    return page === 'home' ? 'Inicio' : 'Formulario';
  }, [page]);

  return (
    <div className="app-shell">
      <header className="nav app-nav">
        <div className="container nav__inner">
          <button className="nav__brand" onClick={() => setPage('home')}>
            CENSO RURAL React
          </button>
          <nav className="nav__menu" aria-label="Navegación principal">
            <button className={page === 'home' ? 'nav__link is-active' : 'nav__link'} onClick={() => setPage('home')}>
              Inicio
            </button>
            <button className={page === 'form' ? 'nav__link is-active' : 'nav__link'} onClick={() => setPage('form')}>
              Formulario
            </button>
          </nav>
        </div>
      </header>

      <main className="container flow page-content">
        <h1>{pageTitle}</h1>

        {page === 'home' ? (
          <section className="flow">
            <article className="card">
              <img className="card__media" src="https://picsum.photos/640/360" alt="Vista previa del artículo" />
              <div className="card__body">
                <h2 className="card__title">Bienvenido al frontend React</h2>
                <p className="card__text">
                  Esta aplicación se ha migrado a React con Vite. Navega a la pestaña Formulario para ver la interfaz de datos dinámicos.
                </p>
                <div className="card__meta">
                  <span className="badge">React + Vite</span>
                  <time dateTime="2026-04-28">28 Abr 2026</time>
                </div>
              </div>
            </article>
          </section>
        ) : (
          <section className="form-section">
            {status && <div className="status-message">{status}</div>}
            <form className="form-grid" onSubmit={handleSubmit}>
              {campoLabels.map((field) => (
                <div key={field.name}>
                  <label htmlFor={field.name}>{field.label}</label>
                  {field.type === 'select' ? (
                    <select id={field.name} name={field.name} value={formValues[field.name]} onChange={handleChange}>
                      <option value="">Seleccionar...</option>
                      {field.options.map((option) => (
                        <option key={option} value={option}>{option}</option>
                      ))}
                    </select>
                  ) : (
                    <input
                      id={field.name}
                      name={field.name}
                      type={field.type ?? 'text'}
                      value={formValues[field.name]}
                      onChange={handleChange}
                    />
                  )}
                </div>
              ))}

              <div className="form-actions">
                <button type="submit" className="btn btn--primary">{editingIndex !== null ? 'Actualizar' : 'Guardar'}</button>
                <button type="button" className="btn btn--secondary" onClick={handleClear}>Limpiar</button>
              </div>
            </form>

            <div className="records-panel">
              <h2>Registros guardados</h2>
              {records.length === 0 ? (
                <p>No hay registros aún.</p>
              ) : (
                <div className="records-list">
                  {records.map((record, index) => (
                    <div key={index} className="record-card">
                      <strong>{record.primer_nombres} {record.primer_apellido}</strong>
                      <span>{record.documento} - {record.numero_identificacion}</span>
                      <button className="btn btn--ghost" onClick={() => handleEdit(index)}>Editar</button>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </section>
        )}
      </main>

      <footer className="footer" role="contentinfo">
        <div className="container footer__grid">
          <section className="footer__col">
            <h2 className="footer__title">CENSO RURAL</h2>
            <p className="footer__text">Construyendo experiencias web accesibles y robustas.</p>
          </section>
          <nav className="footer__col" aria-labelledby="footer-nav-1">
            <h2 id="footer-nav-1" className="footer__title">Recursos</h2>
            <ul className="footer__links">
              <li><a href="#">Guías</a></li>
              <li><a href="#">Blog</a></li>
              <li><a href="#">Ayuda</a></li>
            </ul>
          </nav>
          <nav className="footer__col" aria-labelledby="footer-nav-2">
            <h2 id="footer-nav-2" className="footer__title">Legal</h2>
            <ul className="footer__links">
              <li><a href="#">Privacidad</a></li>
              <li><a href="#">Términos</a></li>
              <li><a href="#">Cookies</a></li>
            </ul>
          </nav>
          <section className="footer__col">
            <h2 className="footer__title">Suscríbete</h2>
            <form className="footer__form" action="#" method="post" onSubmit={(e) => e.preventDefault()}>
              <label className="sr-only" htmlFor="footer-email">Correo electrónico</label>
              <input id="footer-email" name="footer-email" type="email" placeholder="tu@correo.com" />
              <button className="btn btn--primary" type="button">Enviar</button>
            </form>
          </section>
        </div>
        <div className="footer__bar">
          <div className="container footer__bar-inner">
            <small>© 2026 CENSO RURAL. Todos los derechos reservados.</small>
            <button className="btn btn--ghost" type="button">Modo oscuro</button>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
