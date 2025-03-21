# SoD Resolver Max No Of Activities To Keep

**Technical Name:** SodResolver_MaxNoOfActivitiesToKeep

**Category:** SOD

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls the maximum number of activities related to Separation of Duties (SoD) that the system retains for reporting and analysis purposes.

**Business Impact:**

Setting an appropriate value for this parameter ensures that organizations can balance between having sufficient historical data for audits and analysis, and maintaining optimal system performance by not overloading with unnecessary data. 

**Technical Impact when configured:**

- Improves system performance by limiting the number of activities stored.
- Ensures compliance requirements are met by retaining necessary audit trails.
- Helps in identifying and resolving SoD conflicts efficiently with a manageable dataset.

**Examples Scenario:**

In a scenario where an organization needs to conduct a quarterly audit of SoD activities, setting this parameter to keep the last quarter's activities ensures auditors have relevant data without extraneous details from further back, streamlining the audit process.

**Related Settings:** 

- SoDCheckEmployeeSoDForMultiSystemOnly
- SodFullReportRun

**Best Practices:** 

- **Configure when:** Regular auditing and analysis of SoD activities is needed, but there's also a need to keep the system's performance optimized.
- **Avoid when:** There is a requirement to keep a detailed, long-term record of all SoD activities for extended periods. In such cases, consider adjusting the value to meet compliance while balancing system performance.