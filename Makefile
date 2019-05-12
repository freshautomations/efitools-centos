
# These targets build on each other. They are separated for easier readability.

all: prepare-env build-sbsigntools build-efitools rpm-sbsigntools rpm-efitools

prepare-env:
		yum update -y
		yum install -y wget gcc automake binutils-devel openssl openssl-devel libuuid-devel gnu-efi-devel help2man perl-File-Slurp rpm-build rpmdevtools
		wget https://github.com/freshautomations/stemplate/releases/download/v0.3.0/stemplate_linux_amd64 -O /usr/local/bin/stemplate
		chmod +x /usr/local/bin/stemplate

build-sbsigntools:
		git clone git://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
		cd sbsigntools && ./autogen.sh
		cd sbsigntools && ./configure
		$(MAKE) -C sbsigntools
		$(MAKE) -C sbsigntools install
		cd sbsigntools && git tag | sort -V | tail -1 > sbsigntools-version

# Needs build-sbisgntool's last line: make install
build-efitools:
		git clone git://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
		make -C efitools
		mv efitools/mkusb.sh efitools/efitool-mkusb
		cd efitools && git tag | sort -V | tail -1 > efitools-version

rpm-sbsigntools:
		rpmdev-setuptree
		name=sbsigntools stemplate rpmmacros -o ${HOME}/.rpmmacros --string name
		mkdir "${HOME}"/rpmbuild/SOURCES/sbsigntools
		cd sbsigntools/src && cp sbattach sbkeysync sbsiglist sbsign sbvarsign sbverify "${HOME}/rpmbuild/SOURCES/sbsigntools"
		cd sbsigntools/docs && cp sbattach.1 sbsiglist.1 sbsign.1 sbvarsign.1 sbverify.1 "${HOME}"/rpmbuild/SOURCES/sbsigntools
		cd sbsigntools && cp COPYING "${HOME}/rpmbuild/SOURCES/sbsigntools"
		mv "${HOME}"/rpmbuild/SOURCES/sbsigntools "${HOME}"/rpmbuild/SOURCES/sbsigntools-"`cat sbsigntools/sbsigntools-version`"
		tar -czf "${HOME}"/rpmbuild/SOURCES/sbsigntools-"`cat sbsigntools/sbsigntools-version`".tar.gz -C "${HOME}"/rpmbuild/SOURCES sbsigntools-"`cat sbsigntools/sbsigntools-version`"
		VERSION="`cat sbsigntools/sbsigntools-version`" stemplate sbsigntools.spec -o "${HOME}"/rpmbuild/SPECS --string VERSION
		cd "${HOME}"/rpmbuild && rpmbuild -ba SPECS/sbsigntools.spec

rpm-efitools:
		rpmdev-setuptree
		name=efitools stemplate rpmmacros -o ${HOME}/.rpmmacros --string name
		mkdir "${HOME}"/rpmbuild/SOURCES/efitools
		cd efitools && cp HashTool.efi HelloWorld.efi KeyTool.efi Loader.efi LockDown.efi ReadVars.efi SetNull.efi ShimReplace.efi UpdateVars.efi COPYING README cert-to-efi-hash-list cert-to-efi-sig-list efi-readvar efi-updatevar efitool-mkusb flash-var hash-to-efi-sig-list sig-list-to-certs sign-efi-sig-list "${HOME}/rpmbuild/SOURCES/efitools"
		cd efitools/doc && cp cert-to-efi-hash-list.1 cert-to-efi-sig-list.1 efi-readvar.1 efi-updatevar.1 hash-to-efi-sig-list.1 sig-list-to-certs.1 sign-efi-sig-list.1 "${HOME}"/rpmbuild/SOURCES/efitools
		mv "${HOME}"/rpmbuild/SOURCES/efitools "${HOME}"/rpmbuild/SOURCES/efitools-"`cat efitools/efitools-version`"
		tar -czf "${HOME}"/rpmbuild/SOURCES/efitools-"`cat efitools/efitools-version`".tar.gz -C "${HOME}"/rpmbuild/SOURCES efitools-"`cat efitools/efitools-version`"
		VERSION="`cat efitools/efitools-version`" stemplate efitools.spec -o "${HOME}"/rpmbuild/SPECS --string VERSION
		cd "${HOME}"/rpmbuild && rpmbuild -ba SPECS/efitools.spec

release:
		bash .circleci/release.bash ${HOME}/rpmbuild/RPMS/x86_64/sbsigntools-"`cat sbsigntools/sbsigntools-version`"-1.x86_64.rpm ${HOME}/rpmbuild/RPMS/x86_64/efitools-"`cat efitools/efitools-version`"-1.x86_64.rpm

clean:
		rm -rf efitools sbsigntools ${HOME}/rpmbuild
