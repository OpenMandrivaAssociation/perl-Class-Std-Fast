%define upstream_name    Class-Std-Fast
%define upstream_version v0.0.8

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:    faster but less secure than Class::Std
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Std)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(version)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

Requires: perl(Class::Std)
Requires: perl(version)

%description
Class::Std::Fast allows you to use the beautiful API of Class::Std in a
faster way than Class::Std does.

You can get the object's ident via scalarifiyng your object.

Getting the objects ident is still possible via the ident method, but it's
faster to scalarify your object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
