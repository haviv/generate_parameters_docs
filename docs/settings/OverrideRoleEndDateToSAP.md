# Override Role End Date To Sap

**Technical Name:** OverrideRoleEndDateToSAP

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The `OverrideRoleEndDateToSAP` parameter is designed to alter the behavior of how role end dates are handled within SAP role assignments. When enabled, this parameter allows for custom handling of role end date properties, overriding the standard SAP logic.

**Business Impact:**

Enabling this parameter can address specific compliance or operational requirements by ensuring that role assignments within SAP reflect accurate end dates as per organizational policies. This can reduce the risk of unauthorized access due to roles not being properly terminated at the intended time.

**Technical Impact when configured:**

Once configured, the system will bypass the default SAP process for assigning role end dates, allowing for custom implementations. This could be particularly useful in scenarios where roles need to be automatically adjusted based on specific criterias such as project end dates or contract terminations.

**Examples Scenario:**

A scenario in which an employee is assigned to a temporary project role within SAP, and the role needs to be automatically revoked upon the project's completion date. By configuring `OverrideRoleEndDateToSAP`, the organization can ensure that the role end date aligns with the project end date, thereby enforcing stricter access control and compliance with internal policies.

**Related Settings:** 

- DynamicSoDCreateEventForSingleUse

**Best Practices:** configure when

- There is a need for dynamic adjustment of role end dates based on non-standard criteria.
- Compliance requirements dictate more granular control over role assignments and terminations.

avoid when

- Standard SAP role end date handling meets organizational needs.
- There is no clear strategy for managing role end dates outside of the default SAP logic, as improper configuration could lead to security and compliance issues.