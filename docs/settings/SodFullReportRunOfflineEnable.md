# SoD Full Report Run Offline Enable

**Technical Name:** SodFullReportRunOfflineEnable

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

Enables the generation and transmission of Separation of Duties (SoD) full report in an offline mode. This parameter controls whether the SoD full report generation process runs in the background, allowing system resources to be used more efficiently and not impact the performance of live user sessions.

**Business Impact:**

This setting significantly impacts how administrators and compliance officers manage and review SoD violations across users, roles, and permissions within the organization. By enabling offline report generation, it ensures that the system's performance remains optimal during peak business hours, while still allowing for comprehensive SoD audits to be performed.

**Technical Impact when configured:**

When enabled, the system queues SoD full report generation tasks and executes them without immediately consuming resources that are critical for day-to-day business operations. This leads to better system performance and user experience, while still maintaining a high standard of security and compliance vigilance.

**Examples Scenario:**

- **Scenario:** A compliance officer needs to generate a full SoD report to audit access rights and potential conflicts across all users within the system. This report is particularly resource-intensive due to the size of the organization and the complexity of the SoD rules configured.
  
  **With SodFullReportRunOfflineEnable:** The report is generated in an offline process, ensuring that the compliance officer receives a comprehensive view of SoD violations without degrading system performance for other users.

**Related Settings:**

- `SoxForbiddenCombinations`
- `SoCheckUserSoDByEmployeeAuthorizations`

**Best Practices:** 

- **Configure when:** There is a need for regular, comprehensive SoD audits without impacting system performance. Ideal for organizations with large user bases and complex SoD configurations.
  
- **Avoid when:** The organization is small or the system is not heavily utilized, making real-time report generation feasible without significant performance impacts.