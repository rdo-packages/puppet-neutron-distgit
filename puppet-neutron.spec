%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-neutron
Version:        13.3.1
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Neutron
License:        ASL 2.0

URL:            https://launchpad.net/puppet-neutron

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-nova
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet-sysctl
Requires:       puppet-vswitch
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Neutron

%prep
%setup -q -n openstack-neutron-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/neutron/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/neutron/



%files
%{_datadir}/openstack-puppet/modules/neutron/


%changelog
* Mon Oct 15 2018 RDO <dev@lists.rdoproject.org> 13.3.1-1
- Update to 13.3.1

* Mon Aug 20 2018 RDO <dev@lists.rdoproject.org> 13.3.0-1
- Update to 13.3.0



