# Install Ansible
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible -y

# Python + PIP
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo pip3 install --upgrade pip

# Installing AWS dependencies
pip3 install awscli # AWS interface
pip3 install boto3
pip3 install nose
pip3 install tornado
pip3 install boto


