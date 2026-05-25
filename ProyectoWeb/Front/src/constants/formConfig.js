export const initialForm = {
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

export const campoLabels = [
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

export const requiredFields = [
  'primer_nombres',
  'primer_apellido',
  'documento',
  'numero_identificacion',
  'direccion'
];
