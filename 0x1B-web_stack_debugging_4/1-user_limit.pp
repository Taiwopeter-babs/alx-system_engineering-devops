# This script increses the number of open file descriptors
# the web server open per request
$com = 'sed -i'
$filename = '/etc/security/limits.conf'
$const = 'holberton'
exec {'fix-user-limit':
command  => "${com} 's/${const} hard.*/${const} hard nofile 20000/' ${filename}; " +
      "${com} 's/${const} soft.*/${const} soft nofile 20000/' ${filename}",
  path   => '/usr/bin:/usr/sbin:/bin',
  onlyif => 'test -e /etc/security/limits.conf',
}
