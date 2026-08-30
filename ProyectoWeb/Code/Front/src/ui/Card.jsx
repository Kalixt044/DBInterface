export default function Card({ title, text, imageUrl, meta }) {
  return (
    <article className="card">
      {imageUrl && <img className="card__media" src={imageUrl} alt="Vista previa del artículo" />}
      <div className="card__body">
        <h2 className="card__title">{title}</h2>
        <p className="card__text">{text}</p>
        {meta && (
          <div className="card__meta">
            {meta.badges && meta.badges.map((badge) => (
              <span key={badge} className="badge">
                {badge}
              </span>
            ))}
            {meta.date && <time dateTime={meta.date}>{meta.date}</time>}
          </div>
        )}
      </div>
    </article>
  );
}
