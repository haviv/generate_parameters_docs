# Send Roles In Bulk To SAP

**Technical Name:** SendRolesInBulkToSAP

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:**

The "Send Roles In Bulk To SAP" parameter is associated with automated processes that handle mass role assignments or updates in SAP systems, particularly under urgent or emergency circumstances.

**Business Impact:**

Enabling this parameter streamlines the process of granting, updating, or revoking SAP roles in bulk, thereby significantly reducing the time and potential errors associated with manual input. This functionality is vital during critical situations where rapid access adjustments are necessary to ensure business continuity and compliance with security protocols.

**Technical Impact when configured:**

When enabled, this parameter allows the Pathlock Cloud GRC platform to automatically send a bulk list of roles to SAP systems during the execution of specific workflow actions. This process facilitates efficient role management by bypassing the need for individual role assignment transactions, which can be time-consuming and prone to errors.

**Examples Scenario:**

An organization needs to quickly grant emergency access to a group of users in response to an unexpected audit requirement. By enabling "Send Roles In Bulk To SAP," the admin can ensure that all affected users receive the necessary roles swiftly and accurately, without the need to individually process each user.

**Related Settings:** 

- SqlErrorForPKViolationRetries

**Best Practices:** 

Configure when:
- Rapid changes in user role assignments are needed in response to emergency situations or critical business processes.

Avoid when:
- Individual role assignments are preferred due to specific audit or compliance requirements that necessitate a more granular level of control and tracking.