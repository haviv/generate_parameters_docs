# Create User Groups Of Type

**Technical Name:** ImportManagersToWFUserGroupTypeId

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ImportManagersToWFUserGroupTypeId` parameter is used within the Pathlock Cloud GRC platform to automatically import and assign managers to specific user groups based on their organizational unit assignments. This helps in streamlining user group assignments and ensuring that managers have the necessary access to perform risk, compliance, and security management activities efficiently.

**Business Impact:**

Utilizing this parameter can significantly impact how organizations manage their governance, risk, and compliance (GRC) strategy by automating the process of assigning managers to relevant user groups. This not only saves administrative time but also ensures that risk and compliance controls are consistently applied across the organization, reducing the likelihood of human error.

**Technical Impact when configured:**

When configured, this parameter automatically populates user groups with managers from specified organizational units. It ensures that all managers have appropriate access rights and memberships to perform their roles effectively within the GRC platform, aligning with the business's security, risk management, and compliance requirements.

**Examples Scenario:**

A company wants to automate the process of adding managers to a user group responsible for reviewing compliance reports. By configuring the `ImportManagersToWFUserGroupTypeId` parameter, the system will automatically identify managers based on their roles within the organization and add them to the compliance review user group, thereby streamlining the compliance management process.

**Related Settings:**

- UserGroupDescriptionTemplate
- UserGroupTypeId
- WorkflowApprovalGroupRelations

**Best Practices:** 

- **Configure when:** Setting up automated processes for populating user groups with managers to ensure that governance, compliance, and risk management tasks are appropriately delegated and managed.
- **Avoid when:** Manual assignment of users to groups is preferred due to specific organizational requirements, or when the automated inclusion of managers into groups could result in excessive access rights or security concerns.