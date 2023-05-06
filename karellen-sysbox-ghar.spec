%global debug_package %{nil}

Name: karellen-sysbox-ghar
Version: 0.0.1
Release: 1
License: ASL 2.0
Summary: Karellen GitHub Actions Runner for Sysbox Containers
Url: https://github.com/karellen/%{name}

BuildRequires: systemd-rpm-macros

Requires: karellen-sysbox
Requires: python3
Requires: python3-requests

Source0: %{name}-%{version}.tar.gz

%description
A service that spawns a Sysbox-secured self-hosted GitHub Actions Runner

%prep
%autosetup

%build

%install
install -Dpm 744 karellen-sysbox-ghar-wrapper -t %{buildroot}/%{_sbindir}/
install -Dpm 600 karellen-sysbox-ghar -t %{buildroot}%{_sysconfdir}/sysconfig/
install -Dpm 644 karellen-sysbox-ghar.service -t %{buildroot}%{_unitdir}/

%files
%license LICENSE
%attr(600, root, root) %config(noreplace) %{_sysconfdir}/sysconfig/karellen-sysbox-ghar

%attr(700, root, root) %{_sbindir}/karellen-sysbox-ghar-wrapper
%{_unitdir}/karellen-sysbox-ghar.service

%post
%systemd_post karellen-sysbox-ghar.service

%preun
%systemd_preun karellen-sysbox-ghar.service

%postun
%systemd_postun_with_restart karellen-sysbox-ghar.service

%changelog
* Sat May 06 2023 Arcadiy Ivanov <arcadiy@ivanov.biz> 0.0.1-1
- Initial release

