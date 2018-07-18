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
* *{% csrf_token %}* template tag inside \<form\> for **protection** against **Cross Site Request Forgeries**
* After incrementing the choice count, the code returns an *HttpResponseRedirect* rather than a normal HttpResponse. As the Python comment above points out, you should always return an **HttpResponseRedirect** after **successfully dealing with POST data**.
* *reverse()* to avoid to hardcode a URL in the view function.
* **generic views**: *generic.DetailView*, *generic.ListView*

* create *tests.py* with test cass and assertions
* *$ python manage.py test polls* to execute tets
* **The Django test client** to simulate a user interacting with the code at the **view level** (like a browser).
* *django.test.utils.setup_test_environment()* a template renderer which will allow us to examine some additional attributes on responses such as **response.context** that otherwise wouldn’t be available.
