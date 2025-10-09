#!/bin/bash

# Script de despliegue para PsyMetrics Global en DigitalOcean
# Ejecutar desde el directorio raíz del proyecto

echo "🚀 Iniciando despliegue de PsyMetrics Global..."

# Verificar que estamos en el directorio correcto
if [ ! -f "manage.py" ]; then
    echo "❌ Error: No se encontró manage.py. Ejecuta este script desde el directorio raíz del proyecto."
    exit 1
fi

# Crear directorio de logs si no existe
mkdir -p logs

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# Compilar Tailwind CSS
echo "🎨 Compilando Tailwind CSS..."
python manage.py tailwind build

# Ejecutar migraciones
echo "🗄️ Ejecutando migraciones..."
python manage.py migrate

# Recopilar archivos estáticos
echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

# Crear superusuario si no existe
echo "👤 Creando superusuario..."
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@psymetricsglobal.com', 'admin123')
    print('Superusuario creado: admin/admin123')
else:
    print('Superusuario ya existe')
EOF

# Verificar configuración
echo "✅ Verificando configuración..."
python manage.py check --deploy

echo "🎉 Despliegue completado exitosamente!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Configurar variables de entorno en DigitalOcean"
echo "2. Configurar base de datos PostgreSQL"
echo "3. Configurar dominio personalizado (opcional)"
echo "4. Configurar SSL/HTTPS"
echo ""
echo "🔗 URLs importantes:"
echo "- Aplicación: https://tu-app.ondigitalocean.app"
echo "- Admin: https://tu-app.ondigitalocean.app/admin"
echo "- Logs: Revisar en el panel de DigitalOcean"
