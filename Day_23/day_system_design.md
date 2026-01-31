# System Design Basics: Scalability & Load Balancing

## Problem Statement
A single server has inherent capacity limits:
- **1 server** → ~100 users
- **10,000 users** → server crashes, timeouts, slow responses

## Vertical Scaling

Increase the capacity of existing servers by adding more RAM, CPU, or better hardware.

### Advantages
- Easy to implement
- No architectural changes required
- Cost-effective for small scale

### Limitations
- Hardware capacity ceiling exists
- Single point of failure remains
- Becomes expensive at scale

> **Key Takeaway:** Vertical scaling is simple but limited and risky due to single point of failure.

## Horizontal Scaling

Distribute traffic across multiple servers to handle increased load.

### Advantages
- Nearly unlimited scalability
- Cost-effective server additions
- Built-in fault tolerance and high availability
- Industry standard for large-scale systems

### Limitations
- More complex architecture
- Requires load balancing infrastructure
- Data consistency challenges

> **Key Takeaway:** Horizontal scaling improves availability and supports massive traffic by distributing load across multiple servers.

## Load Balancer

Distributes incoming traffic across multiple servers, ensuring no single server becomes overwhelmed.

### Load Balancing Algorithms
- **Round Robin** — Distributes requests sequentially
- **Least Connections** — Routes to server with fewest active connections
- **IP Hash** — Routes based on client IP address

### Load Balancer Options
- **Hardware** — Physical devices
- **Software** — Nginx, HAProxy
- **Cloud-based** — AWS ELB, Google Cloud Load Balancing

### Advantages
- Improved performance and reliability
- Scalability through server addition/removal
- Fault tolerance via traffic rerouting
