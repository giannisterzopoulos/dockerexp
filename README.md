
## TODO:
- Build and Host my own image - Use Docker swarm
- Use Restart Policy
- Scale Nginx
- Update README


# Need to push the image first in order to use Docker Swarm
docker build ...
sudo docker run --name django -d image_id
docker commit -m "initial commit" django terzopoulos/django:test1
docker push terzopoulos/django

# On server
docker pull ...
docker swarm init
docker build -t hello -f hello-service/Dockerfile hello-service
<!-- docker stack deploy --with-registry-auth -c ./docker-compose.yml talk -->
docker service scale swarm_demo_nginx=3

docker service logs votingapp_nginx

docker service ls
docker stack services swarm_demo
docker service ps swarm_demo_nginx
docker node ls
docker stack rm stackdemo  <!-- Bring the stack down -->

************************
- Set up local registry
docker run -d -p 50000:5000 --restart always --name custom-registry registry:latest
- Build the image
docker-compose -f docker-compose-swarm.yml up --build
(--> just use docker-compose build)
docker tag dockerexp_djangoapp:latest localhost:50000/djangoapp:latest
- Push the image to local registry
docker push localhost:50000/djangoapp


(init-letsencrypt.sh on all nodes using the nginx service)
<!-- docker pull terzopoulos/django:test1 -->
docker swarm init
docker swarm join...
docker stack deploy -c docker-compose-swarm.yml foobar_stack
docker stack services foobar_stack
docker stack ps foobar_stack
-------
docker ps (to find container id)
docker exec -it (container id) /bin/bash -c "./manage.py migrate"
docker exec -it (container id) /bin/bash -c "./manage.py collectstatic"


Server needs to have ports 80 and 443 open in inbound.
For Swarm:
TCP port 2377 for cluster management communications
TCP and UDP port 7946 for communication among nodes
UDP port 4789 for overlay network traffic


---
#### Set up server firewall
```sh
sudo ufw enable
sudo ufw allow 22,80,443,2377,7946/tcp
sudo ufw allow 4789,7946/udp
```
**NOTE**: It is important to allow port 22 in order to make SSH connections.

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

Specify POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVICE
and POSTGRES_PORT. POSTGRES_SERVICE needs to be the same with docker service.

Change nginx configuration in **config/nginx/dev/nginx.conf** if needed.

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
docker exec -it postgres-0 psql -d foobar -U db_user
```

#### Issue Let's Encrypt certificate
```sh
sudo chmod +x init-letsencrypt.sh
sudo ./init-letsencrypt.sh
```

To use "python manage.py runserver" in development:
In /etc/postgresql/8.3/main/postgresql.conf :
Change "port = 5432" to 5433 to avoid overlapping ports with docker
In config/postgres/foobar.env :
Change POSTGRES_SERVICE to localhost and POSTGRES_PORT to 5433

<!-- LOGS
logs are saved in /var/lib/docker/containers/container_id/container_id-json.log -->
