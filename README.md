# Robotica-Web

Este proyecto es una aplicación web desarrollada con Django enfocada en la gestión y visualización de robots y sus funcionalidades. Está preparado para desplegarse localmente o en la nube, y cuenta con una estructura modular para facilitar el desarrollo y escalabilidad.

## Características

- Backend en Django (Python)
- Estructura de templates para vistas públicas y de administración
- Configuración lista para desarrollo local y despliegue en servicios cloud (Azure, Render, etc.)
- Soporte para migración de base de datos (SQLite para desarrollo, MySQL recomendado para producción)
- Estilos modernos y personalizables

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/DominidM/Robotica-Web.git
   cd Robotica-Web
   ```

2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno si es necesario (`.env` o en `settings.py`).

4. Aplica migraciones y ejecuta el servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Accede a [http://localhost:8000](http://localhost:8000)

## Estructura de Carpetas

```
core/
  ├── templates/
  │    ├── public/
  │    │     └── home.html
  │    └── admin/
  │          └── dashboard.html
  ├── static/
  └── views.py
webapp/
manage.py
requirements.txt
```

## Despliegue

- Puedes desplegar en Azure App Service, Render, Railway, etc.
- Recuerda cambiar la configuración de base de datos a MySQL o PostgreSQL en producción.
- Para archivos estáticos en producción, usa servicios como Azure Blob Storage o AWS S3.

## Personalización

- El home (`home.html`) es fácilmente editable, puedes mejorarlo con tu propio diseño o basarte en tu prototipo de Figma.

## Repositorios relacionados

- [Robotica](https://github.com/DominidM/Robotica)
- [Robotica-Mobile](https://github.com/DominidM/Robotica-Mobile)


## Licencia

MIT
