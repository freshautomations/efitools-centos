Name:           sbsigntools
Version:        {{ .VERSION }}
Release:        1
Summary:        CentOS EFI binary signing tools

Group:          System/Kernel and hardware
BuildArch:      x86_64
License:        GPLv3
URL:            https://git.kernel.org/cgit/linux/kernel/git/jejb/sbsigntools.git
Source0:        sbsigntools-{{ .VERSION }}.tar.gz
Packager:       Greg Szabo <greg@philosobear.com>
Vendor:         CentOS

%description
This package installs tools which can cryptographically sign EFI
binaries and drivers.

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 sbattach $RPM_BUILD_ROOT/usr/bin/sbattach
install -m 0755 sbkeysync $RPM_BUILD_ROOT/usr/bin/sbkeysync
install -m 0755 sbsiglist $RPM_BUILD_ROOT/usr/bin/sbsiglist
install -m 0755 sbsign $RPM_BUILD_ROOT/usr/bin/sbsign
install -m 0755 sbvarsign $RPM_BUILD_ROOT/usr/bin/sbvarsign
install -m 0755 sbverify $RPM_BUILD_ROOT/usr/bin/sbverify
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/doc/sbsigntools
install -m 0644 COPYING $RPM_BUILD_ROOT/usr/share/doc/sbsigntools/COPYING
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/man/man1
install -m 0644 sbattach.1 $RPM_BUILD_ROOT/usr/share/man/man1/sbattach.1
install -m 0644 sbsiglist.1 $RPM_BUILD_ROOT/usr/share/man/man1/sbsiglist.1
install -m 0644 sbsign.1 $RPM_BUILD_ROOT/usr/share/man/man1/sbsign.1
install -m 0644 sbvarsign.1 $RPM_BUILD_ROOT/usr/share/man/man1/sbvarsign.1
install -m 0644 sbverify.1 $RPM_BUILD_ROOT/usr/share/man/man1/sbverify.1

%files
/usr/bin/sbattach
/usr/bin/sbkeysync
/usr/bin/sbsiglist
/usr/bin/sbsign
/usr/bin/sbvarsign
/usr/bin/sbverify
/usr/share/doc/sbsigntools
/usr/share/doc/sbsigntools/COPYING
/usr/share/man/man1/sbattach.1.gz
/usr/share/man/man1/sbsiglist.1.gz
/usr/share/man/man1/sbsign.1.gz
/usr/share/man/man1/sbvarsign.1.gz
/usr/share/man/man1/sbverify.1.gz

%changelog
* Sun May 12 2019 Greg Szabo  {{ .VERSION }}
  - Initial CentOS RPM release
