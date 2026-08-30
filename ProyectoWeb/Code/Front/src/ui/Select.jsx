export default function Select({ id, name, label, value, options, onChange, required = false }) {
  return (
    <div>
      <label htmlFor={id || name}>{label}</label>
      <select
        id={id || name}
        name={name}
        value={value}
        onChange={onChange}
        required={required}
      >
        <option value="">Seleccionar...</option>
        {options.map((option) => (
          <option key={option} value={option}>
            {option}
          </option>
        ))}
      </select>
    </div>
  );
}
