import { API_BASE, HEADERS } from '../constants/apiConfig';

export async function apiCall(endpoint, method = 'GET', data = null) {
  const url = `${API_BASE}/${endpoint}`;
  const options = { method, headers: HEADERS };
  if (data) options.body = JSON.stringify(data);

  const response = await fetch(url, options);
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || error.message || `HTTP ${response.status}`);
  }
  return response.json();
}
