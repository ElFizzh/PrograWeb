# FizzhStore - Tienda de Ropa

Este proyecto es una tienda de ropa online desarrollada con Django.

## Requisitos

- Python 3.x
- Django
- Pillow (para manejo de imágenes)

## Instalación

1. Clona este repositorio o descárgalo como ZIP
2. Instala las dependencias:
   ```
   pip install django pillow
   ```
3. Aplica las migraciones:
   ```
   python manage.py migrate
   ```
4. Crea un superusuario (para acceder al panel de administración):
   ```
   python manage.py createsuperuser
   ```
5. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```
6. Accede a la aplicación en tu navegador: http://127.0.0.1:8000/

## Estructura del Proyecto

- `fizzhstore/`: Configuración principal del proyecto Django
- `tienda/`: Aplicación principal de la tienda
  - `models.py`: Modelos de datos (Producto, Categoría, Contacto)
  - `views.py`: Vistas para mostrar las páginas
  - `urls.py`: Configuración de URLs
  - `admin.py`: Configuración del panel de administración
- `templates/`: Plantillas HTML
- `static/`: Archivos estáticos (CSS, JS, imágenes)
- `media/`: Archivos subidos por los usuarios (imágenes de productos)

## Funcionalidades

- Catálogo de productos
- Filtrado por categorías
- Página de detalle de producto
- Formulario de contacto
- Panel de administración para gestionar productos y categorías

## Acceso al Panel de Administración

- URL: http://127.0.0.1:8000/admin/
- Usuario: carlos
- Contraseña: carlos123
