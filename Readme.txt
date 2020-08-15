//Crear app dentro de proyecto 
python manage.py startapp <app_name>

//Documentacion metodos fild etc.
https://meet.google.com/linkredirect?authuser=5&dest=https%3A%2F%2Fdocs.djangoproject.com%2Fes%2F3.0%2Fref%2Fmodels%2Ffields%2F

//Una vez agregar la app a aplicaciones instaladas 
//(para crear la base de datos)
python manage.py makemigrations

//(para importarla)
python manage.py migrate

//(para insertar items desde consola)
python manage.py shell
*from -app-.models import -Tabla-
**myVar = -Tabla-.objects.all()
***myVarProducts.objects.create(
*****camp1=value,
*****camp2=value)
///Si quieres comprobar que si se creo, solo escribe "myVar" y debeta 
///tener un objeto


///////////////////////Para prender la app
///Activar el VENV
source venv/Scripts/activate
//Correrla
python manage.py runserver
//Abrir el navegador
localhost:8000/index/


//(Para borrar)
Products.objects.filter(pk=<el id a borrar>).delete()

/// Revisar versiones instaladas
pip freeze

// Guardar esa info en el txt
pip freese >name.txt

// Crear super usuario
python manage.py createsuperuser


-----Serializers leer por medio de api los productos---
class ProductsListAPI (ListCreateAPIView):
    serializer_class = ProductSerializer 
    queryset = Products.objects.all()  
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields='__all__'

from django.db import models

class Products(models.Model):
    name = models.CharField('NOMBRE/DESC PRODUCTO', max_length=60)
    category = models.CharField('Categoria', max_length=20)
    ubication = models.CharField('Ubicacion', max_length=60)
    lote = models.CharField('Lote', max_length=20)
