%define module	Crypt-DH
%define name	perl-%{module}
%define version 0.06
%define release	%mkrel 1

Name: 		%{name}
Version: 	%{version}
Release:	%{release}
Summary:        Diffie-Hellman key exchange system
License:        GPL or Artistic
Group:          Development/Perl
Source0:        http://search.cpan.org/CPAN/authors/id/B/BT/BTROTT/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}
BuildRequires:  perl-devel
BuildRequires:  perl-Crypt-Random
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description 
Crypt::DH is a Perl implementation of the Diffie-Hellman key exchange system.
Diffie-Hellman is an algorithm by which two parties can agree on a shared
secret key, known only to them. The secret is negotiated over an insecure
network without the two parties ever passing the actual shared secret, or
their private keys, between them.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*

