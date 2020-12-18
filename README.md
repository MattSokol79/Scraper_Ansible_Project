# ITJobsWatch Web Scraper app with Python
- A project which will create a dev, test and live environments for the 
  scrapper app in `App_Files`
  
## Pre-requisites
- Git
- Bash 
- AWS Account

## Dev Environment/Ansible Controller
### Setting up instance
- We can create a development environment in a multitude of ways including 
using Vagrant, however, for this example, we will use an EC2 instance created
on AWS.
- NOTE: THE EC2 INSTANCES WILL BE CREATED UNDER MY OWN VPC   
- To do this simply create an AWS account and follow the instructions in the link below
however, change the following options (Network: eng74-matt-project-vpc) and (Subnet: eng74-matt-Project-public)
[How to create an EC2 instance](https://github.com/MattSokol79/Ops_Notes/tree/main/Week_7_VPC/Day3_AWS)
- Name your instance appropriately

### Provisioning instance
- Git clone the contents of this repository and copy all of the files into the
EC2 instance -> Can be achieved in many ways, one way is to use `scp` and bash
  `scp -i <AWSkeypair.pem> -r <FolderPath> ubuntu@<PublicIPofinstance>`
- Now your dev environment should be set and provisioned with all necessary
files.
  
### Installing Dependencies
- Navigate to the `Ansible` directory and run the `ansible_controller_provision.sh` file
this will set up ansible and install necessary dependencies
- Navigate to the `App_Files` directory and run the command `pip install -r requirements.txt`
this installs all necessary modules required to run the app as well as tests  
- Before running the app create a Downloads folder in the `~/` as its necessary 
`cd ~/` and then `mkdir Downloads`  
- Run the app by navigating to directory containing `main.py` and write the 
command `pythom main.py` -> App should start working and should save csv files
into the Downloads folder

### Ansible Vault  
- In order to create AWS instances via Ansible, we will need to create
an ansible vault, do this with the command `ansible-vault create aws_keys.yml`
DONT FORGET YOUR PASSWORD!
- Once inside you will need to provide the vault with 2 keys to access AWS:
```
aws_access_key:
aws_secret_key:
```
- Ensure this file is stored in a `group_vars/all/` directory which you also
need to make sure is located in the `/etc/ansible/` directory
- Now we can run playbooks to create EC2 instances  

## Testing environment
- We can create the testing environment by simply running a playbook: (Ensure to change
relevant information in the playbook with your own information e.g. aws access key, name
of instance etc)
`sudo ansible-playbook playbook_test_env.yaml --ask-vault --tags create_ec2`
- Ensure to provide your vault password when prompted  
- If the build