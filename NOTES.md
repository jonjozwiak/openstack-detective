= Notes / To Do 

== Common
* Validate time in sync across ALL nodes 
* Check disk space on all nodes
* Check CPU, RAM, Swap space usage?
* Verify limits, kernel params
* Check log rotation on nodes?
* A few common browbeat checks (https://github.com/openstack/browbeat/blob/master/ansible/check/roles/common/tasks/main.yml)
  * Verify selinux running
  * Check tuned running and correct profile 

== Per Service
* Check packages installed 
* Check services running 
* Check configuration files - at least for basic things
* Check iptables / firewalld rules
* Verify connection from string in config to DB
  * Verify DB has tables
* Confirm user/pw auth thru keystone
  * Confirm endpoints?  
  * Confirm service?  
* Test main list functionality (As shown below in basic functionality test)
* Check number of workers per component?  Like number of api_workers for glance?  
== High Level Functionality 
* Add ceph node checks
* Add ceph backend checks (Verify pools, auth, etc)
* Add compute node checks
* Add block storage node checks
* Add swift storage node checks
* Add/Document some way to enable/disable checks.  No need to check cinder backup if its not configured... or swift...
* Check for deleted objects in databases?
  * Check for cron jobs where appropriate?
* Detect which openstack version somehow...  RPM name?


== Heat
* Simplifying nested stack troubleshooting with Director

== Ceilometer

== Neutron
* Add some capability to connection test a VM end to end
  * Make certain it is there correctly on all hops
  * Perhaps automate walking through http://abregman.com/2016/01/06/openstack-neutron-troubleshooting-and-solving-common-problems/ or http://dischord.org/2015/03/09/troubleshooting-openstack-neutron-networking-part-one/
  * This should handle vxlan/gre OR vlan
* Check for MTU mismatches
* Check for dnsmasq not running

== Nova
* Look for 'XXX' in nova-manage service list
* Create a playbook that tracks an instance across logs.  (Basically, by UUID see all log messages for an instance?)


== Cinder
* Verify api and scheduler are up
* Verify there is space left on the backing storage (if possible)
* LVM backend
  * In logs: volume group cinder-volumes does not exist
  * In logs: AMQP server on ... ECONNREFUSED. Trying again in xx seconds.

== Glance 
* ADD IPTABLES CHECKS? - For example... 9292 for glance api
  * 9191 for glance registry
  * But no external communication needed to glance registry if colocated with api
* VALIDATE BACKEND CHECKS
* Finish  backend Checks (Note likely different from kilo to liberty to mitaka)
  * RBD
    * Validate ceph auth correct  (Capture what the log should look like if this is not)
    * Validate settings in conf file
  * File (NFS)
    * Validate settings in conf file
    * Validate write permissions on backend
    * Validate mounts on correct servers
  * Swift?
  * Cinder?

== Swift

== RabbitMQ
* In individual modules, the rabbit connection check doesn't print an 'OK' message if successful.  Ideally it would so you know it was checked.
* Make certain the config specifies rabbit and not another backend
* Check for AMQP connections for applicable services 
* check that management plugin enabled 
  * rabbitmq-plugins enable rabbitmq_management (on port 15672)
* Watch queue levels.  Set alerts on queues backing up
* rabbitmqctl status
  * File Descriptors (Total + Sockets)
  * Processes - limit vs used 
* Check nodes / cluster partition
* Check number of messages_ready in the queue (via localhost:15672/api/queues) and alert if > a specific number... Suggesting the queue is backing up? 

== Keystone 
* Validate users in correct roles?  (_member_ or admin?)
* Validate users belong to projects?  

== HAProxy 
* Check maxconn? 

== Galera / MariaDB 


== Pacemaker
* Some help troubleshooting would be nice.  For instance, when I tried manually removing pacemaker remote all of a sudden my cluster crashed and wouldn't restart.  In this case, answers were in /var/log/messages
  * Maybe Beekhof's troubleshooting could be automated: http://blog.clusterlabs.org/blog/2013/debugging-pacemaker
  * Andrew Beekhof says 120s is the correct timeout for systemd based serviecs
    * pcs resource update $RESOURCE op start timeout=60s op stop timeout=60s

== HA tests 
* Check mysql data replication
* verify amount of tables in DB is same on each node
* Check galera envionment state
* RabbitMQ availability 
* RabbitMQ replication 
* check pacemaker status / health

== Functional Tests / Smoke Test 
* Make this optional or a separate role
* Run 'list' commands per service
* Check that required services are running (and enabled via systemd or pacemaker) 
* Functional tests (like cinder create/delete, glance image-create, download, etc) - A minimal subset of what Tempest can test
* Glance Functional Tests Example
  * https://github.com/openstack/tempest/tree/master/tempest/api/image/v2 
  * Test Create image
  * Test Update Image
  * Test List Images
  * Test Delete Image
  * Create, Verify, Delete Tag on Image
  * metadef namespace testing?
  * Test public vs private images?
  * Test image share accept / reject?


== Create testing framework (so we can validate all the checks work)
Thoughts of this...
* Glance
  * Process not running
  * DB auth incorrect
  * DB not initialized
  * Rabbit auth incorrect
  * Create RBD test case (ceph auth incorrect)
  * Create RBD test case (no pool defined)
  * Create RBD test case (can't reach storage network)
  * Create NFS test case (failing perms)
  * Create NFS test case (not mounted)
  * Create NFS test case (can't reach storage network)
* Create tests
  * playbooks to break the deployment
  * Validate the break
  * Maybe even do a random break that people can use for training purposes outside of using the playbooks to detect problems
* Potential deployment test scenarios
  * All in one 
  * Distributed HA (standard 3-node control plane)
  * Fully distributed components (maybe achieved via Kolla) 
    * DB not on same nodes as APIs
    * RabbitMQ not on same nodes as APIs


== Longer term
* Test against Kolla - Some things like systemctl may have to change
* Test aginst containerized compute 
