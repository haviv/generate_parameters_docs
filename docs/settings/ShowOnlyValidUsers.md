# Show Only Valid Users

**Technical Name:** ShowOnlyValidUsers

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

The ShowOnlyValidUsers parameter controls the visibility of users within certain views or reports in the Pathlock Cloud GRC platform by filtering out users that do not meet specific validity criteria. This ensures that only users who are currently active and have valid roles or permissions within the system are displayed.

**Business Impact:**

Using the ShowOnlyValidUsers parameter can significantly enhance the operational efficiency of GRC processes by focusing on active and relevant user profiles. It helps in streamlining audit and compliance activities, by eliminating the clutter of invalid, outdated, or irrelevant user data. This can contribute to a more accurate risk assessment and compliance reporting.

**Technical Impact when configured:**

When the ShowOnlyValidUsers parameter is configured, the system's underlying logic filters the user data to exclude any entries for users who do not qualify as "valid" based on predefined criteria. This can affect various reports and views within the platform, potentially leading to more streamlined and relevant data representation.

**Examples Scenario:**

A company wishes to conduct an audit on the access rights of its employees within a specific system. By enabling the ShowOnlyValidUsers parameter, the audit report will include only those users who are currently active or have valid access, thereby simplifying the audit process and providing a clearer audit trail.

**Related Settings:**

- UserGroupsToUsers
- SoxUserViolations

**Best Practices:** configure when you need accurate and up-to-date user data for GRC processes, avoid when performing comprehensive audits that require visibility into all user accounts, including those that are inactive or have been decommissioned.