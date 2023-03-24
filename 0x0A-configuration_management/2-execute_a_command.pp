# This manifest file executes a pkill command

exec { 'pkill -f killmenow':
  path   => '/bin/',
  onlyif => 'ps aux | grep [k]illmenow',
}

