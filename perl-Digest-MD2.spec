%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	MD2
Summary:	Digest::MD2 Perl module - MD2 digest algorithm implementation
Summary(pl):	Modu³ perla Digest::MD2 - implementacja algorytmu skrótu MD2
Name:		perl-Digest-MD2
Version:	2.00
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::MD2 module allows you to use the RSA Data Security Inc.
MD2 Message Digest algorithm from within Perl programs. The algorithm
takes as input a message of arbitrary length and produces as output a
128-bit "fingerprint" or "message digest" of the input. The algorithm
is described in RFC 1319.

%description -l pl
Modu³ Digest::MD2 pozwala na u¿ywanie algorytmu skrótu MD2 firmy RSA
Data Security Inc. w programach perlowych. Algorytm przyjmuje na
wej¶ciu tekst o dowolnej d³ugo¶ci, a produkuje na wyj¶ciu 128-bitowy
"odcisk palca" lub "skrót" informacji wej¶ciowej. Algorytm jest
opisany w RFC 1319.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Digest/MD2.pm
%dir %{perl_sitearch}/auto/Digest/MD2
%{perl_sitearch}/auto/Digest/MD2/MD2.bs
%attr(755,root,root) %{perl_sitearch}/auto/Digest/MD2/MD2.so
%{_mandir}/man3/*
