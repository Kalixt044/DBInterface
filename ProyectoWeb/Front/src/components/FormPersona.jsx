import Button from '../ui/Button';
import Input from '../ui/Input';
import Select from '../ui/Select';
import StatusMessage from '../ui/StatusMessage';
import { campoLabels } from '../constants/formConfig';

export default function FormPersona({
  formValues,
  onChange,
  onSubmit,
  onClear,
  status,
  isEditing
}) {
  return (
    <section className="form-section">
      <StatusMessage message={status} />
      <form className="form-grid" onSubmit={onSubmit}>
        {campoLabels.map((field) => (
          <div key={field.name}>
            {field.type === 'select' ? (
              <Select
                id={field.name}
                name={field.name}
                label={field.label}
                value={formValues[field.name]}
                options={field.options}
                onChange={onChange}
              />
            ) : (
              <Input
                id={field.name}
                name={field.name}
                label={field.label}
                type={field.type}
                value={formValues[field.name]}
                onChange={onChange}
              />
            )}
          </div>
        ))}

        <div className="form-actions">
          <Button type="submit" className="btn btn--primary">
            {isEditing ? 'Actualizar' : 'Guardar'}
          </Button>
          <Button type="button" onClick={onClear} className="btn btn--secondary">
            Limpiar
          </Button>
        </div>
      </form>
    </section>
  );
}
