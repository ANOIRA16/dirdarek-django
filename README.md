
3. **Active virtual environment (env)**
```sh
source env/bin/activate
```

4. **install requirements**
```sh
pip install -r requirements.txt
```

5. **Run Migrations**

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

```

6. **Run Server**

```sh
python manage.py runserver
```

7. **And Creating an admin user (superuser)**

```sh
python manage.py createsuperuser
```


