# openstack-detective
Openstack-detective is a tool based on ansible to help troubleshoot and diagnose an openstack environment.  

## Usage
* Install ansible on your host (for instance, triple-o/director)
* Create a hosts file to reflect your environment (example in hosts.ex)
* Setup SSH key from your ansible host to the hosts in your hosts file
```
ssh-copy-id heat-admin@<hostname>
  # Or manually paste your .ssh/id_rsa.pub into authorized_keys for the user on the given host
```
* Update group_vars/all and set your user and whether you need to sudo
```
remote_user: "heat-admin"
become: "True"
```
* Execute the checks 
```
ansible-playbook -i hosts healthcheck.yml
# Example of executing only rabbitmq checks and creating a report
#ansible-playbook -i hosts healthcheck.yml --tags='rabbitmq,report'
#ansible-playbook -i hosts healthcheck.yml --tags='glance_backend,report'
```
* View results 
Results will be written to results/config_report.log unless you change the group_vars/all result_dir variable

NOTE: If you see a message like below in the results, it means either the check did not run or there was a problem with it and it received no value: 
```
WARNING: <check>  NOT DEFINED - Check the ansible run to see what happened
```

