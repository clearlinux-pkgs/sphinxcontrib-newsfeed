#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sphinxcontrib-newsfeed
Version  : 0.1.4
Release  : 1
URL      : http://pypi.debian.net/sphinxcontrib-newsfeed/sphinxcontrib-newsfeed-0.1.4.tar.gz
Source0  : http://pypi.debian.net/sphinxcontrib-newsfeed/sphinxcontrib-newsfeed-0.1.4.tar.gz
Summary  : News Feed extension for Sphinx
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-newsfeed-python
Requires: Sphinx
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
``sphinxcontrib-newsfeed`` -- News Feed extension for Sphinx
        ****************************************************************
        
        Overview
        ========
        
        ``sphinxcontrib-newsfeed`` is a extension for adding a simple *Blog*,
        *News* or *Announcements*  section to a Sphinx_ website.

%package python
Summary: python components for the sphinxcontrib-newsfeed package.
Group: Default

%description python
python components for the sphinxcontrib-newsfeed package.


%prep
%setup -q -n sphinxcontrib-newsfeed-0.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502836914
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1502836914
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
