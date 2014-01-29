echo "Este script hara lo siguiente:
1) Instalar modulos necesarios para web2py en CentOS/RHEL
2) Instalar web2py en /opt/web-apps/
3) Crear un certificado SSL
4) Instalar web2py con mod_wsgi y crear entradas de virtualhost en apache para responder 
a '/dtt/'
5) Colocar contrasena a web2py

Probablemente deberias leer este script antes de ejecutarlo.

Este script no toma encuenta SELINUX, si tienes SELINUX activado
probablemente tendras que realizar cambios en su configuracion.

Si utilizas iptables, deberas configurar la entrada del puerto 80 y 443.

v(autor: berubejd, modificado por: boriscougar)

Presiona ENTER para continuar...[ctrl+C para abortar]"

read CONFIRM

#!/bin/bash

###
###  Phase 0 - This may get messy.  Lets work from a temporary directory
###

current_dir=`pwd`

if [ -d /tmp/setup-web2py/ ]; then
    mv /tmp/setup-web2py/ /tmp/setup-web2py.old/
fi

mkdir -p /tmp/setup-web2py
cd /tmp/setup-web2py

###
###  Phase 1 - Requirements installation
###

echo
echo " - Installing required packages"
echo

# Install required packages
yum install httpd mod_ssl mod_wsgi wget python

# Rebuild wsgi to take advantage of Python 2.7
yum install httpd-devel

cd /tmp/setup-web2py
where_python=`which python2.7`
wget http://modwsgi.googlecode.com/files/mod_wsgi-3.3.tar.gz
tar -xzf mod_wsgi-3.3.tar.gz
cd mod_wsgi-3.3
./configure --with-python=${where_python}
make &&  make install

echo "LoadModule wsgi_module modules/mod_wsgi.so" > /etc/httpd/conf.d/wsgi.conf

cd /tmp/setup-web2py

echo
echo " - Stopping Apache Server to Install and start web2py"
echo
/etc/init.d/httpd stop

###
### Phase 2 - Install web2py
###

echo
echo " - Downloading, installing, and starting web2py"
echo

# Create web-apps directory, if required
if [ ! -d "/opt/web-apps" ]; then
    mkdir -p /opt/web-apps

    chmod 755 /opt
    chmod 755 /opt/web-apps
fi

cd /opt/web-apps

# Download web2py
if [ -e web2py_src.zip* ]; then
    rm web2py_src.zip*
fi

wget http://web2py.com/examples/static/web2py_src.zip
unzip web2py_src.zip
mv web2py/handlers/wsgihandler.py web2py/wsgihandler.py
# Configuring routes
cat  > /opt/web-apps/web2py/routes.py <<EOF

routers = dict(
 BASE = dict(
 path_prefix='dtt',
 )
)

EOF

chown -R apache:apache web2py

###
### Phase 3 - Setup SSL
###

echo
echo " - Creating a self signed certificate"
echo

# Verify ssl directory exists
if [ ! -d "/etc/httpd/ssl" ]; then
    mkdir -p /etc/httpd/ssl
fi

# Generate and protect certificate
openssl genrsa 1024 > /etc/httpd/ssl/self_signed.key
openssl req -new -x509 -nodes -sha1 -days 365 -key /etc/httpd/ssl/self_signed.key > /etc/httpd/ssl/self_signed.cert
openssl x509 -noout -fingerprint -text < /etc/httpd/ssl/self_signed.cert > /etc/httpd/ssl/self_signed.info

chmod 400 /etc/httpd/ssl/self_signed.*

###
### Phase 4 - Configure Apache
###

echo
echo " - Configure Apache to use mod_wsgi"
echo

# Create config
if [ -e /etc/httpd/conf.d/welcome.conf ]; then
    mv /etc/httpd/conf.d/welcome.conf /etc/httpd/conf.d/welcome.conf.disabled
fi

cat  > /etc/httpd/conf.d/default.conf <<EOF

NameVirtualHost *:80
NameVirtualHost *:443

<VirtualHost *:80>
  WSGIDaemonProcess web2py user=apache group=apache processes=1 threads=1
  WSGIProcessGroup web2py
  WSGIScriptAlias /dtt /opt/web-apps/web2py/wsgihandler.py
  WSGIPassAuthorization On

  <Directory /opt/web-apps/web2py>
    AllowOverride None
    Order Allow,Deny
    Deny from all
    <Files wsgihandler.py>
      Allow from all
    </Files>
  </Directory>

  AliasMatch ^/([^/]+)/static/(?:_[\d]+.[\d]+.[\d]+/)?(.*) /opt/web-apps/web2py/applications/\$1/static/\$2

  <Directory /opt/web-apps/web2py/applications/*/static>
    Options -Indexes
    Order Allow,Deny
    Allow from all
  </Directory>

  <Location /admin>
    Deny from all
  </Location>

  <LocationMatch ^/([^/]+)/appadmin>
    Deny from all
  </LocationMatch>

  CustomLog /var/log/httpd/access_log common
  ErrorLog /var/log/httpd/error_log
</VirtualHost>

<VirtualHost *:443>
  SSLEngine on
  SSLCertificateFile /etc/httpd/ssl/self_signed.cert
  SSLCertificateKeyFile /etc/httpd/ssl/self_signed.key

  WSGIProcessGroup web2py
  WSGIScriptAlias /dtt /opt/web-apps/web2py/wsgihandler.py
  WSGIPassAuthorization On

  <Directory /opt/web-apps/web2py>
    AllowOverride None
    Order Allow,Deny
    Deny from all
    <Files wsgihandler.py>
      Allow from all
    </Files>
  </Directory>

  AliasMatch ^/([^/]+)/static/(?:_[\d]+.[\d]+.[\d]+/)?(.*) /opt/web-apps/web2py/applications/\$1/static/\$2

  <Directory /opt/web-apps/web2py/applications/*/static>
    Options -Indexes
    ExpiresActive On
    ExpiresDefault "access plus 1 hour"
    Order Allow,Deny
    Allow from all
  </Directory>

  CustomLog /var/log/httpd/access_log common
  ErrorLog /var/log/httpd/error_log
</VirtualHost>

EOF

# Fix wsgi socket locations
echo "WSGISocketPrefix run/wsgi" >> /etc/httpd/conf.d/wsgi.conf

# Restart Apache to pick up changes
/etc/init.d/httpd restart

###
### Phase 5 - Setup web2py admin password
###

echo
echo " - Setup web2py admin password"
echo

cd /opt/web-apps/web2py 
su apache -s ${where_python} -c "from gluon.main import save_password; save_password(raw_input('admin password: '),443)"

###
### Phase 999 - Done!
###

# Change back to original directory
cd ${current_directory}

echo " - Complete!"
echo " Ahora puedes visitar https://dominio/dtt/admin/ para administrar web2py"
