
# Ejercicio 1
def calcular_area(base: float, altura: float) -> float:
    area = base * altura
    print(f"El área es: {area}")
    return area

# Ejercicio 2
try:
    conectar()
except ConnectionError as e:
    logging.error(f"Error de conexión: {e}")

# Ejercicio 3
def saludar(usuario: str) -> None:
    print(f'User {usuario}')
    print('---')

saludar('A')
saludar('B')

# Ejercicio 4 
def suma(a: int, b: int) -> int:
    return a + b

# Ejercicio 5
class MiClase:
    def __init__(self, n: int) -> None:
        self.n = n

# Ejercicio 6
x = 10 + 5 * 2 / (1 + 1)

# Ejercicio 7 
def dia_semana(dia: int) -> str:
    dias = {
        1: 'L',
        2: 'M',
        3: 'X',
        4: 'J',
        5: 'V',
        6: 'S',
        7: 'D'
    }
    return dias.get(dia, 'Día inválido')

# Ejercicio 8
def log_si_autorizado(user: bool, passw: bool, admin: bool) -> None:
    if not user or not passw or not admin:
        return
    log()

# Ejercicio 9
def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

# Ejercicio 10 
API_KEY = os.getenv('API_KEY', 'default_value')

# Ejercicio 11
DB_HOST=localhost
DB_PORT=5432

# Código
import os

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Ejercicio 12 
import os

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'