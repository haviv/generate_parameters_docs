# Cloud Client Reconnect Wait Time In Seconds

**Technical Name:** CloudClientReconnectWaitTimeInSeconds

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Cloud Client Reconnect Wait Time In Seconds parameter specifies the duration in seconds that the system waits before attempting to reconnect a cloud client after an unexpected disconnection or timeout.

**Business Impact:**

Setting an appropriate wait time helps in balancing between immediate reconnection attempts, which might overload the server during transient network issues, and too long delays, which could impact operational efficiency and real-time monitoring activities.

**Technical Impact when configured:**

Configuring this parameter affects the cloud client's resilience to network instabilities and server connectivity issues. It determines how quickly the client system tries to re-establish its connection to the server, potentially reducing downtime but also influencing network traffic and server load.

**Examples Scenario:**

In a scenario where a cloud client faces intermittent network issues, setting an optimal Cloud Client Reconnect Wait Time can ensure that the client attempts to reconnect only after giving enough time for the network to stabilize, thus avoiding excessive network requests.

**Related Settings:**

- CloudClientMissingHeartbeatWarningThresholdInMinutes

**Best Practices:** configure when network reliability is a concern or server load needs to be managed; avoid when continuous, real-time connectivity is crucial for business operations.