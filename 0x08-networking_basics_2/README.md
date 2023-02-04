#	Networking Basics

This directory contains tasks that I took on at ALX Software Engineering programme that introduced me Networking basics, which includes, but not limited to:
- The Open Systems Interconnection Model (OSI)
- Types of Network
	- LAN
	- WAN e.t.c
- IP & MAC Addresses
- The TCP/IP & UDP/IP
- Listening on port

## Example
**Terminal 0 (client terminal)**
```
$ sudo ./100-port_listening_on_localhost

```
**Terminal 1 (server terminal)**
```
$ telnet localhost 98
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Hello Taiwo
```
**Terminal 0 (client terminal)** *Receives text from server*
```
$ sudo ./100-port_listening_on_localhost
Hello Taiwo
```

## Note
**Ports below 1024 are listened on with ```sudo``` access.**

## Requirements
- ```#!/usr/bin/env bash``` at the top of the bash scripts
- Ubuntu 20.04
