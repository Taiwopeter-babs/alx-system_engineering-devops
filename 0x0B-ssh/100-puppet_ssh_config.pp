# This manifest manages the ssh_config client
include stdlib
file_line { 'diasble password auth':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    match  => 'PasswordAuthentication',
    line   => 'PasswordAuthentication no',
  }
file_line { 'add identity file':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    match  => 'IdentityFile ~/.ssh/school',
    line   => 'IdentityFile ~/.ssh/school',
  }
