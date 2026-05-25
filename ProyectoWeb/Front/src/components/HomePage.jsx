import Card from '../ui/Card';

export default function HomePage() {
  return (
    <section className="flow">
      <article className="card">
        <img
          className="card__media"
          src="https://picsum.photos/640/360"
          alt="Vista previa del artículo"
        />
        <div className="card__body">
          <h2 className="card__title">Bienvenido al frontend React</h2>
          <p className="card__text">
            Esta aplicación se ha migrado a React con Vite. Navega a la pestaña Formulario para
            ver la interfaz de datos dinámicos.
          </p>
          <div className="card__meta">
            <span className="badge">React + Vite</span>
            <time dateTime="2026-04-28">28 Abr 2026</time>
          </div>
        </div>
      </article>
    </section>
  );
}
