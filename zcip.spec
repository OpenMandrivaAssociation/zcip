%define	name	zcip
%define	version	4
%define	release %mkrel 11

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
BuildRequires:	libnet1.0.2-static-devel libpcap-devel glibc-static-devel

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
%make CFLAGS="$RPM_OPT_FLAGS -DSTORAGE_DIR=\\\"%{_localstatedir}/lib/zcip\\\""

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


