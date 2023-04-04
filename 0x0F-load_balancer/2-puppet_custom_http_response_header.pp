# This manifest file configures a nginx server with a custom http header

exec { 'configure a nginx server':
  command  => 'sudo apt-get -y update;
	sudo apt-get -y install nginx;
	sed -i "/server { listen 80 default_server; listen [::]:80 default_server;
	root /var/www/html; add_header X-Served-By $hostname;}" /etc/nginx/sites-available/default;
	sudo service nginx restart;',
  provider => 'shell',
}
