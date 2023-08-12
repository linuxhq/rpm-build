%global date 20160428
%global git_commit 482bcf07804a7745a08cd799d997bdebc9e8bd36
%global short_commit %(c=%{git_commit}; echo ${c:0:7})

%define module palaver

Name:           znc-%{module}
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Palaver ZNC Module
Group:          System Environment/Daemons
License:        GPL
URL:            https://github.com/cocodelabs/znc-%{module}
Source0:        https://github.com/cocodelabs/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       libicu, znc
BuildRequires:  gcc-c++, libicu-devel, make, znc-devel

%description
Palaver ZNC module provides push notifications.

%prep
%setup -q -n %{name}-%{git_commit}
%build
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 0755 %{buildroot}%{_libdir}/znc
%{__install} -m 0755 %{module}.so %{buildroot}%{_libdir}/znc

%clean
%{__rm} -rf %{buildroot}

%files
%doc LICENSE README.md VERSION
%{_libdir}/znc/%{module}.so

%changelog
* Thu Apr 28 2016 Taylor Kimball <noreply@linuxhq.org> - 20160428git482bcf0-1
- Initial build.
