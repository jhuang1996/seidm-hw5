
## setup vim
```
set nu
set softtabstop=4
set tabstop=4
set shiftwidth=4
set expandtab
```

## setup ubuntu
```
sudo apt-get update
xargs sudo apt-get install < aptlist
```

## setup python virtualenv
```
sudo pip install pip --upgrade
sudo pip install virtualenv
virtualenv -p python3 ~/.env
source ~/.env/bin/activate
pip install -r requirements.txt
```

## setup mysqladmin
```
mysql-ctl start
mysqladmin -u root password '<root pass>'
(mysqladmin -u root -p'<old root pass>' password '<new root pass>')
```

## setup ssh key for github
```
chmod 700 ~/.ssh
(copy or create private key from somewhere else)
chmod 644 ~/.ssh/<key.pub>
chmod 600 ~/.ssh/<key>
sed -i "/IdentityFile/s/id_rsa/<key>/g" ~/.ssh/config
```

## setup github workflow
```
(fork from public repo to private repo)
git clone git@github.com:<github id>/<repo>.git
```
