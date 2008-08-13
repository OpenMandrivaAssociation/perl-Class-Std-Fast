%define module   Class-Std-Fast
%define version  0.0.8
%define release  %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    faster but less secure than Class::Std
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Class/%{module}-v%{version}.tar.gz
Requires: perl-version
Requires: perl(Class::Std)
BuildRequires: perl(Class::Std)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-version
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Class::Std::Fast allows you to use the beautiful API of Class::Std in a
faster way than Class::Std does.

You can get the object's ident via scalarifiyng your object.

Getting the objects ident is still possible via the ident method, but it's
faster to scalarify your object.

%prep
%setup -q -n %{module}-v%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


