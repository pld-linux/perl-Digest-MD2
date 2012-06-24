#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	MD2
Summary:	Digest::MD2 - MD2 digest algorithm implementation
Summary(pl):	Digest::MD2 - implementacja algorytmu skr�tu MD2
Name:		perl-Digest-MD2
Version:	2.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	feecf9faa1b0a499a48fce214a309a78
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digest::MD2 module allows you to use the RSA Data Security Inc.
MD2 Message Digest algorithm from within Perl programs. The algorithm
takes as input a message of arbitrary length and produces as output a
128-bit "fingerprint" or "message digest" of the input. The algorithm
is described in RFC 1319.

%description -l pl
Modu� Digest::MD2 pozwala na u�ywanie algorytmu skr�tu MD2 firmy RSA
Data Security Inc. w programach perlowych. Algorytm przyjmuje na
wej�ciu tekst o dowolnej d�ugo�ci, a produkuje na wyj�ciu 128-bitowy
"odcisk palca" lub "skr�t" informacji wej�ciowej. Algorytm jest
opisany w RFC 1319.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Digest/MD2.pm
%dir %{perl_vendorarch}/auto/Digest/MD2
%{perl_vendorarch}/auto/Digest/MD2/MD2.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/MD2/MD2.so
%{_mandir}/man3/*
