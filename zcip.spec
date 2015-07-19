Summary:	Ad-hoc link-local IP autoconfiguration
Name:		zcip
Version:	4
Release:	22
License:	MIT
Group:		System/Configuration/Networking
Url:		http://zeroconf.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		zcip-4-alias.patch
Patch1:		zcip-4-gcc3.patch
Patch2:		zcip-4-help.patch 
Patch3:		zcip-4-format_string.patch
BuildRequires:	libpcap-devel
BuildRequires:	net1.0.2-devel

%description
This is an implementation of the ad-hoc link-local IP autoconfiguration
algorithm described in the IETF Draft "Dynamic Configuration of IPv4
link-local addresses".

%prep
%setup -q
%apply_patches

%build
%make CFLAGS="%optflags -DSTORAGE_DIR=\\\"%{_localstatedir}/lib/zcip\\\"" LDFLAGS="%ldflags"

%install
install -m755 zcip -D %{buildroot}/sbin/zcip
install -m644 zcip.8 -D %{buildroot}%{_mandir}/man8/zcip.8
mkdir -p %{buildroot}%{_localstatedir}/lib/zcip

%files
%doc README draft-ietf-zeroconf-ipv4-linklocal-07.txt Changelog Copyright TODO
/sbin/*
%{_mandir}/man8/*
%{_localstatedir}/lib/zcip

