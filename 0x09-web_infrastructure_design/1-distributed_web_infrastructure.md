# Distributed Web Infrastructure

![Image of a distributed web infrastructure](https://raw.githubusercontent.com/JohnSamy2004/alx-system_engineering-devops/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure.jpg)


## Description

This is a distributed web infrastructure designed to reduce traffic to the primary server by distributing some of the load to a replica server with the help of a load balancer. This configuration aims to improve reliability, scalability, and performance.

## Specifics About This Infrastructure

+ **Load Balancer Distribution Algorithm**<br/>
  The HAProxy load balancer is configured with the *Round Robin* algorithm. This algorithm cycles through each server in turn, distributing requests evenly. It's a fair and efficient method, ensuring that all servers handle an equal share of the load. *Round Robin* dynamically adjusts server weights to balance the load as needed.

+ **Setup Enabled by the Load Balancer**<br/>
  The HAProxy load balancer is set up in an *Active-Passive* configuration. In this setup, one server is active and handles requests, while the other server is passive, standing by to take over if the active server fails. This ensures high availability and reliability. In contrast, an *Active-Active* setup would have all nodes active and handling requests simultaneously, improving throughput and response times but requiring more complex management.

+ **Database Primary-Replica Cluster**<br/>
  In a *Primary-Replica* (or *Master-Slave*) cluster, the primary server handles all write operations, while the replica server handles read operations. This setup reduces the read load on the primary server, enhancing performance. Data is synchronized from the primary to the replica server to ensure consistency.

+ **Difference Between Primary and Replica Nodes**<br/>
  The primary node manages all write operations and updates, while the replica node handles read operations. This separation helps in load balancing and ensures that read requests do not overload the primary server, improving overall efficiency.

## Issues With This Infrastructure

+ **Single Points of Failure (SPOF)**<br/>
  There are several SPOFs in this setup. If the primary MySQL database server goes down, the site cannot process write operations. Similarly, if the load balancer or the application server fails, it could bring down the entire infrastructure.

+ **Security Issues**<br/>
  The data transmitted over the network is not encrypted due to the lack of SSL certificates, making it vulnerable to interception by hackers. Additionally, there are no firewalls in place to block unauthorized IP addresses, posing a significant security risk.

+ **Lack of Monitoring**<br/>
  There is no monitoring system in place to track the status and performance of each server. Without monitoring, it is challenging to detect issues proactively, leading to potential downtime and maintenance challenges.
