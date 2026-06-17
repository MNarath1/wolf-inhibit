Name:           wolf-inhibit
Version:        1.0
Release:        1%{?dist}
License:        MIT
Summary:        Inhibits sleep when wolf session is active

URL:            https://github.com/MNarath1/wolf-inhibit

Source:         https://github.com/MNarath1/wolf-inhibit/archive/refs/tags/1.0.tar.gz
BuildArch:      noarch

Requires:       docker

BuildRequires:  systemd-rpm-macros

%description
Inhibits Sleep when active wolf session is detected

%prep
%autosetup

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
cp -v ./wolf-inhibit %{buildroot}%{_bindir}
cp -v ./wolf-inhibit.service %{buildroot}%{_unitdir}

# Do post-installation
%post

systemctl daemon-reload
systemctl enable wolf-inhibit --now

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%{_bindir}/wolf-inhibit
%{_unitdir}/wolf-inhibit.service
