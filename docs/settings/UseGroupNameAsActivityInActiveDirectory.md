# Use Group Name As Activity In Active Directory

**Technical Name:** UseGroupNameAsActivityInActiveDirectory

**Category:** Configuration

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:** This parameter configures the system to utilize the group name attribute from Active Directory (AD) as an activity identifier within the Pathlock Cloud GRC platform.

**Business Impact:** Enabling this feature can significantly streamline user activity tracking and role-based access control by aligning SAP roles with their corresponding Active Directory groups. This alignment facilitates more efficient management of permissions, easier audit trails, and improved compliance with security policies.

**Technical Impact when configured:** When this parameter is configured, the system will interpret the Active Directory group name as the role or activity name within SAP. This alignment allows for more straightforward mapping of permissions and roles between SAP and AD, enabling automated updates and synchronization of roles based on AD group membership changes.

**Example Scenario:** 
- A company implements a new security policy requiring all SAP transactions to be aligned with specific AD groups for tighter security and easier auditability. 
- By enabling this parameter, the IT department can directly map SAP transaction codes to AD groups. 
- Consequently, when a user is added to an AD group, they automatically gain access to the corresponding transactions in SAP, streamlining the access management process.

**Related Settings:** 
- ADMethodsAccountManagement
- GetAuthorizations

**Best Practices:** 
- **Configure when** you have a clear mapping between AD groups and SAP roles to enhance security measures and compliance adherence.
- **Avoid when** there is no direct correlation between AD groups and SAP roles, or if such a mapping could result in unintended access rights being granted due to a misalignment of group purposes and access requirements.