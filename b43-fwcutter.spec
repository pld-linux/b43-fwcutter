Summary:	Utility for extracting Broadcom 43xx firmware
Summary(hu.UTF-8):	Eszköz a Broadcom 43xx firmware-ek kinyerésére
Summary(pl.UTF-8):	Narzędzie do wyciągania firmware'u dla układów Broadcom 43xx
Name:		b43-fwcutter
Version:	012
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://bu3sch.de/b43/fwcutter/%{name}-%{version}.tar.bz2
# Source0-md5:	69eadf67b459f313a8d6b37aaabef96c
URL:		http://linuxwireless.org/en/users/Drivers/b43#devicefirmware
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fwcutter is a tool which can extract firmware from various source
files. It's written for (new) b43 and b43legacy drivers.

%description -l hu.UTF-8
fwcutter egy eszköz, amellyel firmware-eket nyerhetsz ki különféle
fájlkokból. Ez az (új) b43 és b43legacy meghajtókhoz készült.

%description -l pl.UTF-8
fwcutter to narzędzie potrafiące wyciągać firmware z różnych plików
źródłowych. To narzędzie zostało napisane dla (nowych) sterowników b43
oraz b43legacy.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_BSD_SOURCE"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install b43-fwcutter $RPM_BUILD_ROOT%{_bindir}
install b43-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/b43-fwcutter
%{_mandir}/man1/b43-fwcutter.1*
