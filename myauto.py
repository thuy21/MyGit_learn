# -*- coding: utf-8 -*
import os
import sys

def rebootStart():
	os.system('systemctl stop firewalld')
	os.system('systemctl disable firewalld')
	seLinuxTxt = open('/etc/selinux/config','r')
	txtCont = seLinuxTxt.read()
	seLinuxTxt.close()
	seLinuxTxt = open('/etc/selinux/config','w')
	newTxt=txtCont.replace('SELINUX=enforcing','SELINUX=disabled')
	seLinuxTxt.write(newTxt)
	seLinuxTxt.close()

	'''os.system('reboot')'''
def log_wirte(res):
        log_txt=open(path+'/log.txt','w')
        log_txt.write(res)
        log_txt.close()
        

def commStartList(index):
        path=os.getcwd()
        if index<=1:
                os.chdir('/')
                res= os.system('tar -xvf yumrepo.tar.gz')
                if res!=0:
                        print('Error:yumrepo.tar.gz文件不存在')
                        log_wirte('1')
                        os._exit(0)
        if index<=2:
                os.chdir('/')
                res=os.system('tar -xvf install.tar.gz')
                if res!=0:
                        print('Error:install.tar.gz文件不存在')
                        log_wirte('2')
                        os._exit(0)
        if index<=3:
                res= os.system('mkdir /etc/yum.repos.d/bak')
                if res!=0:
                        print('Error:/etc/yum.repos.d/bak执行失败')
                        log_wirte('3')
                        os._exit(0)
        if index<=4:
                os.chdir('/')
                res=os.system('mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bak/')
                if res!=0:
                        print('Error:mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bak/执行失败')
                        log_wirte('4')
                        os._exit(0)
        if index<=5:
                os.chdir('/yumrepo')
                res= os.system('cp mnt.repo /etc/yum.repos.d/')
                if res!=0:
                        print('Error:mnt.repo /etc/yum.repos.d/执行失败')
                        log_wirte('5')
                        os._exit(0)
        if index<=6:
                res=os.system('mv packages /packages')
                if res!=0:
                        print('Error:packages /packages执行失败')
                        log_wirte('6')
                        os._exit(0)
        if index<=7:
                res= os.system('rpm -ivh /yumrepo/deltarpm-3.6-3.el7.x86_64.rpm')
                if res!=0:
                        print('Error:eltarpm-3.6-3.el7.x86_64.rpm依赖包安装失败')
                        log_wirte('7')
                        os._exit(0)
        if index<=8:
                res= os.system('rpm -ivh /yumrepo/python-deltarpm-3.6-3.el7.x86_64.rpm')
                if res!=0:
                        print('Error:python-deltarpm-3.6-3.el7.x86_64.rpm依赖包安装失败')
                        log_wirte('8')
                        os._exit(0)
        if index<=9:
                res= os.system('rpm -ivh /yumrepo/libxml2-python-2.9.1-6.el7_2.3.x86_64.rpm')
                if res!=0:
                        print('Error:libxml2-python-2.9.1-6.el7_2.3.x86_64.rpm依赖包安装失败')
                        log_wirte('9')
                        os._exit(0)
        if index<=10:
                res= os.system('rpm -ivh /yumrepo/createrepo-0.9.9-28.el7.noarch.rpm')
                if res!=0:
                        print('Error:createrepo-0.9.9-28.el7.noarch.rpm依赖包安装失败')
                        log_wirte('10')
                        os._exit(0)
        if index<=11:
                res= os.system('createrepo /packages/')
                if res!=0:
                        print('Error:createrepo /packages/执行失败')
                        log_wirte('11')
                        os._exit(0)
        if index<=12:
                os.system('yum clean all')
                res=os.system('yum makecache')
                if res!=0:
                        print('Error:makecache执行失败')
                        log_wirte('12')
                        os._exit(0)
        if index<=13:
                res=os.system('yum install net-tools')
                if res!=0:
                        print('Error:install net-tools执行失败')
                        log_wirte('13')
                        os._exit(0)
        if index<=14:
                res= os.system('yum install /install/gcc-c++ ncurses-devel bison zlib-devel zip unzip -y')
                if res!=0:
                        print('Error:gcc-c++ ncurses-devel bison zlib-devel依赖包安装失败')
                        log_wirte('14')
                        os._exit(0)
        if index<=15:
                res= os.system('yum install httpd httpd-devel')
                if res!=0:
                        print('Error:install httpd httpd-devel安装失败')
                        log_wirte('15')
                        os._exit(0)
        if index<=16:
                os.system('groupadd www')
                res= os.system('useradd --shell /sbin/nologin -g www www')
                if res!=0:
                        print('Error:seradd --shell /sbin/nologin -g www www执行失败')
                        log_wirte('16')
                        os._exit(0)
        if index<=17:
                res= os.system('cp -r /install/config/httpd.conf /etc/httpd/conf/httpd.conf')
                if res!=0:
                        print('Error:/install/config/httpd.conf /etc/httpd/conf/httpd.conf失败')
                        log_wirte('17')
                        os._exit(0)
        if index<=18:
                res= os.system('cp -r /install/config/vhost.conf /etc/httpd/conf.d/vhost.conf')
                if res!=0:
                        print('Error:/install/config/vhost.conf /etc/httpd/conf.d/vhost.conf执行失败')
                        log_wirte('18')
                        os._exit(0)
        if index<=19:
                res=os.system('yum -y install wget vim pcre pcre-devel openssl openssl-devel libicu-devel gcc gcc-c++ autoconf libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel glibc glibc-devel glib2 glib2-devel ncurses ncurses-devel curl curl-devel krb5-devel libidn libidn-devel openldap openldap-devel nss_ldap jemalloc-devel cmake boost-devel bison automake libevent libevent-devel gd gd-devel libtool* libmcrypt libmcrypt-devel mcrypt mhash libxslt libxslt-devel readline readline-devel gmp gmp-devel libcurl libcurl-devel openjpeg-devel')
                if res!=0:
                        print('Error:wget vim pcre pcre-devel openssl...执行失败')
                        log_wirte('19')
                        os._exit(0)
        if index<=20:
                res= os.system('tar -xvf /install/php-7.2.1.tar.gz')
                if res!=0:
                        print('Error:/install/config/httpd.conf /etc/httpd/conf/httpd.conf失败')
                        log_wirte('20')
                        os._exit(0)
        if index<=21:
                os.chdir('php-7.2.1')
                res= os.system('cp -frp /usr/lib64/libldap* /usr/lib/')
                if res!=0:
                        print('Error:cp -frp /usr/lib64/libldap* /usr/lib/执行失败')
                        log_wirte('21')
                        os._exit(0)
        if index<=22:
                res= os.system('./configure --prefix=/usr/local/php \
--with-config-file-path=/usr/local/php/etc \
--enable-fpm \
--with-fpm-user=www \
--with-fpm-group=www \
--enable-mysqlnd \
--with-mysqli=mysqlnd \
--with-pdo-mysql=mysqlnd \
--enable-mysqlnd-compression-support \
--with-iconv-dir \
--with-freetype-dir \
--with-jpeg-dir \
--with-png-dir \
--with-zlib \
--with-libxml-dir \
--enable-xml \
--disable-rpath \
--enable-bcmath \
--enable-shmop \
--enable-sysvsem \
--enable-inline-optimization \
--with-curl \
--enable-mbregex \
--enable-mbstring \
--enable-intl \
--with-mcrypt \
--with-libmbfl \
--enable-ftp \
--with-gd \
--enable-gd-jis-conv \
--enable-gd-native-ttf \
--with-openssl \
--with-mhash \
--enable-pcntl \
--enable-sockets \
--with-xmlrpc \
--enable-zip \
--enable-soap \
--with-gettext \
--disable-fileinfo \
--enable-opcache \
--with-pear \
--enable-maintainer-zts \
--with-ldap=shared \
--without-gdbm \
--with-apxs2=/usr/bin/apxs \
--with-icu-dir=/usr')
                if res!=0:
                        print('Error:第22失败')
                        log_wirte('22')
                        os._exit(0)
        if index<=23:
                res= os.system('make -j 4 && make install')
                if res!=0:
                        print('Error:make -j 4 && make install失败')
                        log_wirte('23')
                        os._exit(0)

                        

log_file=os.path.exists('log.txt')
path=os.getcwd()
if log_file:
        log_txt=open('log.txt','r')
        res=int(log_txt.read())
        commStartList(res)
else:
        rebootStart()
        log_txt=open('log.txt','w')
        log_txt.write('1')
        log_txt.close()
        commStartList(1)
        

os.system('cp /install/config/php.ini /usr/local/php/etc/php.ini')
os.system('cp /usr/local/php/etc/php-fpm.conf.default /usr/local/php/etc/php-fpm.conf')
os.system('cp /usr/local/php/etc/php-fpm.d/www.conf.default /usr/local/php/etc/php-fpm.d/www.conf')
os.system('ln -s /usr/local/php/bin/php /usr/bin/php')

os.chdir('/install')
os.system('yum -y install memcached')
os.system('chkconfig memcached on')
seLinuxTxt = open('/etc/sysconfig/memcached','r')
txtCont = seLinuxTxt.read()
seLinuxTxt.close()
seLinuxTxt = open('/etc/sysconfig/memcached','w')
newTxt=txtCont.replace('PORT="11211"','PORT="12580"')
seLinuxTxt.write(newTxt)
seLinuxTxt.close()
os.system('service memcached start')
os.system('rpm -ql memcached')
os.system('netstat -tunlp | grep memcached')

'''
while True:
    try:
        res = input('1280端口是否启动？键入"1"继续，键入"0"终止:')
        if int(res)==1:
	  break
        else:
            if int(res)==0:
                os._exit(0)
    except:
         print('input error:')
         '''

os.chdir('/install')
os.system('tar -zxvf libmemcached-1.0.18.tar.gz')
os.chdir('libmemcached-1.0.18')
os.system('./configure --prefix=/usr/lib/libmemcached')
os.system('make && make install')
os.chdir('..')


os.system('tar -xvf php-memcached.tar.gz')
os.chdir("php-memcached")
os.system('/usr/local/php/bin/phpize')
os.system('./configure -enable-memcached -with-php-config=/usr/local/php/bin/php-config -with-zlib-dir -with-libmemcached-dir=/usr/lib/libmemcached -prefix=/usr/local/phpmemcached --disable-memcached-sasl')
os.system('make && make install')
os.chdir('..')

os.chdir("memcache")
os.system('/usr/local/php/bin/phpize')
os.system('./configure -with-php-config=/usr/local/php/bin/php-config')
os.system('make && make install')
os.chdir('..')

os.chdir('/install/php-7.2.1/ext/exif/')
os.system('/usr/local/php/bin/phpize')
os.system('./configure --with-php-config=/usr/local/php/bin/php-config')
os.system('make && make install')
os.chdir('/install')
os.system('tar -xvf mysql-5.7.25-1.el7.x86_64.rpm-bundle.tar')
os.system('rpm -ivh mysql-community-common-5.7.25-1.el7.x86_64.rpm --replacefiles')
os.system('rpm -e `rpm -qa |grep mariadb-libs` --nodeps')
os.system('rpm -ivh mysql-community-libs-5.7.25-1.el7.x86_64.rpm')
os.system('rpm -ivh mysql-community-client-5.7.25-1.el7.x86_64.rpm')
os.system('rpm -ivh mysql-community-server-5.7.25-1.el7.x86_64.rpm')
os.system('rpm -ivh mysql-community-devel-5.7.25-1.el7.x86_64.rpm')
os.system('systemctl start mysqld')
'''
os.system('cat /var/log/mysqld.log |grep password')
os.system('mysql -uroot -p')
os.system("cp -r /install/config/my.cnf /etc/")
os.system('systemctl restart mysqld')
'''
os.chdir('/')
os.system('yum install -y gcc-c++ pcre pcre-devel zlib zlib-devel openssl openssl-devel')
os.system('tar -xvf /install/nginx-1.14.2.tar.gz')
os.chdir('/install/nginx-1.14.2')
os.system('./configure')
os.system('make && make install')
os.system('cp -r /install/config/nginx.service /lib/systemd/system/')
os.system('cp -r /install/config/nginx.conf /usr/local/nginx/conf/')
os.system('systemctl enable nginx.service')

'------------------------------------------------------------------------------------------------------------------------------------'
os.chdir('/install')
os.system('mkdir /usr/java')
os.system('cp jdk-8u211-linux-x64.tar.gz /usr/java')
os.chdir('/usr/java')
os.system('tar -xvf jdk-8u211-linux-x64.tar.gz')

seLinuxTxt = open('/etc/profile','r+')
txtCont = seLinuxTxt.read()
seLinuxTxt.write('export JAVA_HOME=/usr/java/jdk1.8.0_211\n')
seLinuxTxt.write('export JRE_HOME=/usr/java/jdk1.8.0_211/jre\n')
seLinuxTxt.write('export CLASSPATH=.:$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH\n')
seLinuxTxt.write('export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH\n')
seLinuxTxt.close()

os.system('source /etc/profile')
os.system('sudo cp -r /install/java /')
os.system('cp -r /install/config/crontab /etc/crontab')
os.system('cp -r /install/lecent_prison_fund_sys /var/www/')
os.system('cp -r /install/native /tmp/')
os.chdir('/var/www')
os.system('chown -R www:www .')
os.system('mkdir -p /var/lib/php/session')
os.chdir('/var/lib')
os.system('chown -R www:www php/')

os.system('systemctl start nginx')
os.system('systemctl enable httpd')
os.system('systemctl start httpd')
os.system('cp /install/config/lecent.service /lib/systemd/system/')
os.chdir('/lib/systemd/system/')
os.system('systemctl enable lecent')
os.system('systemctl start lecent')

print('系统部署完毕！')






