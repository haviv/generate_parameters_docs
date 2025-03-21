# Number of days back for usage of activities

**Technical Name:** SodResolverConfig_UsageDaysBack

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

This configuration parameter determines the number of days in the past for which activities within the system will be considered during the resolution of Segregation of Duties (SoD) conflicts. It specifies the historical period that should be examined to provide an accurate assessment of SoD violations.

**Business Impact:**

Setting an appropriate value for this parameter is critical for effective risk management. A shorter period may not provide a sufficient view of user activities to accurately detect and resolve conflicts, potentially leaving the organization exposed to unmitigated risks. Conversely, a very long period may include outdated information, leading to unnecessary resolutions or an overwhelmed administrative process.

**Technical Impact when configured:**

When configured, this parameter adjusts the scope of activity logs and data considered during the automated SoD conflict resolution process. This impacts the detection of potential SoD violations by either broadening or narrowing down the historical data used for analysis, directly influencing the effectiveness of controls in the GRC (Governance, Risk Management, and Compliance) environment.

**Examples Scenario:**

- **Scenario 1:** If an organization sets the parameter to 30 days, only the activities performed by users within the last month will be analyzed for potential SoD conflicts. This might be suitable for environments where roles and access rights change frequently.
  
- **Scenario 2:** Setting the parameter to 365 days might be necessary for organizations with less frequent access changes or for annual audit requirements, providing a comprehensive review of SoD conflicts over the past year.

**Related Settings:**

- SodResolverConfig_CoveragePercentageFactor
- SodResolverConfig_ExtraHighRiskFactor

**Best Practices:** Set the parameter based on the typical lifecycle of roles and permissions within the organization. A shorter period (e.g., 30-90 days) might be appropriate for dynamic environments, whereas a longer period (e.g., 180-365 days) could be better for organizations with stable access assignments or for thorough annual audits. Avoid setting the value too low to prevent missing relevant activities or too high to prevent analysis overload and potential performance impacts.