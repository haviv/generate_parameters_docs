# Check Dynamic SoD On Log Records With Changes Only

**Technical Name:** CheckDynamicSoDOnLogRecordsWithChangesOnly

**Category:** SOD

**Default Value:** 

**Impact Level:** High

**Description:** This parameter controls whether the Pathlock Cloud GRC platform checks for Segregation of Duties (SoD) violations dynamically on log records that actually have changes. It ensures that SoD checks are only performed on meaningful data modifications, improving performance and focusing compliance efforts on significant changes.

**Business Impact:** Enabling this setting helps organizations minimize unnecessary SoD checks, leading to more efficient audit and compliance processes. It focuses resources on reviewing changes that could potentially violate SoD policies, reducing overhead and enhancing the effectiveness of governance, risk, and compliance strategies.

**Technical Impact when configured:** When enabled, the system will insert SoD violation records into the database only when there is a change in the user data that potentially violates dynamic SoD policies. This selective logging reduces data clutter and improves the relevancy of SoD violation investigations.

**Examples Scenario:** A user is promoted and gains additional roles that, combined with their existing roles, could create a conflict of interest. Only if these roles are changed and potentially violate SoD policies, a record is created for review. This ensures that the compliance team focuses on reviewing and addressing only those changes that have a direct impact on the organization's SoD policy.

**Related Settings:** 

- `SodResolverConfig_RolesInSolutionFactor`
- `IsNewButtonShowInReports`

**Best Practices:** configure when you wish to optimize the performance of dynamic SoD violation checks and focus on significant data changes. Avoid when comprehensive logging of all user data changes, regardless of their relevance to SoD violations, is required for audit or other purposes.