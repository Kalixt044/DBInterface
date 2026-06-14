        async function apiCall(endpoint, method = 'GET', data = null) {
            const url = `${API_BASE}/${endpoint}`;
            showStatus('loading', '⏳ Conectando...');
            
            try {
                const options = { headers: HEADERS };
                if (data) options.body = JSON.stringify(data);
                if (method !== 'GET') options.method = method;
                
                const response = await fetch(url, options);
                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.detail || error.error || `HTTP ${response.status}`);
                }
                return await response.json();
            } catch (error) {
                showStatus('error', `❌ Error: ${error.message}`);
                throw error;
            }
        }
        
        //  CARGAR ESTRUCTURA TABLA (campos dinámicos)
        async function loadTableStructure() {
            try {
                const data = await apiCall(`table/${TABLE_NAME}/structure`);
                tableStructure = data.fields;
                console.log('✅ Estructura cargada:', tableStructure.map(f => f.name));
            } catch (error) {
                console.error('Error estructura:', error);
            }
        }
        
        //  GUARDAR/EDITAR
        document.getElementById('dynamicForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = Object.fromEntries(new FormData(e.target));
            
            // Checkbox handling
            const activo = document.querySelector('input[name="activo"]')?.checked || true;
            formData.activo = activo;
            
            try {
                if (editingId) {
                    // Editar
                    await apiCall(`table/${TABLE_NAME}/${editingId}`, 'PUT', formData);
                    showStatus('success', '✅ Registro actualizado');
                } else {
                    // Nuevo
                    const result = await apiCall(`table/${TABLE_NAME}/insert`, 'POST', formData);
                    showStatus('success', `✅ Creado con ID: ${result.id}`);
                }
                document.getElementById('dynamicForm').reset();
                editingId = null;
                document.getElementById('btnGuardar').textContent = '💾 Guardar';
                loadRecords();
            } catch (error) {
                console.error('Error guardar:', error);
            }
        });
        
        // 📋 LISTAR REGISTROS
        async function loadRecords(page = 1) {
            try {
                currentPage = page;
                const data = await apiCall(`table/${TABLE_NAME}?page=${page}&limit=10`);
                totalRecords = data.total;
                renderRecords(data.records);
                updatePagination();
                document.getElementById('records').style.display = 'block';
            } catch (error) {
                console.error('Error listar:', error);
            }
        }
        
        function renderRecords(records) {
            const container = document.getElementById('recordsList');
            container.innerHTML = records.map(record => `
                <div class="record-card">
                    <h4>${record.primer_nombres} ${record.primer_apellido}</h4>
                    <p><strong>Doc:</strong> ${record.documento} ${record.numero_identificacion}</p>
                    <p><strong>Email:</strong> ${record.email || 'N/A'}</p>
                    <p><strong>Tel:</strong> ${record.numero_celular || 'N/A'}</p>
                    <p><strong>Dirección:</strong> ${record.direccion}, ${record.barrio}</p>
                    <div style="margin-top: 10px;">
                        <button class="btn" onclick="editRecord(${record.id})">✏️ Editar</button>
                        <button class="btn btn-danger" onclick="deleteRecord(${record.id})">🗑️ Eliminar</button>
                    </div>
                </div>
            `).join('');
        }
        
        //  EDITAR
        async function editRecord(id) {
            try {
                const record = await apiCall(`table/${TABLE_NAME}/${id}`);
                editingId = id;
                document.getElementById('btnGuardar').textContent = '💾 Actualizar';
                
                // Llenar formulario
                Object.keys(record).forEach(key => {
                    const input = document.querySelector(`[name="${key}"]`);
                    if (input) {
                        if (input.type === 'checkbox') {
                            input.checked = record[key];
                        } else {
                            input.value = record[key] || '';
                        }
                    }
                });
                
                showStatus('success', '✏️ Cargado para editar');
                document.getElementById('dynamicForm').scrollIntoView();
            } catch (error) {
                console.error('Error editar:', error);
            }
        }
        
        //  ELIMINAR
        async function deleteRecord(id) {
            if (!confirm('¿Eliminar este registro?')) return;
            
            try {
                await apiCall(`table/${TABLE_NAME}/${id}`, 'DELETE');
                showStatus('success', '🗑️ Eliminado correctamente');
                loadRecords(currentPage);
            } catch (error) {
                console.error('Error eliminar:', error);
            }
        }



# DBInterface API

**Descripción:** Colección de pruebas CRUD para el backend FastAPI de ProyectoWeb.

**Variables de entorno:**
- `base_url`: `http://localhost:8000/api`
- `personas_id`: (se asigna dinámicamente)

---

## 1 - Listar tablas

**Método:** `GET`  
**URL:** `http://localhost:8000/tables`  
**Headers:**  
- `Accept: application/json`

---

## 2 - Obtener estructura de personas

**Método:** `GET`  
**URL:** `http://localhost:8000/table/personas/structure`  
**Headers:**  
- `Accept: application/json`

---

## 3 - Listar primeras 5 personas

**Método:** `GET`  
**URL:** `http://localhost:8000/table/personas?page=1&limit=5`  
**Headers:**  
- `Accept: application/json`

---

## 4 - Insertar persona

**Método:** `POST`  
**URL:** `http://localhost:8000/table/personas/insert`  
**Headers:**  
- `Content-Type: application/json`  
- `Accept: application/json`  

**Body (JSON):**
```json
{
  "primer_nombres": "Luis Alberto",
  "segundo_nombre": "Daniel",
  "primer_apellido": "Torres",
  "segundo_apellido": "García",
  "documento": "CC",
  "numero_identificacion": "1122334455",
  "domicilio": "Calle Nueva 123",
  "fecha_nacimiento": "1985-07-10",
  "sexo": "M",
  "numero_celular": "+573001112233",
  "direccion": "Av. Libertador 456",
  "barrio": "Norte",
  "email": "luis.torres@example.com"
}

## 5 - elimina 
**Delete**

http://localhost:8000/api/table/personas/13