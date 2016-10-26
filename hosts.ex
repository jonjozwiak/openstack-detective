[all:vars]
# OpenStack release. Valid value is one of 'kilo,liberty,mitaka,newton' and so on
openstack_release=newton
os_admin_username=admin
os_admin_password=password
os_admin_project_name=admin
os_auth_url=http://192.168.220.100:5000/v2.0

[controller]
192.168.220.78
192.168.220.79
192.168.220.80

[compute]
192.168.220.90
192.168.220.91
192.168.220.92
192.168.220.93

[ceph]
192.168.220.150
192.168.220.151
192.168.220.152
192.168.220.153
