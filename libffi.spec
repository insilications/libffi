#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libffi
Version  : 3.2.1
Release  : 38
URL      : https://github.com/libffi/libffi/archive/v3.2.1/libffi-3.2.1.tar.gz
Source0  : https://github.com/libffi/libffi/archive/v3.2.1/libffi-3.2.1.tar.gz
Summary  : Library supporting Foreign Function Interfaces
Group    : Development/Tools
License  : LGPL-2.0+
Requires: libffi-info = %{version}-%{release}
Requires: libffi-lib = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : tcl
BuildRequires : texinfo
Patch1: 0001-Fix-.m4-files.patch

%description
Status
======
libffi-3.2.1 was released on November 12, 2014.  Check the libffi web
page for updates: <URL:http://sourceware.org/libffi/>.

%package dev
Summary: dev components for the libffi package.
Group: Development
Requires: libffi-lib = %{version}-%{release}
Provides: libffi-devel = %{version}-%{release}
Requires: libffi = %{version}-%{release}
Requires: libffi-dev = %{version}-%{release}
Requires: libffi-dev32 = %{version}-%{release}

%description dev
dev components for the libffi package.


%package dev32
Summary: dev32 components for the libffi package.
Group: Default
Requires: libffi-lib32 = %{version}-%{release}
Requires: libffi-dev = %{version}-%{release}
Requires: libffi-dev32 = %{version}-%{release}

%description dev32
dev32 components for the libffi package.


%package info
Summary: info components for the libffi package.
Group: Default

%description info
info components for the libffi package.


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


%package staticdev
Summary: staticdev components for the libffi package.
Group: Default
Requires: libffi-dev = %{version}-%{release}
Requires: libffi-dev32 = %{version}-%{release}

%description staticdev
staticdev components for the libffi package.


%package staticdev32
Summary: staticdev32 components for the libffi package.
Group: Default
Requires: libffi-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the libffi package.


%prep
%setup -q -n libffi-3.2.1
cd %{_builddir}/libffi-3.2.1
%patch1 -p1
pushd ..
cp -a libffi-3.2.1 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610405288
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
#
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -fvisibility-inlines-hidden -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
%global _lto_cflags 1
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%autogen --enable-shared --enable-static --disable-docs --enable-portable-binary --without-gcc-arch
make  %{?_smp_mflags}  V=1 VERBOSE=1

make VERBOSE=1 V=1 %{?_smp_mflags} check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%autogen  --enable-shared --enable-static --disable-docs --enable-portable-binary --without-gcc-arch
make  %{?_smp_mflags}  V=1 VERBOSE=1

pushd ../build32/
## altflags1_32 content
export CFLAGS="-O3 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native -fexceptions -fomit-frame-pointer -fstrict-aliasing -ffast-math"
export CXXFLAGS="-O3 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native -fexceptions -fomit-frame-pointer -fstrict-aliasing -ffast-math"
export LDFLAGS="-O3 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native -fexceptions -fomit-frame-pointer -fstrict-aliasing -ffast-math"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#
## altflags1_32 end
%autogen  --enable-shared --enable-static --disable-docs --enable-portable-binary --without-gcc-arch  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1610405288
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
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
/usr/share/man/man3/ffi.3
/usr/share/man/man3/ffi_call.3
/usr/share/man/man3/ffi_prep_cif.3
/usr/share/man/man3/ffi_prep_cif_var.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libffi.so
/usr/lib32/pkgconfig/32libffi.pc
/usr/lib32/pkgconfig/libffi.pc

%files info
%defattr(0644,root,root,0755)
/usr/share/info/libffi.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libffi.so.6
/usr/lib64/libffi.so.6.0.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libffi.so.6
/usr/lib32/libffi.so.6.0.4

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libffi.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libffi.a
