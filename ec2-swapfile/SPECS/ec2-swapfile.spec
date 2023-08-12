Name:           ec2-swapfile
Version:        0.1
Release:        1%{?dist}
Summary:        Swapfile creation init script
Group:          Applications/Internet
License:        GPL
URL:            https://github.com/linuxhq/ec2-swapfile
Source0:        ec2-swapfile.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description
Swapfile creation init script

%prep
%build
%install
%{__install} -d -m 0755 %{buildroot}%{_sysconfdir}/rc.d/init.d
%{__install} -m 0755 %{SOURCE0} %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}

%post
/sbin/chkconfig --add %{name}
/sbin/chkconfig %{name} on

%preun
/sbin/service %{name} stop > /dev/null 2>&1
/sbin/chkconfig --del %{name}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/rc.d/init.d/%{name}

%changelog
* Thu Apr 28 2016 Taylor Kimball <noreply@linuxhq.org> - 0.1-1
- Initial commit.
