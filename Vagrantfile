# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Configuration for the first virtual machine
  config.vm.define "confine" do |confine|
    confine.vm.box = "chenhan/ubuntu-desktop-20.04"
    confine.vm.synced_folder ".", "/home/vagrant/vagrant_data"
    confine.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = "2048"
    end
    confine.vm.provision "shell", inline: <<-SHELL
      apt-get update
    
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt-get update
    apt-get install -y docker-ce docker-ce-cli containerd.io
    usermod -aG docker vagrant
    sudo apt-get install -y sysdig
    sudo apt install mysql-client-core-8.0
    sudo snap install curl
    curl -sL https://raw.githubusercontent.com/slimtoolkit/slim/master/scripts/install-slim.sh | sudo -E bash -
    apt install -y sysdig
    # mongo client dependendcies
    sudo apt-get update
    sudo apt-get install libssl1.1
    wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
    sudo apt-get update
    sudo apt-get install -y mongodb-org
    sudo systemctl start mongod
    sudo systemctl enable mongod
    sudo apt-get install -y redis
    docker pull nginx:1.23.4
    docker pull python:3.9.16
    docker pull node:19-bullseye
    docker pull redis:7-bullseye
    docker pull httpd:2.4.54-bullseye
    docker pull mongo:6.0.9-jammy
    docker pull mysql:debian
    SHELL
  end

  # Configuration for the second virtual machine
  config.vm.define "speaker" do |speaker|
    speaker.vm.box = "kwilczynski/ubuntu-16.04"
    speaker.vm.synced_folder ".", "/home/vagrant/vagrant_data"
    speaker.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = "2048"
    end
    speaker.vm.provision "shell", inline: <<-SHELL
      apt-get update
    apt-get -y install libseccomp-dev
    apt-get -y install auditd
    sudo apt-get install libssl1.1
    sudo apt-get install -y make
    sudo apt-get install -y snapd
    sudo apt-get install -y gcc
    sudo apt-get install -y g++
    sudo apt-get install -y flex
    sudo apt-get install -y bison
    sudo apt-get install -y nginx
    sudo apt-get install -y nano
    sudo apt-get install -y git
    sudo apt-get install -y mysql-client
    sudo apt-get install -y mongodb-clients
    sudo apt-get install -y apache2-utils
    sudo apt-get install -y redis
    pip3 install numpy
    pip3 install matplotlib
    pip3 install pyPDF2
    pip3 install pillow
    pip3 install pandas
    pip3 install xlrd
    pip3 install openpyxl
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt-get update
    apt-get install -y docker-ce docker-ce-cli containerd.io
    usermod -aG docker vagrant
    sudo apt-get install -y sysdig
    sudo snap install curl
    SHELL
  end
  
  # Configuration for the third virtual machine
  config.vm.define "slimtoolkit" do |slimtoolkit|
    slimtoolkit.vm.box = "kwilczynski/ubuntu-16.04"
    slimtoolkit.vm.synced_folder ".", "/home/vagrant/vagrant_data"
    slimtoolkit.vm.provider "virtualbox" do |vb|
      vb.cpus = 2
      vb.memory = "2048"
    end
    slimtoolkit.vm.provision "shell", inline: <<-SHELL
    apt-get update
    sudo apt-get install libssl1.1
    sudo apt-get install -y snapd
    sudo apt-get install -y gcc
    sudo apt-get install -y g++
    sudo apt-get install -y nginx
    sudo apt-get install -y git
    sudo apt-get install -y mysql-client
    sudo apt-get install -y mongodb-clients
    sudo apt-get install -y apache2-utils
    sudo apt-get install -y redis
    pip3 install numpy
    pip3 install matplotlib
    pip3 install pyPDF2
    pip3 install pillow
    pip3 install pandas
    pip3 install xlrd
    pip3 install openpyxl
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt-get update
    apt-get install -y docker-ce docker-ce-cli containerd.io
    usermod -aG docker vagrant
    sudo apt-get install -y sysdig
    sudo snap install curl
    curl -sL https://raw.githubusercontent.com/slimtoolkit/slim/master/scripts/install-slim.sh | sudo -E bash -
    SHELL
  end
end

