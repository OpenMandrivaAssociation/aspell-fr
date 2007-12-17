%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# WARNING
# To build this package, you must set LC_ALL to fr
# example : LC_ALL=fr rpm -ba aspell-fr.spec

%define src_ver 0.50-3
%define languagelocal francais
%define languageeng french
%define languageenglazy French
%define languagecode fr
%define lc_ctype fr_FR

Name:		aspell-%{languagecode}
Version:	0.50.3
Release:	%mkrel 11
Summary:	%{languageenglazy} files for aspell
Group:		System/Internationalization
Source:		http://aspell.sourceforge.net/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		http://aspellfr.free.fr/aspell/
License:	GPL
Epoch:		1
Provides: spell-fr

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50

BuildRequires:	locales-fr

# Mandriva Stuff
Requires:	locales-%{languagecode}
Provides:	aspell-dictionary

# RedHat Stuff. is this right:
#Obsoletes: ispell-fr, ispell-french

Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{name}-%{src_ver}

%build
export LC_ALL=fr
./configure
%make

%install
rm -fr $RPM_BUILD_ROOT
export LC_ALL=fr
%makeinstall_std

# fix doc perms
chmod 644 README COPYING

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING
%{_libdir}/aspell-*/*


