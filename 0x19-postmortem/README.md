# 	A Post-Mortem Report of The Outage That Took Down My Server

## Summary
At precisely 3:00pm West African Time on Thursday 24-04-2023, two web servers hosting the web pages started slowing down, then at 5:00pm, they shut down. The number of requests queued up with each assignment to it, and 50,000 clients could not access the landing page of the website. On-call engineers were quickly briefed, and new servers were deployed to work along with the active servers. The cause of the downtime was found to be an untested server-side function deployed to production.

The server-side scripts were updated with the removal of the functions, and the servers restarted.

## Timeline
- 3:00pm WAT: Request processing on servers started slowing down
- 5:00pm WAT: servers stopped processing requests due to backlog of unprocessed requests, which ultimately caused thier failure
- 7:00pm WAT: On-call engineers were notified
- 7:50pm WAT: New servers were provisioned, and the failed servers diconnected from the services
- 9:00pm WAT: Tests were carried out which pointed out a failure. The failure was a proposed search algorithm function which is not approved for deployment
- 9:30pm WAT: New tests were carried out which passed.
- 10:00pm WAT: The formerly failed servers were deployed.

## Root cause

A proposed search algorithm which would optimize the search feature was accidentally deployed to production. This untested script had similar name with the current search script, but with a suffix of `_v2` was deployed to two of my servers.

## Corrective and preventive measures
Naming of scripts/directories which is an improvement/upgrade of a current version is more important that I would have originally stated. That being said, I can't come up with a new naming system which would prevent a similar ocuurence, but a bash script which would automate marking of similar scripts and notify me of their similarities and differences would ensure that new and existing scripts or existing scripts which are updated should be properly tested before deployment.

Furthermore, engineers should take advantage of monitoring tools so that total downtime of a server will be averted early in the future. 
