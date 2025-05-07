from django.contrib.auth.models import User

# Eliminar usuario admin si existe
User.objects.filter(username='admin').delete()

# Crear un nuevo superusuario
User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)

print('Superusuario creado/actualizado con éxito')