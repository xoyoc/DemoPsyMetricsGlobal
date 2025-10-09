# PsyMetrics Global - Django Application

Aplicación web Django para evaluaciones psicométricas online con Tailwind CSS.

## 🚀 Características

- **Django 5.2** - Framework web moderno
- **Tailwind CSS** - Diseño responsive y moderno
- **Evaluaciones NOM-035** - Sistema de evaluaciones psicométricas
- **Sistema de Consultas** - Plataforma para consultas con psicólogos
- **Diseño Responsive** - Optimizado para móviles y desktop

## 🛠️ Tecnologías Utilizadas

- Python 3.12+
- Django 5.2
- Tailwind CSS 4.2
- Pillow (manejo de imágenes)
- PostgreSQL (recomendado para producción)

## 📦 Instalación Local

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd django
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Compilar Tailwind CSS
```bash
python manage.py tailwind build
```

### 6. Ejecutar servidor
```bash
python manage.py runserver
```

## 🌐 Despliegue en DigitalOcean

### Opción 1: App Platform (Recomendado)

1. **Conectar repositorio**:
   - Ve a DigitalOcean App Platform
   - Conecta tu repositorio de GitHub/GitLab
   - Selecciona la rama `main`

2. **Configurar aplicación**:
   ```yaml
   # .do/app.yaml
   name: psymetrics-global
   services:
   - name: web
     source_dir: /django
     github:
       repo: tu-usuario/tu-repositorio
       branch: main
     run_command: gunicorn psymetrics.wsgi:application
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     http_port: 8000
     envs:
     - key: DJANGO_SETTINGS_MODULE
       value: psymetrics.settings
     - key: DEBUG
       value: "False"
     - key: SECRET_KEY
       value: tu-secret-key-aqui
   ```

3. **Variables de entorno**:
   - `SECRET_KEY`: Genera una nueva clave secreta
   - `DEBUG`: `False` para producción
   - `ALLOWED_HOSTS`: Tu dominio de DigitalOcean
   - `DATABASE_URL`: URL de la base de datos PostgreSQL

### Opción 2: Droplet (VPS)

1. **Crear Droplet**:
   - Ubuntu 22.04 LTS
   - Mínimo 1GB RAM, 1 CPU
   - Agregar SSH key

2. **Configurar servidor**:
   ```bash
   # Conectar al servidor
   ssh root@tu-ip
   
   # Actualizar sistema
   apt update && apt upgrade -y
   
   # Instalar Python y dependencias
   apt install python3 python3-pip python3-venv nginx postgresql postgresql-contrib -y
   
   # Instalar Node.js para Tailwind
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   apt install nodejs -y
   ```

3. **Desplegar aplicación**:
   ```bash
   # Clonar repositorio
   git clone <tu-repositorio>
   cd django
   
   # Crear entorno virtual
   python3 -m venv venv
   source venv/bin/activate
   
   # Instalar dependencias
   pip install -r requirements.txt
   pip install gunicorn psycopg2-binary
   
   # Configurar base de datos
   sudo -u postgres createdb psymetrics_db
   sudo -u postgres createuser psymetrics_user
   
   # Migrar base de datos
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py tailwind build
   ```

4. **Configurar Gunicorn**:
   ```bash
   # Crear archivo gunicorn.service
   sudo nano /etc/systemd/system/psymetrics.service
   ```
   
   ```ini
   [Unit]
   Description=PsyMetrics Global Django App
   After=network.target
   
   [Service]
   User=www-data
   Group=www-data
   WorkingDirectory=/path/to/your/django
   ExecStart=/path/to/your/django/venv/bin/gunicorn --workers 3 --bind unix:/path/to/your/django/psymetrics.sock psymetrics.wsgi:application
   
   [Install]
   WantedBy=multi-user.target
   ```

5. **Configurar Nginx**:
   ```bash
   sudo nano /etc/nginx/sites-available/psymetrics
   ```
   
   ```nginx
   server {
       listen 80;
       server_name tu-dominio.com;
       
       location = /favicon.ico { access_log off; log_not_found off; }
       
       location /static/ {
           root /path/to/your/django;
       }
       
       location /media/ {
           root /path/to/your/django;
       }
       
       location / {
           include proxy_params;
           proxy_pass http://unix:/path/to/your/django/psymetrics.sock;
       }
   }
   ```

## 🔧 Configuración de Producción

### Variables de Entorno Importantes

```bash
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com', 'tu-ip']
SECRET_KEY = 'tu-secret-key-muy-seguro'
DATABASE_URL = 'postgresql://usuario:password@localhost:5432/psymetrics_db'
```

### Base de Datos PostgreSQL

```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# Crear base de datos
sudo -u postgres createdb psymetrics_db
sudo -u postgres createuser psymetrics_user
sudo -u postgres psql -c "ALTER USER psymetrics_user PASSWORD 'tu-password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE psymetrics_db TO psymetrics_user;"
```

## 📁 Estructura del Proyecto

```
django/
├── psymetrics/           # Configuración principal
├── evaluaciones/         # App de evaluaciones
├── consultas/           # App de consultas
├── theme/               # Configuración Tailwind
├── templates/           # Templates HTML
├── static/             # Archivos estáticos
├── media/              # Archivos de usuario
├── requirements.txt    # Dependencias Python
└── manage.py          # Script de Django
```

## 🔐 Seguridad

- Cambiar `SECRET_KEY` en producción
- Configurar `ALLOWED_HOSTS` correctamente
- Usar HTTPS en producción
- Configurar firewall (UFW)
- Mantener dependencias actualizadas

## 📞 Soporte

Para soporte técnico o consultas sobre el despliegue, contacta al equipo de desarrollo.

## 📄 Licencia

Este proyecto es propiedad de PsyMetrics Global. Todos los derechos reservados.
