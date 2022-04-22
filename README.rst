Intro 
=====
.. code-block:: docker

 docker pull ptsdocker16/interview-test-server
 docker run -d --name interview-test-server --init -p  5000:5000 -it ptsdocker16/interview-test-server 
 docker run -d --name pypointa pypointss4
 
 # http://172.17.0.5:8080/  --> should return a hey there!
 # http://localhost:5000/autonomous-car/ --> should show the instrcutions page

 docker network create points-network2
 docker network inspect points-network2
 docker network connect points-network2 pypointa
 docker network connect points-network2 interview-test-server
 docker inspect points-network2
 # note the IPv4Addresses 
 curl 172.20.0.3:5000/autonomous-car/routes/empty-route/





Resources
=========

.. code-block:: docker
    docker kill $(docker ps -q)
    docker rm $(docker ps -a -q)
    docker rmi $(docker images -q)
    docker rmi $(docker images --filter "dangling=true" -q --no-trunc)



 * Docker Article_ 
 * Docker and Poetry multistage poetry_docker_
 
.. _Article: https://medium.com/rockedscience/docker-ci-cd-pipeline-with-github-actions-6d4cd1731030  
.. _poetry_docker: https://github.com/python-poetry/poetry/discussions/1879