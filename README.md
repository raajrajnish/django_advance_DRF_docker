# Django DRF - Docker Architecture Guide
Run django drf in docker environment using postgresql as database.
#### IMPORTANT NOTE 
We will use Alpine version of docker image's as command apk only works with 
alpine images's of docker.

### Build Dockerfile file
Dockerfile commands:Build Dockerfile (with no extension) and run below commands
1. In terminal type >  sudo docker build . (mandatory step)
run docker build . in case of any change done to Dockerfile file

Please run command to see the non-rootuser > sudo docker run --rm 4ce871011bf5(buld id or name) id
for more info visit : https://www.thegeekdiary.com/run-docker-as-a-non-root-user/


### Build docker-compose.yml file
Helps in running docker image from our project location, it helps in running all 
services (example web-django,db-mongodb), Build docker-compose.yml file and run 
below commands:
1. from root run -> sudo docker-compose build (mandatory step)
run docker-compose build in case of any change done to docker-compose.yml file

### Run Docker in non sudo mode
Follow below steps to run docker without adding sudo for more info please visit:
https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo
Simple steps are :
1. sudo groupadd docker
2. sudo gpasswd -a $USER docker # whoami will print current user
3. newgrp docker
4. docker run hello-world

### Docker Commands
For more important docker commands please visit:
https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

### Create Django Project
1. from root -> sudo docker-compose run app (service name) sh -c 
   "django-admin.py startproject app ." (command to create project app)

### Create Django App
1. sudo docker-compose run app sh -c 'django-admin.py startapp core'
(command to create app core)
   
### Writing Django unit tests
while writing unit test make sure file name and function name must start with 
test as django looks for these files only to run unit tests

### Implement CI/CD using travis CI
create a file in root as .travis.yml file

#### vim editor commands
1. https://coderwall.com/p/adv71w/basic-vim-commands-for-getting-started
2. when doing git commit -a (inside editor use vim commands) also use ctrl + commands

### Handling Folder/File Permissions and Creations
1. remove right proctected folder - sudo rm -r foldername
2. remove right proctected file - sudo rm -f app/core/tests.py (filename)
3. how to change readonly status of a folder sudo chown -R $(whoami) app/core/tests
4. create a folder docker-compose run app sh -c "mkdir /app/core/tests"
5. create a file docker-compose run app sh -c "touch /app/core/tests/__init__.py"

### Running Docker/Git Commands
1. run unit test - docker-compose run app sh -c "python manage.py test"
2. run flake8 -  docker-compose run app sh -c "python manage.py test && flake8"
3. git push  git push -u https://github.com/raajrajnish/django_advance_DRF_docker.git


#### understanding port 
1. django is running internally in docker on http://0.0.0.0:8000
2. 0.0.0.0 = means any ip address inside docker
3. 8000 = port on which django is running internally in docker, please check docker
   compose.yml file to find to which external port it is using


#### https://www.youtube.com/watch?v=ZpR1W-NWnp4