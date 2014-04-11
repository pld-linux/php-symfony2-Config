%define		pearname	Config
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Config Component
Name:		php-symfony2-Config
Version:	2.4.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	7bb503daab06e47a18969796e1024e3b
URL:		http://symfony.com/doc/current/components/config/index.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
Requires:	php-symfony2-Filesystem >= 2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Config Component provides several classes to help you find, load,
combine, autofill and validate configuration values of any kind,
whatever their source may be (Yaml, XML, INI files, or for instance a
database).

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/Config
%{php_pear_dir}/Symfony/Component/Config/*.php
%{php_pear_dir}/Symfony/Component/Config/Definition
%{php_pear_dir}/Symfony/Component/Config/Exception
%{php_pear_dir}/Symfony/Component/Config/Loader
%{php_pear_dir}/Symfony/Component/Config/Resource
%{php_pear_dir}/Symfony/Component/Config/Util
