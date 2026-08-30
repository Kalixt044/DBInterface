import { useMemo, useState } from 'react';
import Header from './components/Header';
import HomePage from './components/HomePage';
import FormPersona from './components/FormPersona';
import RecordsList from './components/RecordsList';
import { initialForm } from './constants/formConfig';
import { TABLE_NAME } from './constants/apiConfig';
import { apiCall } from './utils/api';
import { validateForm } from './utils/validation';

const computeAge = (fechaNacimiento) => {
  if (!fechaNacimiento) return null;
  const birthDate = new Date(fechaNacimiento);
  if (Number.isNaN(birthDate.getTime())) return null;

  const today = new Date();
  let age = today.getFullYear() - birthDate.getFullYear();
  const monthDiff = today.getMonth() - birthDate.getMonth();
  const dayDiff = today.getDate() - birthDate.getDate();

  if (monthDiff < 0 || (monthDiff === 0 && dayDiff < 0)) {
    age -= 1;
  }

  return age >= 0 ? age : null;
};

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

    const submissionData = {
      ...formValues,
      edad: computeAge(formValues.fecha_nacimiento)
    };

    const validation = validateForm(formValues);
    if (!validation.isValid) {
      setStatus(validation.message);
      return;
    }

    try {
      if (editingIndex !== null && records[editingIndex]?.id) {
        const recordToUpdate = records[editingIndex];
        await apiCall(`table/${TABLE_NAME}/${recordToUpdate.id}`, 'PUT', submissionData);
        setRecords((current) =>
          current.map((record, index) =>
            index === editingIndex ? { ...record, ...submissionData } : record
          )
        );
        setStatus('Registro actualizado en backend.');
        setEditingIndex(null);
      } else {
        const result = await apiCall(`table/${TABLE_NAME}/insert`, 'POST', submissionData);
        setRecords((current) => [
          ...current,
          { ...submissionData, id: result.id ?? Date.now() }
        ]);
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
      <Header currentPage={page} onPageChange={setPage} />

      <main className="container flow page-content">
        <h1>{pageTitle}</h1>

        {page === 'home' ? (
          <HomePage />
        ) : (
          <>
            <FormPersona
              formValues={formValues}
              onChange={handleChange}
              onSubmit={handleSubmit}
              onClear={handleClear}
              status={status}
              isEditing={editingIndex !== null}
            />
            <RecordsList records={records} onEdit={handleEdit} />
          </>
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
