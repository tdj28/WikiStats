# ExploreWikiStats
Base code for http://www.explorewikistats.org

## Chef deploy

In the top directory you will find a Vagrantfile, which you can launch via the command:

```
vagrant up
```

### But first:

This uses Berks, so you will want to install the chef-dk first and be sure that you don't have 
any gem Berks interfering:

```
wget https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/12.04/x86_64/chefdk_0.4.0-1_amd64.deb
sudo dpkg -i chefdk_0.4.0-1_amd64.deb
```

Vagrant will be ready as soon as you run:

```
vagrant plugin install vagrant-omnibus
vagrant plugin install vagrant-berkshelf
```

If you have trouble with berks, you can either point your current paths to the right chef-dk binaries/libs:

```
eval "$(chef shell-init bash)"
```

or try uninstalling the gem version:

```
gem uninstall berkshelf
```

This deploy has been tested against vagrant 1.7.

### OpsWorks

The flatness of the directory makes it ready, with trivial modification, for Opsworks.

### Viewing

The front end can be viewed from a browser on the host machine at localhost:8080

The API access can be ran from the command line of the host machine by running:

```
curl -X POST -H 'X-Authentication-Token: an-auth-token' localhost:8080/hits/
```

