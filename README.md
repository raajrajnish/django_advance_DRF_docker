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


#### vim editor commands
#### https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started
#### when doing git commit -a (inside editor use vim commands) also use ctrl + commands

#### CI/CD using travis CI
#### create file in root .travis.yml


#### writing django unit tests
#### make sure file name and function name must start with test as 
#### django looks for these files only to run unit tests

#### on change in files say requirements.txt run
#### docker-compose build

#### how to create app in project
#### sudo docker-compose run app sh -c 'djnago-admin.py startapp core'

#### remove right proctected folder - sudo rm -r foldername
#### remove right proctected file - sudo rm -f app/core/tests.py (filename)

#### please try docker compose to delete folder and file, i think it will work
#### because docker compose will use same user with rights to do this thing

#### create a folder docker-compose run app sh -c "mkdir /app/core/tests"
#### create a file docker-compose run app sh -c "touch /app/core/tests/__init__.py"

#### how to change readonly status of a folder sudo chown -R $(whoami) app/core/tests

#### run unit test - docker-compose run app sh -c "python manage.py test"
#### run migrations docker-compose run app sh -c "python manage.py makemigrations core"
#### run flake8 -  docker-compose run app sh -c "python manage.py test && flake8"



#### deployment
#### https://www.youtube.com/watch?v=ZpR1W-NWnp4