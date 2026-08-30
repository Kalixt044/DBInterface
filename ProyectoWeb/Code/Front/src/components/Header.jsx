import Button from '../ui/Button';

export default function Header({ currentPage, onPageChange }) {
  return (
    <header className="nav app-nav">
      <div className="container nav__inner">
        <button className="nav__brand" onClick={() => onPageChange('home')}>
          CENSO RURAL React
        </button>
        <nav className="nav__menu" aria-label="Navegación principal">
          <button
            className={currentPage === 'home' ? 'nav__link is-active' : 'nav__link'}
            onClick={() => onPageChange('home')}
          >
            Inicio
          </button>
          <button
            className={currentPage === 'form' ? 'nav__link is-active' : 'nav__link'}
            onClick={() => onPageChange('form')}
          >
            Formulario
          </button>
        </nav>
      </div>
    </header>
  );
}
