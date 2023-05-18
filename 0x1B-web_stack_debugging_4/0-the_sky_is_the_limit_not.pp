# This script increses the number of open file descriptors
# the web server open per request

exec {'sed -i "s/15/4096/" /etc/default/nginx':
  path   => '/usr/bin:/usr/sbin:/bin',
  onlyif => 'test -e /etc/default/nginx',
}

exec {'restart nginx':
  command => 'sudo service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
