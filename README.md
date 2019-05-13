[![CircleCI](https://circleci.com/gh/freshautomations/efitools-centos/tree/master.svg?style=svg)](https://circleci.com/gh/freshautomations/efitools-centos/tree/master)
# EFITools for CentOS

## What is EFI Tools?
EFI Tools is a set of applications to manage UEFI Secure Boot under Linux.

## Problem description
* EFI Tools was not packaged for CentOS / Red Hat.
* The RPM/DEB packages available depend on an old OpenSSL version, hence they cannot run on CentOS 7.

## Proposed solution
This repository builds EFITools against the latest CentOS release. This keeps EFITools up-to-date and packaged for
CentOS / RedHat.

The build process takes the latest commit on the `master` branch from the kernel Git repos to build the `sbsigntools` and `efitools` packages.

## Todo and ToFix
* Instead of pulling `master`, the build process should build the latest tagged release. Until this is done, the package
should not be considered for production use.
* The RPM binaries should be signed using a GPG key. (This is in the works.)
* A package repository should be set up.
