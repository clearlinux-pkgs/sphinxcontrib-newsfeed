#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-newsfeed
Version  : 0.1.4
Release  : 36
URL      : http://pypi.debian.net/sphinxcontrib-newsfeed/sphinxcontrib-newsfeed-0.1.4.tar.gz
Source0  : http://pypi.debian.net/sphinxcontrib-newsfeed/sphinxcontrib-newsfeed-0.1.4.tar.gz
Summary  : News Feed extension for Sphinx
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-newsfeed-license = %{version}-%{release}
Requires: sphinxcontrib-newsfeed-python = %{version}-%{release}
Requires: sphinxcontrib-newsfeed-python3 = %{version}-%{release}
Requires: Sphinx
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-python

%description
``sphinxcontrib-newsfeed`` -- News Feed extension for Sphinx
        ****************************************************************
        
        Overview
        ========
        
        ``sphinxcontrib-newsfeed`` is a extension for adding a simple *Blog*,
        *News* or *Announcements*  section to a Sphinx_ website.

%package license
Summary: license components for the sphinxcontrib-newsfeed package.
Group: Default

%description license
license components for the sphinxcontrib-newsfeed package.


%package python
Summary: python components for the sphinxcontrib-newsfeed package.
Group: Default
Requires: sphinxcontrib-newsfeed-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-newsfeed package.


%package python3
Summary: python3 components for the sphinxcontrib-newsfeed package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_newsfeed)
Requires: pypi(sphinx)

%description python3
python3 components for the sphinxcontrib-newsfeed package.


%prep
%setup -q -n sphinxcontrib-newsfeed-0.1.4
cd %{_builddir}/sphinxcontrib-newsfeed-0.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583697351
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-newsfeed
cp %{_builddir}/sphinxcontrib-newsfeed-0.1.4/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-newsfeed/cb85b4873c8f8fe43344bf8e4c07b860260044e7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-newsfeed/cb85b4873c8f8fe43344bf8e4c07b860260044e7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
