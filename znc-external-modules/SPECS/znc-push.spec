%global date 20160430
%global git_commit 46148fc0815944f72bc9c3c3c128eff4623c6765
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

%define module push

Name:           znc-%{module}
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Push ZNC module
Group:          System Environment/Daemons
License:        GPL
URL:            https://github.com/jreese/znc-%{module}
Source0:        https://github.com/jreese/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       libcurl, libicu, znc
BuildRequires:  libcurl-devel, libicu-devel, gcc-c++, make, znc-devel

%description
ZNC Push is a module for ZNC that will send notifications to
multiple push notification services, or SMS for any private
message or channel highlight that matches a configurable set
of conditions.

%prep
%setup -q -n %{name}-%{git_commit}
%build
%{__make} %{?_smp_mflags} curl=yes

%install
%{__install} -d -m 0755 %{buildroot}%{_libdir}/znc
%{__install} -m 0755 %{module}.so %{buildroot}%{_libdir}/znc

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md doc/
%{_libdir}/znc/%{module}.so

%changelog
* Thu Apr 30 2016 Taylor Kimball <noreply@linuxhq.org> - 20160430git46148fc-1
- Initial build.
