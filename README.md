# PsyMetrics Global - Django Application

Aplicación web Django para evaluaciones psicométricas online con Tailwind CSS.

## 🚀 Características

- **Django 5.2** - Framework web moderno
- **Tailwind CSS 4.2** - Diseño responsive y moderno con tema personalizado
- **Evaluaciones NOM-035** - Sistema completo de evaluaciones psicométricas con dominios y preguntas
- **Sistema de Consultas** - Plataforma para consultas con psicólogos especializados
- **Diseño Responsive** - Optimizado para móviles y desktop con Alpine.js
- **Panel de Administración** - Django Admin integrado para gestión de contenido
- **Autenticación de Usuarios** - Sistema completo de login/logout
- **Dashboard Personalizado** - Panel para usuarios autenticados
- **Sistema de Mensajería** - Comunicación entre clientes y psicólogos
- **Gestión de Disponibilidad** - Sistema de horarios para psicólogos

## 💻 Tecnologías Utilizadas

- Python 3.12+
- Django 5.2
- Tailwind CSS 4.2 con configuración personalizada
- Alpine.js (interactividad frontend)
- Pillow (manejo de imágenes)
- PostgreSQL (producción)
- SQLite (desarrollo)
- Gunicorn (servidor WSGI)
- Honcho (gestión de procesos)
- django-tailwind (integración de Tailwind)
- django-browser-reload (recarga automática en desarrollo)

## 📦 Instalación Local

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd django
```

### 2. Crear entorno virtual
```bash
# Se recomienda usar .venv_psmetrics como nombre
python -m venv .venv_psmetrics
source .venv_psmetrics/bin/activate  # En Windows: .venv_psmetrics\Scripts\activate
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

**Opción A: Servidor estándar (sin recarga automática de Tailwind)**
```bash
python manage.py runserver
```

**Opción B: Con recarga automática de Tailwind (recomendado para desarrollo)**
```bash
# Usa honcho para ejecutar Django y Tailwind simultáneamente
honcho start -f Procfile.tailwind
```

La aplicación estará disponible en: http://127.0.0.1:8000

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
├── psymetrics/              # Configuración principal del proyecto
│   ├── settings.py         # Configuración de desarrollo (SQLite, DEBUG=True)
│   ├── settings_production.py  # Configuración de producción (PostgreSQL, seguridad)
│   ├── urls.py             # Enrutamiento principal
│   ├── wsgi.py             # Punto de entrada WSGI
│   └── asgi.py             # Punto de entrada ASGI
├── evaluaciones/            # App de evaluaciones psicométricas
│   ├── models.py           # Modelos: Cuestionario, Dominio, Pregunta, Respuesta
│   ├── views.py            # Vistas: Home, Servicios, Dashboard
│   ├── urls.py             # URLs de la app
│   ├── admin.py            # Configuración del admin
│   └── migrations/         # Migraciones de base de datos
├── consultas/               # App de consultas con psicólogos
│   ├── models.py           # Modelos: Psicólogo, Consulta, Disponibilidad
│   ├── views.py            # Vistas: Consultas, Mis Consultas
│   ├── urls.py             # URLs de la app
│   ├── admin.py            # Configuración del admin
│   └── migrations/         # Migraciones de base de datos
├── theme/                   # Configuración de Tailwind CSS
│   ├── static_src/         # Código fuente de Tailwind
│   │   ├── tailwind.config.js  # Configuración personalizada (colores, fuentes)
│   │   ├── styles.css          # Estilos personalizados
│   │   └── package.json        # Dependencias npm
│   └── static/             # Archivos CSS compilados
├── templates/               # Templates HTML globales
│   ├── base.html           # Template base con navegación y footer
│   ├── home.html           # Página de inicio
│   ├── servicios.html      # Página de servicios
│   ├── nosotros.html       # Página sobre nosotros
│   ├── contacto.html       # Página de contacto
│   ├── dashboard.html      # Panel de usuario
│   ├── evaluaciones/       # Templates de evaluaciones
│   └── consultas/          # Templates de consultas
├── static/                  # Archivos estáticos (imágenes, etc.)
├── staticfiles/             # Archivos estáticos recopilados (producción)
├── media/                   # Archivos subidos por usuarios
├── .do/                     # Configuración de DigitalOcean
│   └── app.yaml            # Definición de la aplicación
├── requirements.txt         # Dependencias Python
├── gunicorn.conf.py         # Configuración de Gunicorn
├── deploy.sh                # Script de despliegue automático
├── Procfile                 # Configuración para despliegue
├── Procfile.tailwind        # Configuración para desarrollo con Tailwind
├── manage.py                # Script de gestión de Django
└── db.sqlite3               # Base de datos de desarrollo
```

## 📦 Modelos de Datos

### Aplicación de Evaluaciones

**CuestionarioNOM035**
- Cuestionarios con versiones y estados (borrador, activo, inactivo)
- Campos: nombre, versión, descripción, estado, fecha_creación, creado_por

**DominioNOM035**
- Dominios/secciones de los cuestionarios con orden
- Campos: cuestionario (FK), nombre, descripción, orden

**PreguntaNOM035**
- Preguntas individuales (Likert, opción múltiple, abierta)
- Campos: dominio (FK), texto, tipo, orden, obligatoria

**OpcionRespuesta**
- Opciones de respuesta con puntuación
- Campos: pregunta (FK), texto, valor, orden

**Evaluacion**
- Instancias de evaluación con estados (iniciada, en progreso, completada, cancelada)
- Campos: cuestionario (FK), evaluado (FK), evaluador (FK), estado, puntuación_total

**RespuestaEvaluacion**
- Respuestas individuales con timestamps
- Campos: evaluacion (FK), pregunta (FK), opcion_seleccionada (FK), respuesta_texto, puntuación

**TipoEvaluacion** y **EvaluacionPersonalizada**
- Tipos de evaluaciones personalizadas con duración y precios

### Aplicación de Consultas

**Psicologo**
- Perfiles de psicólogos con especialidades (organizacional, clínica, cognitiva, industrial, social)
- Campos: usuario (OneToOne), especialidad, experiencia_anos, descripción, tarifa_hora, disponible, foto

**TipoConsulta**
- Tipos de consultas con duración y precios
- Campos: nombre, descripción, duracion_minutos, precio, activo

**Consulta**
- Sesiones de consulta con estados (solicitada, confirmada, en progreso, completada, cancelada)
- Campos: cliente (FK), psicologo (FK), tipo_consulta (FK), fecha_agendada, estado, motivo_consulta, calificación

**DisponibilidadPsicologo**
- Horarios disponibles por día de la semana
- Campos: psicologo (FK), dia_semana, hora_inicio, hora_fin, activo

**MensajeConsulta**
- Sistema de mensajería para consultas
- Campos: consulta (FK), remitente (FK), mensaje, fecha_envio, leido

## 📡 Rutas de la Aplicación

### Evaluaciones (`/`)
- `/` - Página de inicio
- `/servicios/` - Servicios ofrecidos
- `/nosotros/` - Información de la empresa
- `/contacto/` - Formulario de contacto
- `/dashboard/` - Panel de usuario (requiere autenticación)
- `/solicitar-evaluacion/` - Solicitud de evaluación (POST)

### Consultas (`/consultas/`)
- `/consultas/` - Listado de consultas disponibles
- `/consultas/mis-consultas/` - Consultas del usuario (requiere autenticación)
- `/consultas/solicitar-consulta/` - Solicitud de consulta (POST)

### Administración (`/admin/`)
- `/admin/` - Panel de administración de Django
- `/admin/login/` - Inicio de sesión
- `/admin/logout/` - Cierre de sesión

## 🎨 Personalización de Tailwind

El proyecto incluye una configuración personalizada de Tailwind CSS:

**Colores Personalizados:**
- `primary` - Azul oscuro (#0F2C4B) - Color principal del logo
- `accent` - Teal (#36A89C) - Color de acento del logo

**Tipografía:**
- Fuente principal: Inter (Google Fonts)

**Ubicación:** `theme/static_src/tailwind.config.js`

## 🔐 Seguridad

- Cambiar `SECRET_KEY` en producción
- Configurar `ALLOWED_HOSTS` correctamente
- Usar HTTPS en producción
- Configurar firewall (UFW)
- Mantener dependencias actualizadas
- Cookies seguras habilitadas en producción (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
- Protección XSS y Content Type Sniffing
- X-Frame-Options configurado a DENY

## 🛠️ Comandos Útiles para Desarrollo

### Migraciones
```bash
# Crear migraciones para ambas apps
python manage.py makemigrations evaluaciones consultas

# Aplicar todas las migraciones
python manage.py migrate

# Ver historial de migraciones
python manage.py showmigrations

# Revertir migración específica
python manage.py migrate evaluaciones 0001
```

### Django Shell
```bash
# Abrir shell de Django para pruebas
python manage.py shell

# Ejemplo de uso en shell:
# from evaluaciones.models import CuestionarioNOM035
# from django.contrib.auth.models import User
# cuestionarios = CuestionarioNOM035.objects.all()
```

### Usuarios y Autenticación
```bash
# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña de usuario
python manage.py changepassword username
```

### Archivos Estáticos y Tailwind
```bash
# Compilar Tailwind (solo CSS)
python manage.py tailwind build

# Modo de desarrollo con watch (recarga automática)
python manage.py tailwind start

# Recopilar archivos estáticos para producción
python manage.py collectstatic --noinput

# Limpiar archivos estáticos antiguos
python manage.py collectstatic --clear --noinput
```

### Base de Datos
```bash
# Resetear base de datos (CUIDADO: Elimina todos los datos)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser

# Hacer backup de SQLite
cp db.sqlite3 db.sqlite3.backup

# Exportar datos
python manage.py dumpdata evaluaciones > evaluaciones_data.json
python manage.py dumpdata consultas > consultas_data.json

# Importar datos
python manage.py loaddata evaluaciones_data.json
```

### Verificaciones
```bash
# Verificar problemas del proyecto
python manage.py check

# Verificar problemas de despliegue
python manage.py check --deploy

# Verificar migraciones sin aplicar
python manage.py showmigrations --plan
```

## 📝 Variables de Entorno

### Desarrollo
Las variables de desarrollo están configuradas en `psymetrics/settings.py`:
- `DEBUG=True`
- `ALLOWED_HOSTS=['*']`
- Base de datos: SQLite

### Producción
Configurar las siguientes variables de entorno en DigitalOcean:

```bash
DJANGO_SETTINGS_MODULE=psymetrics.settings_production
DEBUG=False
SECRET_KEY=tu-secret-key-muy-seguro-aqui
ALLOWED_HOSTS=tu-dominio.com,*.ondigitalocean.app

# Base de datos
DB_NAME=psymetrics_db
DB_USER=psymetrics_user
DB_PASSWORD=tu-password-seguro
DB_HOST=db-postgresql-nyc1-12345.ondigitalocean.com
DB_PORT=25060

# Email (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-password-de-app
DEFAULT_FROM_EMAIL=noreply@psymetricsglobal.com

# Redis (opcional)
REDIS_URL=redis://localhost:6379/1
```

## 📞 Soporte

Para soporte técnico o consultas sobre el despliegue, contacta al equipo de desarrollo.

## 👨‍💻 Desarrollo y Contribución

### Estructura de Django Apps

El proyecto sigue la arquitectura estándar de Django con dos aplicaciones principales:

1. **evaluaciones** - Maneja todo lo relacionado con cuestionarios y evaluaciones psicométricas
2. **consultas** - Gestiona las consultas con psicólogos y disponibilidad

### Admin de Django

Actualmente los modelos no están registrados en el admin. Para habilitarlos, editar:
- `evaluaciones/admin.py`
- `consultas/admin.py`

Ejemplo:
```python
from django.contrib import admin
from .models import CuestionarioNOM035, DominioNOM035, PreguntaNOM035

@admin.register(CuestionarioNOM035)
class CuestionarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'version', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion']
```

### Buenas Prácticas

- Siempre crear migraciones después de modificar modelos
- Compilar Tailwind antes de hacer commit de cambios en estilos
- Probar cambios con `python manage.py check` antes de desplegar
- Usar `.venv_psmetrics` como nombre del entorno virtual para consistencia
- Mantener separadas las configuraciones de desarrollo y producción

### Localización

- **Idioma:** Español (es-es)
- **Zona Horaria:** America/Mexico_City
- Los templates y mensajes están en español

## 📝 Licencia

Este proyecto es propiedad de PsyMetrics Global. Todos los derechos reservados.

