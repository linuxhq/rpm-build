%global date 20160430
%global git_commit 5eb9be0e1478ec221db2de11d430d16dfbdf0bc1
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

%define module fish

Name:           znc-%{module}
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        FiSH Module for ZNC
Group:          System Environment/Daemons
License:        GPL
URL:            https://github.com/dctrwatson/znc-%{module}
Source0:        https://github.com/dctrwatson/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Patch0:         %{name}.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       libicu, znc
BuildRequires:  libicu-devel, gcc-c++, make, znc-devel

%description
FiSH Module for ZNC

%prep
%setup -q -n %{name}-%{git_commit}
%patch0 -p0
%build
znc-buildmod %{module}.cpp

%install
%{__install} -d -m 0755 %{buildroot}%{_libdir}/znc
%{__install} -m 0755 %{module}.so %{buildroot}%{_libdir}/znc

%clean
%{__rm} -rf %{buildroot}

%files
%doc README.md
%{_libdir}/znc/%{module}.so

%changelog
* Thu Apr 30 2016 Taylor Kimball <noreply@linuxhq.org> - 20160430git5eb9be0-1
- Initial build.
