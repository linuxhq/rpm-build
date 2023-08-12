Name:           phantomjs
Version:        2.1.1
Release:        1%{dist}
Summary:        PhantomJS is a headless WebKit scriptable with a JavaScript API.
Group:          Development/Languages
License:        BSD
URL:            http://phantomjs.org
Source0:        https://bitbucket.org/ariya/%{name}/downloads/%{name}-%{version}-linux-%{_arch}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       expat, fontconfig, freetype, zlib

%description
PhantomJS is a headless WebKit scriptable with a JavaScript API.
It has fast and native support for various web standards: DOM handling,
CSS selector, JSON, Canvas, and SVG.

%prep
%setup -n %{name}-%{version}-linux-%{_arch}
%build
%install
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0755 bin/%{name} %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%doc ChangeLog LICENSE.BSD README.md third-party.txt examples/
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Thu Apr 28 2016 Taylor Kimball <noreply@linuxhq.org> - 2.1.1-1
- Updated to 2.1.1.

* Mon Dec 07 2015 Taylor Kimball <noreply@linuxhq.org> - 2.0.0-1
- Initial build.
