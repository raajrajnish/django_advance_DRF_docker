# django_advanced_DRF_docker
using django with drf and using docker

#### Docker Commands
0. Build Dockerfile (with no extension) then run below commands
1. After creating Dockerfile
2. In terminal type >  sudo docker build .
3. run command to see the non-rootuser > sudo docker run --rm 4ce871011bf5(buld id or name) id
#### https://www.thegeekdiary.com/run-docker-as-a-non-root-user/

### Docker Compose 
#### Lets to run our docker image from our project location, it helps in running all services (example web-django,db-mongodb)
0. Build docker-compose.yml file and run below commands
1. from root run -> sudo docker-compose build

#### Create Django Project
1. from root -> sudo docker-compose run app (service name) sh -c "django-admin.py startproject app ." (command)


#### Essentials Docker Commands
#### https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

#### Run docker without sudo
#### 1.  sudo groupadd docker
#### 1.  sudo gpasswd -a $USER docker # whoami will print current user
#### 3. newgrp docker
#### 4. docker run hello-world
#### https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo
