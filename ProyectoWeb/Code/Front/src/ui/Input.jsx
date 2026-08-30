export default function Input({ id, name, label, type = 'text', value, onChange, required = false }) {
  return (
    <div>
      <label htmlFor={id || name}>{label}</label>
      <input
        id={id || name}
        name={name}
        type={type}
        value={value}
        onChange={onChange}
        required={required}
      />
    </div>
  );
}
