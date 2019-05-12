Name:           efitools
Version:        {{ .VERSION }}
Release:        1
Summary:        Tools to manipulate EFI secure boot keys and signatures

Group:          System/Kernel and hardware
BuildArch:      x86_64
License:        GPL
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source0:        efitools-{{ .VERSION }}.tar.gz
Packager:       Greg Szabo <greg@philosobear.com>
Vendor:         CentOS

%description
This package installs a variety of tools for manipulating keys and binary
signatures on UEFI secure boot platforms.
The tools provide access to the keys and certificates stored in the
secure variables of the UEFI firmware, usually in the NVRAM area.

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/usr/bin
install -m 0755 cert-to-efi-hash-list $RPM_BUILD_ROOT/usr/bin/cert-to-efi-hash-list
install -m 0755 cert-to-efi-sig-list $RPM_BUILD_ROOT/usr/bin/cert-to-efi-sig-list
install -m 0755 efi-readvar $RPM_BUILD_ROOT/usr/bin/efi-readvar
install -m 0755 efi-updatevar $RPM_BUILD_ROOT/usr/bin/efi-updatevar
install -m 0755 efitool-mkusb $RPM_BUILD_ROOT/usr/bin/efitool-mkusb
install -m 0755 flash-var $RPM_BUILD_ROOT/usr/bin/flash-var
install -m 0755 hash-to-efi-sig-list $RPM_BUILD_ROOT/usr/bin/hash-to-efi-sig-list
install -m 0755 sig-list-to-certs $RPM_BUILD_ROOT/usr/bin/sig-list-to-certs
install -m 0755 sign-efi-sig-list $RPM_BUILD_ROOT/usr/bin/sign-efi-sig-list
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/doc/efitools
install -m 0644 COPYING $RPM_BUILD_ROOT/usr/share/doc/efitools/COPYING
install -m 0644 README $RPM_BUILD_ROOT/usr/share/doc/efitools/README
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/efitools/efi
install -m 0644 HashTool.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/HashTool.efi
install -m 0644 HelloWorld.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/HelloWorld.efi
install -m 0644 KeyTool.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/KeyTool.efi
install -m 0644 Loader.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/Loader.efi
install -m 0644 LockDown.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/LockDown.efi
install -m 0644 ReadVars.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/ReadVars.efi
install -m 0644 SetNull.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/SetNull.efi
install -m 0644 ShimReplace.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/ShimReplace.efi
install -m 0644 UpdateVars.efi $RPM_BUILD_ROOT/usr/share/efitools/efi/UpdateVars.efi
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/man/man1
install -m 0644 cert-to-efi-hash-list.1 $RPM_BUILD_ROOT/usr/share/man/man1/cert-to-efi-hash-list.1
install -m 0644 cert-to-efi-sig-list.1 $RPM_BUILD_ROOT/usr/share/man/man1/cert-to-efi-sig-list.1
install -m 0644 efi-readvar.1 $RPM_BUILD_ROOT/usr/share/man/man1/efi-readvar.1
install -m 0644 efi-updatevar.1 $RPM_BUILD_ROOT/usr/share/man/man1/efi-updatevar.1
install -m 0644 hash-to-efi-sig-list.1 $RPM_BUILD_ROOT/usr/share/man/man1/hash-to-efi-sig-list.1
install -m 0644 sig-list-to-certs.1 $RPM_BUILD_ROOT/usr/share/man/man1/sig-list-to-certs.1
install -m 0644 sign-efi-sig-list.1 $RPM_BUILD_ROOT/usr/share/man/man1/sign-efi-sig-list.1

%files
/usr/bin/cert-to-efi-hash-list
/usr/bin/cert-to-efi-sig-list
/usr/bin/efi-readvar
/usr/bin/efi-updatevar
/usr/bin/efitool-mkusb
/usr/bin/flash-var
/usr/bin/hash-to-efi-sig-list
/usr/bin/sig-list-to-certs
/usr/bin/sign-efi-sig-list
/usr/share/doc/efitools
/usr/share/doc/efitools/COPYING
/usr/share/doc/efitools/README
/usr/share/efitools
/usr/share/efitools/efi
/usr/share/efitools/efi/HashTool.efi
/usr/share/efitools/efi/HelloWorld.efi
/usr/share/efitools/efi/KeyTool.efi
/usr/share/efitools/efi/Loader.efi
/usr/share/efitools/efi/LockDown.efi
/usr/share/efitools/efi/ReadVars.efi
/usr/share/efitools/efi/SetNull.efi
/usr/share/efitools/efi/ShimReplace.efi
/usr/share/efitools/efi/UpdateVars.efi
/usr/share/man/man1/cert-to-efi-hash-list.1.gz
/usr/share/man/man1/cert-to-efi-sig-list.1.gz
/usr/share/man/man1/efi-readvar.1.gz
/usr/share/man/man1/efi-updatevar.1.gz
/usr/share/man/man1/hash-to-efi-sig-list.1.gz
/usr/share/man/man1/sig-list-to-certs.1.gz
/usr/share/man/man1/sign-efi-sig-list.1.gz

%changelog
* Sun May 12 2019 Greg Szabo  {{ .VERSION }}
  - CentOS RPM release
