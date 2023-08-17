# This manifest manages the ssh_config client
class config_ssh {

  ssh_config{ 'PasswordAuthentication':
      ensure => 'present',
      value  => 'no',
  }
  ssh_config { 'IdentityFile':
      ensure => 'present',
      value  => '~/.ssh/school',
  }
}
