#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Nagios
%define		pnam	Plugin-WWW-Mechanize
Summary:	Login to a web page as a user and get data as a Nagios plugin
Name:		perl-Nagios-Plugin-WWW-Mechanize
Version:	0.12
Release:	1
# same as Perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Nagios/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	480e8929fabae667f6783a22012e7922
URL:		http://search.cpan.org/dist/Nagios-Plugin-WWW-Mechanize/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Nagios-Plugin
BuildRequires:	perl-WWW-Mechanize
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module ties Nagios::Plugin with WWW::Mechanize so that there's
less code in your Perl script and the most common work is done for
you.

For example, the plugin will automatically call nagios_exit(CRITICAL,
...) if a page is unavailable or a submit_form fails. The plugin will
also keep a track of the time for responses from the remote web server
and output that as performance data.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Nagios/Plugin/WWW
%{perl_vendorlib}/Nagios/Plugin/WWW/Mechanize.pm
%{_mandir}/man3/*
