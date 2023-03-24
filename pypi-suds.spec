#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-suds
Version  : 1.1.2
Release  : 1
URL      : https://files.pythonhosted.org/packages/35/e5/d9571b3f8757573ba0fd1ad56c20ca24c1f339db8731914fee6f657b7170/suds-1.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/35/e5/d9571b3f8757573ba0fd1ad56c20ca24c1f339db8731914fee6f657b7170/suds-1.1.2.tar.gz
Summary  : Lightweight SOAP client (community fork)
Group    : Development/Tools
License  : LGPL-3.0
Requires: pypi-suds-license = %{version}-%{release}
Requires: pypi-suds-python = %{version}-%{release}
Requires: pypi-suds-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![Build Status](https://github.com/suds-community/suds/workflows/Test/badge.svg?branch=master)

%package license
Summary: license components for the pypi-suds package.
Group: Default

%description license
license components for the pypi-suds package.


%package python
Summary: python components for the pypi-suds package.
Group: Default
Requires: pypi-suds-python3 = %{version}-%{release}

%description python
python components for the pypi-suds package.


%package python3
Summary: python3 components for the pypi-suds package.
Group: Default
Requires: python3-core
Provides: pypi(suds)

%description python3
python3 components for the pypi-suds package.


%prep
%setup -q -n suds-1.1.2
cd %{_builddir}/suds-1.1.2
pushd ..
cp -a suds-1.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679700489
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-suds
cp %{_builddir}/suds-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-suds/adbfde070cbf605aea1261de577ac0d2b2c12d68 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-suds/adbfde070cbf605aea1261de577ac0d2b2c12d68

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*