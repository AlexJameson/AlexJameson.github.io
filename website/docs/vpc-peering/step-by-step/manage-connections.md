---
id: connections
title: Manage connections
---

You can create and manage connections between your Virtual Private Cloud (VPC) and outside networks.

:::caution

Currently, only connections to AWS networks are supported.

:::

## Create a connection {#create-a-connection}

:::caution

You can't change the parameters of the connection after you create it.

:::

Perform the following steps to create a peer connection:

1. Go to the [console](https://app.double.cloud).

1. In the list of services, select **VPC**.

1. On the **Connections** tab, click **Create connection**.

1. Specify the **AWS account ID** you want to connect to.

1. Specify the **AWS VPC ID**.

1. Provide your **AWS IPv4 CIDR**. You can also add a **AWS IPv6 CIDR** if you have such a range.

1. Select your **VPC Region** and a zone within this region.

1. Select your **DoubleCloud Network** to peer with.

1. Click **Create connection**.

Your connection is created, but you also need to enable it on the AWS side as shown in the next section:

1. Open the AWS console.

1. Go to the **Peering connections** section.

1. Select your VPC peering connection and choose **Actions** → **Accept Request**.

1. In the confirmation dialog, choose **Yes, Accept**.

## Delete a connection {#modify-a-connection}

1. Go to the [console](https://app.double.cloud).

1. In the list of services, select **VPC**.

1. Switch to the **Connections** tab and select a connection to delete.

1. Click ![vertical-ellipsis](../../../static/img/logo.svg) and select **Delete**.

**See also**:

* [Concepts - Connections](../concepts/connections.md)
