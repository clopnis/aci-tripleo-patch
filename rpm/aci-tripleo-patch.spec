Name:           aci-tripleo-patch
Version:        9.0
Release:        %{?release}%{!?release:1}
Summary:        Files for ACI tripleO patch
License:        ASL 2.0
Group:          Applications/Utilities
Source0:        aci-tripleo-patch.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       libguestfs-tools

%define debug_package %{nil}

%description
This package contains files that are required for patch tripleO to support ACI

%prep
%setup -q -n aci-tripleo-patch

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/aci-tripleo-patch
cp -r * $RPM_BUILD_ROOT/opt/aci-tripleo-patch
chmod a+x $RPM_BUILD_ROOT/opt/aci-tripleo-patch/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/mv /usr/share/openstack-tripleo-heat-templates/puppet/compute.yaml /usr/share/openstack-tripleo-heat-templates/puppet/compute.yaml.orig
/usr/bin/mv /usr/share/openstack-tripleo-heat-templates/puppet/controller.yaml /usr/share/openstack-tripleo-heat-templates/puppet/controller.yaml.orig
/usr/bin/ln -s /opt/aci-tripleo-patch/files/compute.yaml /usr/share/openstack-tripleo-heat-templates/puppet/compute.yaml
/usr/bin/ln -s /opt/aci-tripleo-patch/files/controller.yaml /usr/share/openstack-tripleo-heat-templates/puppet/controller.yaml

%postun
unlink /usr/share/openstack-tripleo-heat-templates/puppet/compute.yaml
unlink /usr/share/openstack-tripleo-heat-templates/puppet/controller.yaml
mv /usr/share/openstack-tripleo-heat-templates/puppet/compute.yaml.orig /usr/share/openstack-tripleo-heat-templates/puppet/compute.yaml
mv /usr/share/openstack-tripleo-heat-templates/puppet/controller.yaml.orig /usr/share/openstack-tripleo-heat-templates/puppet/controller.yaml

%files
%defattr(-,root,root,-)
/opt/aci-tripleo-patch/*