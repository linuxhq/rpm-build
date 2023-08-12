%global date 20160430
%global git_commit 989bb187106be43e8e9946e82bcd9f2177d13ae5
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

%define module colloquy

Name:           znc-%{module}
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Colloquy Module for ZNC
Group:          System Environment/Daemons
License:        GPL
URL:            https://github.com/wired/colloquypush
Source0:        https://github.com/wired/colloquypush/archive/%{git_commit}/colloquypush-%{git_commit}.tar.gz
Patch0:         %{name}.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       libicu, znc
BuildRequires:  libicu-devel, gcc-c++, make, znc-devel

%description
Colloquy push module for ZNC

%prep
%setup -q -n colloquypush-%{git_commit}
%patch0 -p0
%build
znc-buildmod znc/%{module}.cpp

%install
%{__install} -d -m 0755 %{buildroot}%{_libdir}/znc
%{__install} -m 0755 %{module}.so %{buildroot}%{_libdir}/znc

%clean
%{__rm} -rf %{buildroot}

%files
%doc znc/AUTHORS znc/README
%{_libdir}/znc/%{module}.so

%changelog
* Thu Apr 30 2016 Taylor Kimball <noreply@linuxhq.org> - 20160430git989bb18-1
- Initial build.
