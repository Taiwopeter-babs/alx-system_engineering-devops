# This script increses the number of open file descriptors
# the web server open per request
$com = 'sed -i'
$filename = '/etc/security/limits.conf'
$const = 'holberton'
$com_one = "${com} 's/${const} hard.*/${const} hard nofile 20000/' ${filename};"
$com_two = "${com} 's/${const} soft.*/${const} soft nofile 20000/' ${filename}"

exec {'fix-user-limit':
command  => "${com_one}${com_two}",
  path   => '/usr/bin:/usr/sbin:/bin',
  onlyif => 'test -e /etc/security/limits.conf',
}
