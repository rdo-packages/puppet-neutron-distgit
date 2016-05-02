Name:           puppet-neutron
Version:        XXX
Release:        XXX
Summary:        Puppet module for OpenStack Neutron
License:        Apache-2.0

URL:            https://launchpad.net/puppet-neutron

Source0:        https://github.com/openstack/puppet-neutron/archive/%{version}.tar.gz

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
%setup -q -n %{name}-%{version}

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

