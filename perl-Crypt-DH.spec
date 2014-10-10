%define upstream_name	 Crypt-DH
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Diffie-Hellman key exchange system
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::Random)
BuildArch:	noarch

%description 
Crypt::DH is a Perl implementation of the Diffie-Hellman key exchange system.
Diffie-Hellman is an algorithm by which two parties can agree on a shared
secret key, known only to them. The secret is negotiated over an insecure
network without the two parties ever passing the actual shared secret, or
their private keys, between them.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 680850
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 406922
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.06-3mdv2009.0
+ Revision: 256257
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.06-1mdv2008.1
+ Revision: 131417
- kill re-definition of %%buildroot on Pixel's request


* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- New release 0.06
- spec cleanup
- make test in %%check
- fix directory ownership

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.03-1mdk
- New package

