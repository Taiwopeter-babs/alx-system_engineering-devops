# This script increses the number of open file descriptors
# the web server open per request

exec {'fix-nginx-server-too-many-open-files-error':
command => 'sed -i "s/15/4096/" /etc/default/nginx; sudo service restart nginx',
  path  => '/usr/bin:/usr/sbin:/bin',
}
