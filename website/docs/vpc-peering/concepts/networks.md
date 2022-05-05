---
id: networks
title: Cloud Networks
---

Cloud networks are used for transferring information between cloud resources and connecting resources to the internet. Resources are ClickHouse and Apache Kafka® clusters.

Networks allow users to create resources in target regions. Access to the networks is regulated by allow lists that do not depend on networks. You can use [connections](connections.md) to peer networks between different VPCs.

## Resources availability within or outside the networks

By default, users can connect to resources only from IPs specified in the Allow list.

You can select an existing network when you create a resource. Other services, such as Transfers and Visualization, have access to these resources if they are not blocked by Allow lists.

**See also**:

* [Instructions - Manage networks](../step-by-step/networks)
