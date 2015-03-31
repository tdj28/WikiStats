#
# Cookbook Name:: wikistats
# Recipe:: default
#

execute "apt-get-update-periodic" do
  command "apt-get update"
  ignore_failure true
  only_if do
    !File.exists?('/var/lib/apt/periodic/update-success-stamp') ||
    File.mtime('/var/lib/apt/periodic/update-success-stamp') < Time.now - 86400
  end
end

package "redis-server" do
    action :install
end

execute "/etc/init.d/redis-server start" do
    ignore_failure true
end
