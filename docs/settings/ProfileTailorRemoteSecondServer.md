# Pathlock Remote Second Server

**Technical Name:** ProfileTailorRemoteSecondServer

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ProfileTailorRemoteSecondServer` parameter is designed to configure a secondary server for Pathlock's cloud-based GRC (Governance, Risk Management, and Compliance) platform. This setting is specifically aimed at enhancing the robustness of Configuration Sync operations by allowing organizations to have a backup server in place, ensuring continuous operation and data sync across multiple server environments.

**Business Impact:**

Implementing a Remote Second Server enhances the operational resilience of the Pathlock GRC platform by providing redundancy. This is crucial for organizations that rely heavily on real-time data availability for security, risk, and compliance management, as it minimizes downtime and ensures that GRC activities can continue unimpeded during primary server outages.

**Technical Impact when configured:**

When configured, the `ProfileTailorRemoteSecondServer` parameter ensures that there is a secondary server setup that can take over or mirror the operations of the primary server seamlessly. This redundancy can prevent data loss and ensure the reliability of configuration synchronization between the Pathlock Platform and connected third-party systems or applications.

**Examples Scenario:**

Imagine a financial institution that utilizes the Pathlock platform for managing its compliance with financial regulations. By setting up a remote second server through the `ProfileTailorRemoteSecondServer` parameter, the institution ensures that, in the event of a failure with their primary server, their GRC processes continue running smoothly. This redundancy is crucial during financial audits or when real-time risk assessment data is essential for decision-making.

**Related Settings:**

- `ConfigurationSyncServers`
- `Portal_ShowProductHeader`

**Best Practices:** 

- **Configure when:** You have critical operations that require high availability and cannot afford downtime.
- **Avoid when:** Your organization does not have the infrastructure to support multiple servers or where the GRC processes are not critical to real-time decision-making.