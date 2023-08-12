Name:           hatop
Version:        0.7.7
Release:        1%{dist}
Summary:        Interactive ncurses client for the HAProxy unix socket
Group:          Applications/System
License:        GPLv3
URL:            http://feurix.org/projects/%{name}
Source0:        https://github.com/feurix/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python

%description
HATop's appearance is similar to top(1). It supports various modes
for detailed statistics of all configured proxies and services in near
realtime. In addition, it features an interactive CLI for the haproxy
unix socket. This allows administrators to control the given haproxy
instance (change server weight, put servers into maintenance mode, ...)
directly out of hatop and monitor the results immediately.

%prep
%setup -q -n %{name}-%{version}
%build
%install
%{__install} -d -m 0755 %{buildroot}%{_sbindir} \
                        %{buildroot}%{_datadir}/man/man1

%{__install} -m 0755 bin/%{name} %{buildroot}%{_sbindir}
%{__install} -m 0644 man/%{name}.1 %{buildroot}%{_datadir}/man/man1

%{__gzip} -9 %{buildroot}%{_datadir}/man/man1/%{name}.1

%clean
%{__rm} -rf %{buildroot}

%files
%doc CHANGES HACKING KEYBINDS LICENSE README
%defattr(-,root,root,-)
%{_sbindir}/%{name}
%{_datadir}/man/man1/%{name}.*

%changelog
* Fri Jun 19 2015 Taylor Kimball <noreply@linuxhq.org> - 0.7.7-1
- Initial build.
