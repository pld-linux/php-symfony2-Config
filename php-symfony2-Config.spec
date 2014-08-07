%define		pearname	Config
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Config Component
Name:		php-symfony2-Config
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	f5f9256083fc86629063647eeb25eb96
URL:		http://symfony.com/doc/2.4/components/config/index.html
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
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoloader.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests

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
