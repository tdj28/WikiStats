include_recipe 'apache2::mod_wsgi'


web_app "wikistats" do
       template 'web_app.conf.erb'
       server_name 'localhost'
end
