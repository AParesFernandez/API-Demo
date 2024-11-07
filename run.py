from app_flask import create_app

# Crea la aplicación Flask
app = create_app()

# Verifica si este archivo está siendo ejecutado directamente por Python
if __name__ == "__main__":
    # Ejecuta la aplicación en modo de desarrollo
    app.run(debug=True)
