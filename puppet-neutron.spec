%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-neutron
Version:        11.5.0
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
* Fri Jan 19 2018 RDO <dev@lists.rdoproject.org> 11.5.0-1
- Update to 11.5.0

* Fri Dec 01 2017 RDO <dev@lists.rdoproject.org> 11.4.0-1
- Update to 11.4.0

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 11.3.0-1
- Update to 11.3.0



