# natemarks.docker

This is based entirely on a role created by Jeff Geerling. I customized it a little for our desktop ubuntu use case, but it's 90% huis work.

https://github.com/geerlingguy/ansible-role-docker


```shell
git clone https://github.com/natemarks/arole-docker.git
cd arole-docker
sudo apt install -y curl 
bash -c 'curl "https://raw.githubusercontent.com/natemarks/pipeline-scripts/v0.0.39/scripts/run_playbook.sh" | bash -s --  -p  playbook' 
```
