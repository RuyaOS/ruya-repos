%global fedora_compat %{?fedora}

Name: ruya-repo
Version: 0.3
Release: 1%{?dist}
Summary: Ruya Software Repos
Summary(ar): مستودعات رؤية البرمجية
License: GPLv3
URL: https://ruya.parmg.sa
BuildArch: noarch

%description
Ruya software official repos.

%description -l ar
مستودعات رؤية البرمجية الرسمية.



%package -n ruya-dnf
Summary: Ruya dnf customizations

%description -n ruya-dnf
Ruya dnf customizations.

%description -n ruya-dnf -l ar
تخصيصات رؤية لمدير البرمجيات د.ن.ف.



%prep
echo '[ruya]
name=Ruya Softwares %{version}
baseurl=https://download.copr.fedorainfracloud.org/results/moceap/RUYA/fedora-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/moceap/RUYA/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1

[ruya:ml]
name=Ruya Softwares %{version} - Multilib
baseurl=https://download.copr.fedorainfracloud.org/results/moceap/RUYA/fedora-$releasever-i386/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/moceap/RUYA/pubkey.gpg
repo_gpgcheck=0
cost=1100
enabled=1
enabled_metadata=1' > ruya.repo


echo '%{fedora_compat}' > releasever


%build
#Nothing to build

%install
install -d -m 755 %{buildroot}/etc/yum.repos.d
install -m 644 ruya.repo %{buildroot}/etc/yum.repos.d

install -d -m 755 %{buildroot}/etc/dnf/vars
install -m 644 releasever %{buildroot}/etc/dnf/vars

%post -n ruya-dnf
echo "$(cat /etc/dnf/dnf.conf)

## Add by ruya-dnf package
fastestmirror=true
deltarpm=true
max_parallel_downloads=11" > /etc/dnf/dnf.conf

%files
%config(noreplace) /etc/yum.repos.d/ruya.repo

%files -n ruya-dnf
/etc/dnf/vars/releasever

%changelog
* Mon Oct 24 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 0.3-1
- Add dnf custom configurations

* Mon Oct 10 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 0.2-1
- Fedora version number

* Sun Oct 2 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 0.1-1
- Initial.

