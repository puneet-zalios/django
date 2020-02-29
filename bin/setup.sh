#!/bin/bash

#Update the apt package index:
sudo apt update

# Install packages to allow apt to use a repository over HTTPS:
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

# Add Docker’s official GPG key:
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# set up the stable repository.
sudo add-apt-repository "deb https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"

# Update the apt package index && Install the latest version of Docker CE, or
# go to the next step to install a specific version:
sudo apt-get update && sudo apt-get install -y docker-ce=$(apt-cache madison docker-ce | grep 18.03 | head -1 | awk '{print $3}')

# Install docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Add default user to docker group
sudo usermod -a -G docker $USER
sudo su - $USER
