# SoD Full Report Run Offline Users

**Technical Name:** SodFullReportRunOfflineUsers

**Category:** SoD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls whether the Separation of Duties (SoD) full reports for users are run in an offline mode. It is intended to optimize the performance of the PathlockGRC platform during intensive SoD report generation processes by allowing these processes to occur without real-time computational load, thereby not impacting the system's online operational efficiency.

**Business Impact:**

Enabling this feature can significantly reduce the system's load during heavy reporting periods, ensuring that the Pathlock GRC platform remains responsive for other critical governance, risk, and compliance (GRC) functions. For organizations with a large user base and complex SoD policies, this feature is critical in maintaining operational efficiency and ensuring timely compliance reporting.

**Technical Impact when configured:**

When enabled, SoD reports for users will be generated in an offline mode. This means that the system will utilize saved snapshots of user roles and permissions instead of querying live data. While this reduces system load, it is essential to ensure that the snapshots are updated regularly to reflect the current state of user access accurately.

**Examples Scenario:**

- During the end of the fiscal year, a financial institution needs to run comprehensive SoD reports for all its users to comply with internal audits and regulatory requirements. Enabling SoD Full Report Run Offline Users allows the institution to generate these reports without slowing down other critical operations on the Pathlock GRC platform.

**Related Settings:**

- SoxForbiddenCombinations
- SoxGroupsContents

**Best Practices:** 

- **Configure when:** Anticipating heavy reporting periods or when performance impacts are detected during real-time SoD report generation.
- **Avoid when:** Up-to-the-minute accuracy of SoD reports is required, and the system resources are sufficient to handle real-time computations without impacting performance.