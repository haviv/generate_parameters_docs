# Cloud Client Reconnect Attempts Check Every

**Technical Name:** CloudClientReconnectAttemptsCheckEvery

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** 

This parameter determines the frequency (in minutes) with which the system checks the connection status of cloud clients and attempts reconnection if necessary. It ensures continuous communication between the Pathlock Cloud GRC platform and its cloud clients, thereby maintaining the integrity and reliability of cloud-based Governance, Risk, and Compliance (GRC) operations.

**Business Impact:**

Proper configuration of this parameter minimizes the risk of data loss or miscommunication due to interrupted service between the cloud client and the GRC platform. It ensures that compliance monitoring and risk assessment processes are continuous, without disruption, which is crucial for maintaining the organization's security posture and compliance status.

**Technical Impact: when configured**

- **Increased Reliability:** Ensures that cloud clients maintain a stable and persistent connection with the Pathlock Cloud GRC platform.
- **Improved Monitoring:** Facilitates real-time monitoring and alerts by minimizing downtime or disconnections.
- **Enhanced Compliance:** Supports continuous compliance and risk management processes by reducing the chances of interrupted connections.

**Example Scenario:**

An organization has deployed the Pathlock Cloud GRC platform to monitor compliance with regulatory standards. To ensure that their cloud-based services are continuously assessed without interruptions, the `CloudClientReconnectAttemptsCheckEvery` parameter is configured to check the connection status every 5 minutes. This proactive measure addresses any potential disconnections quickly, thereby maintaining uninterrupted compliance monitoring and reporting.

**Related Settings:**

- CloudClientMissingHeartbeatErrorThresholdInMinutes

**Best Practices:** 

- **Configure when:** Continuous communication between the cloud client and the GRC platform is critical for your organization's operational, compliance, or security needs.
- **Avoid when:** The system's performance might be negatively impacted by too frequent reconnection attempts, or if the cloud environment is stable enough that fewer checks are required. Adjust the parameter according to the stability of your cloud connectivity and the criticality of continuous monitoring for your business operations.