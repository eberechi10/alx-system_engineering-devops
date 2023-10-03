#  Puppet script install and configure Nginx.

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!\n',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => 'file',
  content => "server {
    listen 80;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location /redirect_me {
        return 301 https://www.github.com/eberechi10;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html/;
        internal;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/var/www/html/404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page\n",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
