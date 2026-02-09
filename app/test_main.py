from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    # Simula una petición GET a la raíz "/"
    response = client.get("/")
    
    # Verifica que el servidor responde con éxito (200)
    assert response.status_code == 200
    
    # Verifica que el mensaje es el esperado
    # OJO: Esto debe coincidir con lo que pusiste en main.py
    assert response.json() == {"mensaje": "Hola Mundo"}