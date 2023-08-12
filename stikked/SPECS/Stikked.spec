Name:          Stikked
Version:       0.12.0
Release:       1%{?dist}
Summary:       An open-source PHP pastebin
Group:         Applications/System
License:       CC0
URL:           https://github.com/claudehohl/%{name}
Source0:       https://github.com/claudehohl/%{name}/archive/%{version}.tar.gz
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      php, php-mysql

%description
Stikked is an Open-Source PHP Pastebin, with the aim of keeping
a simple and easy to use user interface.

Stikked allows you to easily share code with anyone you wish.
Based on the original Stikked with lots of bugfixes and improvements.

%prep
%setup -q -n %{name}-%{version}
%build
%install
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}
%{__cp} -rf htdocs %{buildroot}%{_datadir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%doc AUTHORS.md CC0 doc README.md
%{_datadir}/%{name}

%changelog
* Mon Mar 26 2018 Taylor Kimball <noreply@linuxhq.org> - 0.12.0-1
- Update to v0.12.0

* Thu Apr 28 2016 Taylor Kimball <noreply@linuxhq.org> - 20160428gitc1257bb-1
- Update to commit c1257bb.
