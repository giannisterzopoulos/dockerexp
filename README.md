
### Demo project

Create **project/settings/local.py** and specify DEBUG, ALLOWED_HOSTS and SECRET_KEY.
Change database credentials in **config/postgres/project.env**
Change nginx configuration in **config/nginx/conf.d/local.conf**

```sh
docker compose build
docker-compose run --rm djangoapp /bin/bash -c "./manage.py migrate"
```

#### Connect to Postgres shell
```sh
docker exec -it dockerexp_project_1 psql -d project -U db_user
```
