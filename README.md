### Ansible flask

The goal was to create a web application with 3 routes using Flask and deploy it on an Azure virtual machine.
It was a question of making 3 routes:

  -get /id routes return current id,

  -get / inc increments the id,
 
  -and a route that returns welcome.
## Technologies used
### Front-end:
2. HTML
3. Jinja

### Back-end:
1. Flask

### automation tool:
1. Ansible

### Database:
1. Postgres

## How to used it
1. Clone this project `git clone https://github.com/FaroukDev/ansible_flask.git`
2. Move to the cloned directory `cd ansible_flask`
3. Run `ansible-playbook -i hosts playbook.yml -e ansible_python_interpreter=/usr/bin/python3 --key-file farouk-vm-ansible_key.pem `
4. Access to the website from your browser with `http://13.66.249.200:5000/`


