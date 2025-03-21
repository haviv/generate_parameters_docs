**Technical Name:** NumberOfIdocsToDisplay

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `NumberOfIdocsToDisplay` parameter controls the number of IDoc (Intermediate Document) entries displayed in reporting interfaces within the Pathlock Cloud GRC platform. IDocs serve as data containers for secure and reliable message exchange between different systems. Adjusting this parameter enables users to tailor the volume of IDoc information retrieved and displayed, optimizing the interface for usability and performance based on specific user needs or system capabilities.

**Business Impact:**

The setting directly impacts operational efficiency for administrators and users who rely on IDoc information for auditing, tracking, and monitoring system integrations and data exchanges. By fine-tuning the number of IDocs displayed, organizations can manage the balance between comprehensive data accessibility and system performance, enabling faster decision-making and issue resolution while potentially reducing system load.

**Technical Impact: when configured**

When configured, this parameter influences the system's response time and the accessibility of IDoc data for reporting purposes. A higher number of IDocs displayed can increase the time required to generate reports, affecting system performance. Conversely, a lower number might limit visibility into transaction histories and data exchanges, which could impact troubleshooting efforts and audit completeness.

**Examples Scenario:**

An administrator wants to review all IDoc exchanges from the previous day within a specific timeframe. Given concerns over system performance during peak hours, the administrator adjusts the `NumberOfIdocsToDisplay` to a lower value to ensure the report generates quickly, allowing for a rapid review of critical data exchanges without significantly impacting system resources.

**Related Settings:** 

- TransactionHistoryOrganizationInformationDataSource_UsersSelector

**Best Practices:** configure when the need for detailed IDoc information is critical for audit or reporting purposes and system performance is not a primary concern. Avoid when system performance could be adversely affected by the large volumes of data retrieval, or when a high-level overview suffices for operational needs.