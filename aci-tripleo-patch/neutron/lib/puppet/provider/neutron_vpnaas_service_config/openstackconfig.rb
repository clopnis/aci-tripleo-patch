Puppet::Type.type(:neutron_vpnaas_service_config).provide(
  :openstackconfig,
  :parent => Puppet::Type.type(:openstack_config).provider(:ruby)
) do

  def self.file_path
    '/etc/neutron/neutron_vpnaas.conf'
  end

  # added for backwards compatibility with older versions of inifile
  def file_path
    self.class.file_path
  end

end
