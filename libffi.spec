#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libffi
Version  : 3.2.1
Release  : 27
URL      : ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
Source0  : ftp://sourceware.org/pub/libffi/libffi-3.2.1.tar.gz
Summary  : Library supporting Foreign Function Interfaces
Group    : Development/Tools
License  : MIT
Requires: libffi-lib
Requires: libffi-doc
BuildRequires : autogen
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : tcl

%description
Status
======
libffi-3.2.1 was released on November 12, 2014.  Check the libffi web
page for updates: <URL:http://sourceware.org/libffi/>.

%package dev
Summary: dev components for the libffi package.
Group: Development
Requires: libffi-lib
Provides: libffi-devel

%description dev
dev components for the libffi package.


%package dev32
Summary: dev32 components for the libffi package.
Group: Default
Requires: libffi-lib32

%description dev32
dev32 components for the libffi package.


%package doc
Summary: doc components for the libffi package.
Group: Documentation

%description doc
doc components for the libffi package.


%package lib
Summary: lib components for the libffi package.
Group: Libraries

%description lib
lib components for the libffi package.


%package lib32
Summary: lib32 components for the libffi package.
Group: Default

%description lib32
lib32 components for the libffi package.


%prep
%setup -q -n libffi-3.2.1
pushd ..
cp -a libffi-3.2.1 build32
popd

%build
export LANG=C
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib32/libffi-3.2.1/include/ffi.h
/usr/lib32/libffi-3.2.1/include/ffitarget.h
/usr/lib64/libffi-3.2.1/include/ffi.h
/usr/lib64/libffi-3.2.1/include/ffitarget.h
/usr/lib64/libffi.so
/usr/lib64/pkgconfig/libffi.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libffi.so
/usr/lib32/pkgconfig/32libffi.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libffi.so.6
/usr/lib64/libffi.so.6.0.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libffi.so.6
/usr/lib32/libffi.so.6.0.4
