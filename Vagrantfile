# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://oss-binaries.phusionpassenger.com/vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"
  config.vm.hostname = "explorewikistats"
  config.omnibus.chef_version = :latest
  config.berkshelf.berksfile_path = "./Berksfile"
  config.berkshelf.enabled = true
  config.vm.network :forwarded_port, guest: 80, host: 8080


  config.ssh.forward_agent = true
  config.vm.synced_folder "Website", "/Website"
  config.vm.synced_folder "MapReduce", "/MapReduce"


  config.vm.provider :virtualbox do |vb|
     vb.customize ["modifyvm", :id, "--memory", "512"]
   end

  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "cookbooks"
    chef.roles_path = "roles"
    chef.data_bags_path = "databags"
    chef.add_role "wikistats"
    chef.json = { :mysql_password => "foo" }
  end
end
