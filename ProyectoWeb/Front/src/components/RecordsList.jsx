import Button from '../ui/Button';

export default function RecordsList({ records, onEdit }) {
  return (
    <div className="records-panel">
      <h2>Registros guardados</h2>
      {records.length === 0 ? (
        <p>No hay registros aún.</p>
      ) : (
        <div className="records-list">
          {records.map((record, index) => (
            <div key={index} className="record-card">
              <strong>
                {record.primer_nombres} {record.primer_apellido}
              </strong>
              <span>
                {record.documento} - {record.numero_identificacion}
              </span>
              <Button onClick={() => onEdit(index)} className="btn btn--ghost">
                Editar
              </Button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
