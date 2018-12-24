
### Demo project

Create **myproject/settings/local.py** and specify DEBUG, ALLOWED_HOSTS and SECRET_KEY.
Change database credentials in **config/postgres/myproject.env**
Change nginx configuration in **config/nginx/conf.d/local.conf**

```sh
docker-compose build
docker-compose run --rm djangoapp /bin/bash -c "./manage.py migrate"
```

#### Connect to Postgres shell
```sh
docker exec -it dockerexp_myproject_1 psql -d myproject -U db_user
```
