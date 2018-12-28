
## TODO:
- Logging
- Change to alpine images?


---
#### Set up server firewall
```sh
sudo ufw enable
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
```
**NOTE** It is important to allow port 22 in order to make SSH connections.

#### Add user deploy
It is recommended to add a user with sudo privileges to make deployments
```sh
sudo adduser deploy
sudo usermod -aG sudo deploy
```

#### Set up Docker and Docker Compose
Follow installation instructions in 
[Docker - Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
and
[Docker Compose - Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04)

---
### Set up directories

Create **foobar/settings/local.py** and specify DEBUG, ALLOWED_HOSTS and SECRET_KEY.
Change database credentials in **config/postgres/foobar.env**
Change nginx configuration in **config/nginx/dev/nginx.conf**

```sh
docker-compose build
docker-compose run --rm djangoapp /bin/bash -c "./manage.py migrate"
```

In production, use docker-compose.prod.yml in docker commands
```sh
docker-compose -f docker-compose.prod.yml build
```

#### Connect to Postgres shell
```sh
docker exec -it dockerexp_myproject_1 psql -d myproject -U db_user
```

#### Issue Let's Encrypt certificate
```sh
sudo chmod +x init-letsencrypt.sh
sudo ./init-letsencrypt.sh
```
