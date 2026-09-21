import ast
from pathlib import Path


def _load_calcular_edad():
    file_path = Path(__file__).resolve().parents[1] / 'DesktopProyect' / 'index.py'
    source = file_path.read_text(encoding='utf-8')
    module = ast.parse(source)
    namespace = {'datetime': __import__('datetime').datetime, 'date': __import__('datetime').date, 'tk': __import__('tkinter')}

    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name == 'calcular_edad':
            exec(compile(ast.Module(body=[node], type_ignores=[]), str(file_path), 'exec'), namespace)
            return namespace['calcular_edad']

    raise AssertionError('No se encontró la función calcular_edad en DesktopProyect/index.py')


def test_calcular_edad_valida_para_una_fecha_en_2024():
    calcular_edad = _load_calcular_edad()
    assert calcular_edad('15/05/1990') == 34
    assert calcular_edad('27/11/2024') == 0
    assert calcular_edad('31/12/2025') is None


def test_calcular_edad_rechaza_fecha_invalida():
    calcular_edad = _load_calcular_edad()
    assert calcular_edad('fecha-mala') is None
