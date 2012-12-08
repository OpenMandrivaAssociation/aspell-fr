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
Release:	%mkrel 19
Summary:	%{languageenglazy} files for aspell
Group:		System/Internationalization
Source:		http://aspell.sourceforge.net/aspell-%{languagecode}-%{src_ver}.tar.bz2
URL:		http://aspellfr.free.fr/aspell/
License:	GPL
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Provides: spell-fr

BuildRequires:	aspell >= 0.50
Requires:	aspell >= 0.50

BuildRequires:	locales-fr

# Mandriva Stuff
Requires:	locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:	enchant-dictionary = 1
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




%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.50.3-19mdv2011.0
+ Revision: 662814
- mass rebuild

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.50.3-18mdv2011.0
+ Revision: 603209
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.50.3-17mdv2010.1
+ Revision: 518923
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1:0.50.3-16mdv2010.0
+ Revision: 413066
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1:0.50.3-15mdv2009.1
+ Revision: 350024
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1:0.50.3-14mdv2009.0
+ Revision: 220378
- rebuild

* Sun Mar 09 2008 Anssi Hannula <anssi@mandriva.org> 1:0.50.3-13mdv2008.1
+ Revision: 182430
- provide enchant-dictionary

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1:0.50.3-12mdv2008.1
+ Revision: 148769
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- s/Mandrake/Mandriva/

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.3-11mdv2007.0
+ Revision: 123255
- Import aspell-fr

* Wed Feb 21 2007 Oden Eriksson <oeriksson@mandriva.com> 0.50.3-11mdv2007.1
- use the mkrel macro
- disable debug packages

* Fri Nov 04 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.50.3-10mdk
- fix URL

* Fri Dec 03 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.50.3-9mdk
- rebuild for new aspell

* Wed Jul 28 2004 Pablo Saratxaga <pablo@mandrakesoft.com> 0.50.3-8mdk
- allow build on ia64

