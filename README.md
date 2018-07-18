## Django test

Według tutoriala: https://docs.djangoproject.com/en/2.0/intro/tutorial01/

**ważne kroki:**
* *$ django-admin startproject mysite*<br>
* *$ python manage.py runserver* lub np *$ python manage.py runserver 0:8000*
* *$ python manage.py startapp polls*
* *views.py* to define views + *urls.py* to include **path()** to urlpatterns[] 

* *settings.py* to define database connection
* *$ python manage.py migrate*
* *$ models.py* - modele/definicje tabel w bazie
* *settings.py* to add INSTALLED_APPS, potrzebne do modeli / migracji
* *$ python manage.py makemigretions myapp*
* Jeśli chcę zobaczyć SQL to: *$ python manage.py sqlmigrate myapp 0001*
* *$ python manage.py migrate* <- aktualizuje bazę danych po zmianach w **models.py**
* *$ python manage.py shell* jeśli chcemy korzystać z databaseAPI
* add **__str__()** method for **models.py**
* *$ python manage.py createsuperuser* <- tworzy administratora i umożliwia korzystanie z myapp/admin/
* *admin.py* **admin.site.register(TableName)** <- tabela do edycji w myapp/admin/

* **templates** + namespacing + *render()*


