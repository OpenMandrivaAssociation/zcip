%define	name	zcip
%define	version	4
%define	release %mkrel 13

Summary:	Ad-hoc link-local IP autoconfiguration
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		zcip-4-alias.patch
Patch1:		zcip-4-gcc3.patch
Patch2:     zcip-4-help.patch 
Patch3:     zcip-4-format_string.patch
License:	MIT
Group:		System/Configuration/Networking
URL:		http://zeroconf.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}buildroot
BuildRequires: net1.0-devel
BuildRequires: libpcap-devel

%description
This is an implementation of the ad-hoc link-local IP autoconfiguration
algorithm described in the IETF Draft "Dynamic Configuration of IPv4
link-local addresses".

%prep
%setup -q
%patch0 -p1 -b .alias
%patch1 -p1 -b .gcc3
%patch2 -p0
%patch3 -p0

%build
%make CFLAGS="%optflags -DSTORAGE_DIR=\\\"%{_localstatedir}/lib/zcip\\\"" LDFLAGS="%ldflags"

%install
rm -rf $RPM_BUILD_ROOT
install -m755 zcip -D %{buildroot}/sbin/zcip
install -m644 zcip.8 -D %{buildroot}%{_mandir}/man8/zcip.8
mkdir -p %{buildroot}%{_localstatedir}/lib/zcip

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README draft-ietf-zeroconf-ipv4-linklocal-07.txt Changelog Copyright TODO
/sbin/*
%{_mandir}/man8/*
%{_localstatedir}/lib/zcip




%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 4-13mdv2011.0
+ Revision: 671953
- mass rebuild

* Sat Dec 04 2010 Funda Wang <fwang@mandriva.org> 4-12mdv2011.0
+ Revision: 609503
- do not build statically

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 4-11mdv2010.1
+ Revision: 520292
- rebuilt for 2010.1

* Sat Mar 07 2009 Michael Scherer <misc@mandriva.org> 4-10mdv2009.1
+ Revision: 350877
- fix build, add patch 4 to correct format string error

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Mon Jun 02 2008 Pixel <pixel@mandriva.com> 4-9mdv2009.0
+ Revision: 214231
- adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Mon Feb 11 2008 Michael Scherer <misc@mandriva.org> 4-9mdv2008.1
+ Revision: 165111
- fix --help output, patch2, closes bug #33886

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 4-8mdv2008.1
+ Revision: 130708
- kill re-definition of %%buildroot on Pixel's request


* Tue Oct 31 2006 Michael Scherer <misc@mandriva.org> 4-8mdv2007.0
+ Revision: 74725
- Bump release
- Bunzip patch
- Import zcip

