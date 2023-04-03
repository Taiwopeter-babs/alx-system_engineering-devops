#	Load Balancing

Load balancers, which may be a software or hardware, distribute the workload of a system to multiple individual systems or group of systems to reduce the amount of load/traffic/connections to a single system.
Load balancing creates redundancy so that a single point of failure is averted, thus increasing the relaibility, efficiencynd overall performance of the application.

In this project, a nginx load balancer is configured with HAProxy (High Availabilty Proxy) and [round-robin](https://www.thegeekstuff.com/2016/01/load-balancer-intro/) algorithm to distribute connections to two web servers.

## Requirements
- Ubuntu 20.04
- Nginx web servers
- shellcheck
