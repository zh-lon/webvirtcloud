# -*- mode: ruby -*-
# vi: set ft=ruby :

BOX = "bento/centos-7.5"
KVM_CPU = 2
KVM_RAM = 4096
KVM_NODES = 1

Vagrant.configure(2) do |config|
  config.vm.box = "#{BOX}"
  config.ssh.insert_key = false
  config.vm.provision :shell, path: "devenv/vagrant/bootstrap.sh"
  config.vm.network "private_network", ip: "192.168.250.254", auto_config: false
  config.vm.network "private_network", ip: "10.16.0.254", auto_config: false
  config.vm.network "forwarded_port", guest: 9090, host: 9090
  config.vm.network "forwarded_port", guest: 16509, host: 16509

  (0..KVM_NODES - 1).each do |i|
    config.vm.define "node#{i}" do |kvm|
      kvm.vm.hostname = "node#{i}"
      kvm.vm.provider :virtualbox do |vb|
        vb.cpus = "#{KVM_CPU}"
        vb.memory = "#{KVM_RAM}"
      end
    end
  
  end
end
