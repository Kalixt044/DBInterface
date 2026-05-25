import { requiredFields } from '../constants/formConfig';

export function validateForm(formValues) {
  const missingFields = requiredFields.filter(field => !formValues[field]);
  
  if (missingFields.length > 0) {
    return {
      isValid: false,
      message: 'Por favor completa los campos obligatorios.'
    };
  }

  return {
    isValid: true,
    message: ''
  };
}
