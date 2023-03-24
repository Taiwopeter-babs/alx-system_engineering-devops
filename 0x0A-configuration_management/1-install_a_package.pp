# This manifest file installs the flask package/framework

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
