%global date 20160428
%global commit b66d1ad93e7a1fe7d9564b0293243f785da8b0b6
%global short_commit %(c=%{commit}; echo ${c:0:7})

%define _prefix /opt/aws

Name:           ec2-expire-snapshots
Version:        %{date}git%{short_commit}
Release:        1%{?dist}
Summary:        Delete expired EBS snapshots in Amazon EC2
Group:          Applications/Internet
License:        Apache License 2.0
URL:            https://github.com/alestic/%{name}
Source0:        https://github.com/alestic/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl

%description
Delete expired EBS snapshots in Amazon EC2

%prep
%setup -q -n %{name}-%{commit}
%build
%{__make} %{?_smp_mflags}

%install
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0755 %{name} %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README.textile
%{_bindir}/%{name}

%changelog
* Thu Apr 28 2016 Taylor Kimball <noreply@linuxhq.org> - 20160428gitb66d1ad-1
- Initial package.
