
mysql_service 'default' do
    port '3306'
    version '5.5'
    initial_root_password node['mysql_password']
    action [:create, :start]
end

mysql_config 'default' do
    source 'my.cnf.erb'
    notifies :restart, 'mysql_service[default]'
    action :create
end

mysql_client 'default' do
    action :create
end

# New version of this cook book wipes /etc/mysql/my.cnf
# Uh. Their readme has more on this.
link "/etc/mysql/my.cnf" do
    to "/etc/mysql-default/my.cnf"
end

link "/var/run/mysqld/mysqld.sock" do
    to "/var/run/mysql-default/mysqld.sock"
end

package "libmysqlclient-dev" do
    action :install
end

file "/root/.my.cnf" do
    owner  "root"
    group  "root"
    mode 00600
    content "[client]\nuser=root\npassword=#{node['mysql_password']}"
    action :create
end

execute "make_wikistats_db" do
    cwd "/Website"
    command "mysql < wikistats.sql"
    user "root"
    action :run
    # should have a not_if in here
    not_if 'test -d /var/lib/mysql-default/wikistats'
    notifies :restart,
        "service[apache2]"
    notifies :run, "execute[make_data_db]"
    # chaining them means we only need one not_if that will 
    # cut off that branch of execute
end

execute "make_data_db" do
    cwd "/MapReduce/data"
    command "for i in `ls *.sql`; do mysql < $i; done"
    user "root"
    action :nothing
end
