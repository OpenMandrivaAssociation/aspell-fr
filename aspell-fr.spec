%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

# WARNING
# To build this package, you must set LC_ALL to fr
# example :	LC_ALL=fr rpm -ba aspell-fr.spec

%define src_ver 0.50-3
%define languagelocal francais
%define languageeng french
%define languageenglazy French
%define languagecode fr
%define lc_ctype fr_FR

Summary:	%{languageenglazy} files for aspell
Name:		aspell-%{languagecode}
Epoch:		1
Version:	0.50.3
Release:	27
Group:		System/Internationalization
License:	GPLv2
Url:		http://aspellfr.free.fr/aspell/
Source0:	http://aspell.sourceforge.net/aspell-%{languagecode}-%{src_ver}.tar.bz2

BuildRequires:	aspell >= 0.50
BuildRequires:	locales-fr
Requires:	aspell >= 0.50
# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
Provides:	aspell-dictionary
Provides:	spell-fr
Autoreqprov:	no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -qn %{name}-%{src_ver}

%build
export LC_ALL=fr
./configure
%make

%install
export LC_ALL=fr
%makeinstall_std

# fix doc perms
chmod 644 README COPYING

%files
%doc README COPYING
%{_libdir}/aspell-*/*

