# Activity To User Matrix Static And Real User Use Static As Base For The Report

**Technical Name:** ActivityToUserMatrixStaticAndRealUserUseStaticAsBaseForTheReport

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls how the Activity to User matrix report is generated when comparing static (pre-defined roles and activities) and real user data (actual user activities within the system). When enabled, the report uses the static data as the baseline for comparison rather than treating actual user data as the baseline.

**Business Impact:** Understanding how actual user activities compare against pre-defined roles and activities helps in identifying deviations and ensuring that users only have the access necessary to perform their job functions. This can be critical in maintaining a secure, compliant, and efficient access environment.

**Technical Impact when configured:** Enabling this setting shifts the perspective of the report, highlighting discrepancies where actual user activities extend beyond what is statically defined. This can assist in tightening security controls and improving compliance by identifying and rectifying excessive permissions.

**Example Scenario:** If an organization is undergoing a security audit and needs to demonstrate that users are not granted more permissions than those defined by their roles, enabling this setting would make discrepancies apparent, thereby facilitating the identification of users with excess privileges.

**Related Settings:** `FioriConnectorIdentifyBasedOnCatalogs` (as it pertains to identifying user activities based on specific catalogs, which could be related in assessing access and activity scopes).

**Applicable Workflow Actions:** The specific workflow actions relevant to this parameter would typically include generating reports, assessing user permissions against pre-defined roles, and auditing user activities.

**Best Practices:** 
- **Configure when:** Preparing for audits, assessing compliance against predefined roles, or when security and access governance are a priority.
- **Avoid when:** The organization prioritizes monitoring real user behavior without comparing it to static definitions, or if the static data is not up-to-date, which might result in misleading report outcomes.

**Context:** This parameter plays a critical role in Pathlock Cloud GRC's reporting functionality, enabling organizations to fine-tune how they monitor and compare user activities against predefined access controls and roles. Its configuration is essential for leveraging the platform's capabilities to maintain compliance, manage risk, and enhance security protocols effectively.