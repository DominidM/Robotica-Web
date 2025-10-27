#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn --bind=0.0.0.0 --timeout 600 webapp.wsgi
```

*(Asegúrate de que sea `webapp.wsgi` porque tu `WSGI_APPLICATION = 'webapp.wsgi.application'`)*

---

## **Próximo paso: Configurar Azure**

Una vez que hagas push a GitHub, necesitarás configurar en Azure:

### **Variables de entorno en Azure App Service:**

1. Ve a tu App Service en Azure Portal
2. **Configuration** → **Application settings** → **New application setting**
3. Agrega estas variables:
```
SCM_DO_BUILD_DURING_DEPLOYMENT = true
DEBUG = False
SECRET_KEY = [genera-una-clave-segura-aquí]
DB_NAME = dimsor
DB_USER = [tu-usuario-mysql-azure]
DB_PASSWORD = [tu-contraseña-mysql-azure]
DB_HOST = [tu-servidor-mysql-azure.mysql.database.azure.com]
```

### **Configurar el comando de inicio:**

En Azure Portal → **Configuration** → **General settings** → **Startup Command**:
```
startup.sh