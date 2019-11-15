#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6
#
Name     : libksba
Version  : 1.3.5
Release  : 14
URL      : https://gnupg.org/ftp/gcrypt/libksba/libksba-1.3.5.tar.bz2
Source0  : https://gnupg.org/ftp/gcrypt/libksba/libksba-1.3.5.tar.bz2
Source1 : https://gnupg.org/ftp/gcrypt/libksba/libksba-1.3.5.tar.bz2.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-3.0
Requires: libksba-bin = %{version}-%{release}
Requires: libksba-info = %{version}-%{release}
Requires: libksba-lib = %{version}-%{release}
Requires: libksba-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : valgrind

%description
LIBKSBA
---------
2012, 2013, 2014, 2015  g10 Code GmbH
This file is free software; as a special exception the author gives
unlimited permission to copy and/or distribute it, with or without
modifications, as long as this notice is preserved.

%package bin
Summary: bin components for the libksba package.
Group: Binaries
Requires: libksba-license = %{version}-%{release}

%description bin
bin components for the libksba package.


%package dev
Summary: dev components for the libksba package.
Group: Development
Requires: libksba-lib = %{version}-%{release}
Requires: libksba-bin = %{version}-%{release}
Provides: libksba-devel = %{version}-%{release}
Requires: libksba = %{version}-%{release}

%description dev
dev components for the libksba package.


%package info
Summary: info components for the libksba package.
Group: Default

%description info
info components for the libksba package.


%package lib
Summary: lib components for the libksba package.
Group: Libraries
Requires: libksba-license = %{version}-%{release}

%description lib
lib components for the libksba package.


%package license
Summary: license components for the libksba package.
Group: Default

%description license
license components for the libksba package.


%prep
%setup -q -n libksba-1.3.5
cd %{_builddir}/libksba-1.3.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573789789
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1573789789
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libksba
cp %{_builddir}/libksba-1.3.5/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/libksba/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libksba-1.3.5/COPYING.GPLv3 %{buildroot}/usr/share/package-licenses/libksba/e31db874e5b375f0592b02e3e450c9e94086e661
cp %{_builddir}/libksba-1.3.5/COPYING.LGPLv3 %{buildroot}/usr/share/package-licenses/libksba/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ksba-config

%files dev
%defattr(-,root,root,-)
/usr/include/ksba.h
/usr/lib64/libksba.so
/usr/share/aclocal/*.m4

%files info
%defattr(0644,root,root,0755)
/usr/share/info/ksba.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libksba.so.8
/usr/lib64/libksba.so.8.11.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libksba/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libksba/e31db874e5b375f0592b02e3e450c9e94086e661
/usr/share/package-licenses/libksba/f45ee1c765646813b442ca58de72e20a64a7ddba
