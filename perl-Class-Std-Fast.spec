%define upstream_name    Class-Std-Fast
%define upstream_version v0.0.8

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Faster but less secure than Class::Std
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Std)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)

BuildArch:	noarch

Requires:	perl(Class::Std)
Requires:	perl(version)

%description
Class::Std::Fast allows you to use the beautiful API of Class::Std in a
faster way than Class::Std does.

You can get the object's ident via scalarifiyng your object.

Getting the objects ident is still possible via the ident method, but it's
faster to scalarify your object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.0.8-5mdv2011.0
+ Revision: 654896
- rebuild for updated spec-helper

* Sun Feb 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.0.8-4mdv2011.0
+ Revision: 505698
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.8-3mdv2010.0
+ Revision: 430334
- rebuild

* Wed Aug 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.0.8-2mdv2009.0
+ Revision: 271528
- fix dependencies
- fix version

* Wed Aug 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> v0.0.8-1mdv2009.0
+ Revision: 271303
- import perl-Class-Std-Fast


* Wed Aug 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> v0.0.8-1mdv2009.0
- initial mdv release, generated with cpan2dist

