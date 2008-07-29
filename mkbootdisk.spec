%define name	mkbootdisk
%define version 1.5.3
%define release %mkrel 4

Summary: 	Creates an initial ramdisk image for preloading modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		System/Kernel and hardware
Source: 	%{name}-%{version}.tar.bz2
URL:		http://www.redhat.com/swr/src/mkbootdisk-1.4.2-1.src.html
Patch0: 	mkbootdisk-1.5.3-mdk.patch
Patch1: 	mkbootdisk-1.5.1-devfs-compliant.patch
ExclusiveArch: 	sparc sparc64 %{ix86} x86_64 amd64
ExclusiveOs: 	Linux
Requires: 	mkinitrd /bin/awk dosfstools mktemp
Conflicts:	modutils < 2.3.11-5
%ifarch %ix86 x86_64 amd64
Requires:	syslinux >= 1.76-2mdk
%endif
%ifarch sparc sparc64
Requires: 	silo genromfs
%endif
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root

%description
The mkbootdisk program creates a standalone boot floppy disk for booting
the running system.  The created boot disk will look for the root
filesystem on the device mentioned in /etc/fstab and includes an
initial ramdisk image which will load any necessary SCSI modules for
the system.

%prep
%setup -q
%patch0 -p1 -b .mdk
%patch1 -p1 -b .devfs

%install
rm -rf $RPM_BUILD_ROOT
%make BUILDROOT=$RPM_BUILD_ROOT mandir=%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root) /sbin/mkbootdisk
%attr(644,root,root) %{_mandir}/man8/mkbootdisk.8*
