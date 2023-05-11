# This file replaces all wrong `.phpp` extensions with `.php`
# to correct the internal server error on apache hosting a wordpress site

exec {'wordpress-site-fix':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  provider => shell
}
