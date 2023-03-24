#	Configuration Management - CI/CD

Handling and monitioring changes to softwares is a crucial part of the software engineering process. This includes provisioning of servers, version control of scripts, replication of environments for the same configuration and tools e.t.c. 
Configuration management makes tasks in the foregoing paragraph trivial. which can speed up the software development process. To add, CM can play a big role in crucial moments, for example, a server goes down and the team needs to keep the company's services running. A CM tool can help to deploy a new server with all necessary configurations while they focus on getting error logs and analysis of the server that went down without spending too much time worrying about how to keep the service running.
Read about Sylvain Kalache's experience [here](https://engineering.linkedin.com/slideshare/skynet-project-_-monitor-scale-and-auto-heal-system-cloud)

The ```puppet``` configuration tool is used in this project as an introduction to continuous integration and continuos development

### Requirements
- Ubuntu 20.04
- puppet 5.5.10 
