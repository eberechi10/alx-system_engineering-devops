# puppet script to replace `phpp` to `php` in the server`.

exec { 'fix-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
