# Secured and Monitored Web Infrastructure

![Image of a secured and monitored infrastructure](https://raw.githubusercontent.com/JohnSamy2004/alx-system_engineering-devops/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure.jpg)


## Description

This is a 3-server web infrastructure that ensures security, monitoring, and encrypted traffic transmission. The infrastructure leverages firewalls, SSL certificates, and monitoring clients to enhance security, performance, and reliability.

## Specifics About This Infrastructure

+ **Purpose of Firewalls**<br/>
  Firewalls serve as a critical security measure, acting as a barrier between the internal network and external threats. They filter incoming and outgoing traffic based on predetermined security rules, blocking unauthorized access while allowing legitimate communication. This protects the web servers from potential attacks and unauthorized users.

+ **Purpose of the SSL Certificate**<br/>
  An SSL certificate encrypts the data transmitted between web servers and users, ensuring secure communication. This encryption prevents man-in-the-middle attacks and data sniffing, safeguarding sensitive information like login credentials and personal data. SSL certificates provide privacy, data integrity, and server authentication, fostering trust in the website.

+ **Purpose of Monitoring Clients**<br/>
  Monitoring clients continuously assess the performance and health of servers and the network. They collect data on server operations, detect anomalies, and alert administrators to potential issues. By providing real-time insights and metrics, these tools help in maintaining optimal server performance, identifying security vulnerabilities, and ensuring prompt issue resolution.

## Issues With This Infrastructure

+ **Unencrypted Traffic Between Load Balancer and Web Servers**<br/>
  If SSL termination occurs at the load balancer, the traffic between the load balancer and the web servers remains unencrypted. This could expose sensitive data to potential threats within the internal network, undermining the overall security of the infrastructure.

+ **Single MySQL Server Limitation**<br/>
  Relying on a single MySQL server poses a scalability issue and represents a single point of failure. If the MySQL server experiences downtime, it could disrupt the entire web infrastructure, affecting data availability and service continuity.

+ **Resource Contention and Scalability Issues**<br/>
  Having all components (web server, application server, and database) on the same server can lead to resource contention. Competing for CPU, memory, and I/O resources can degrade performance and complicate problem diagnosis. This monolithic setup is also challenging to scale, as adding more resources to a single server does not proportionally improve performance.

By addressing these issues and implementing best practices, this infrastructure can be further optimized for security, performance, and scalability.
