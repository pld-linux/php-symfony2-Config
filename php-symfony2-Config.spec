%define		package	Config
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Config Component
Name:		php-symfony2-Config
Version:	2.7.7
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	677335f97cc8c03a7d35c1053eadba78
URL:		http://symfony.com/doc/2.7/components/config/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php(xml)
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
%setup -q -n config-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Config
%{php_pear_dir}/Symfony/Component/Config/*.php
%{php_pear_dir}/Symfony/Component/Config/Definition
%{php_pear_dir}/Symfony/Component/Config/Exception
%{php_pear_dir}/Symfony/Component/Config/Loader
%{php_pear_dir}/Symfony/Component/Config/Resource
%{php_pear_dir}/Symfony/Component/Config/Util
