# This manifest file configures a nginx server with a custom http header

exec { 'configure a nginx server':
  command  => 'sudo apt-get -y update;
	sudo apt-get -y install nginx;
	sed -i "/index.nginx-debian.html/a add_header X-Served-By $hostname;" /etc/nginx/sites-available/default;
	sudo service nginx restart;',
  provider => 'shell',
}
