Name:           python-lxml
Version:        4.1.1
Release:        1%{?dist}
Summary:        XML processing library combining libxml2/libxslt with the ElementTree API
Group:          Development/Libraries
License:        BSD
URL:            http://lxml.de
Source0:        http://lxml.de/files/lxml-%{version}.tgz
BuildRequires:  libxml2-devel, libxslt-devel, python2-devel, python-setuptools
Requires:       libxml2, libxslt, python-cssselect, python-html5lib, python-beautifulsoup4

%description
lxml provides a Python binding to the libxslt and libxml2 libraries.
It follows the ElementTree API as much as possible in order to provide
a more Pythonic interface to libxml2 and libxslt than the default
bindings.  In particular, lxml deals with Python Unicode strings
rather than encoded UTF-8 and handles memory management automatically,
unlike the default bindings.

%prep
%setup -q -n lxml-%{version}
%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__python} setup.py install --skip-build --no-compile --root %{buildroot}

%files
%doc LICENSES.txt PKG-INFO CREDITS.txt CHANGES.txt doc/*
%{python_sitearch}/lxml
%{python_sitearch}/lxml-*.egg-info

%changelog
* Sun Feb 11 2018 Taylor Kimball <packages@linuxhq.org> - 4.1.1-1
- Initial build.
