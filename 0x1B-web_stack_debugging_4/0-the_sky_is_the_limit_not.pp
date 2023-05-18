# This script increses the number of open file descriptors
# the web server open per request

exec {'nginx-server-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  onlyif  => 'test -e /etc/default/nginx',
}

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin/',
}
