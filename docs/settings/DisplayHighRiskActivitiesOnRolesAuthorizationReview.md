# Display No. of High Risk Activities column

**Technical Name:** DisplayHighRiskActivitiesOnRolesAuthorizationReview

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Display No. of High Risk Activities column parameter enables or disables the visibility of a column that shows the number of high risk activities within roles in the roles authorization review report. This parameter is crucial for identifying roles with a high potential for abuse or misuse, facilitating a focused review and risk management process.

**Business Impact:**

Enabling this parameter helps organizations to quickly identify roles with a high number of risky activities. This identification aids in mitigating potential security threats and ensuring compliance with internal and external audit requirements by prioritizing review efforts on roles that pose the highest risk.

**Technical Impact when configured:**

When configured to display the column, users are able to see a quantitative assessment of risk directly in the roles authorization review report. This can influence decision-making processes related to role redesign, user access reviews, and Segregation of Duties (SOD) policy enforcement.

**Example Scenario:**

Consider a scenario where an organization is undergoing a compliance audit and needs to demonstrate adequate controls over high-risk activities within their ERP system. By enabling this parameter, the organization can easily generate a report highlighting roles with a high concentration of high-risk activities, thereby facilitating a focused audit of those roles to ensure appropriate controls are in place.

**Related Settings:** 

- DisableRoleRequestType
- DisableValidityCheckForHRData

**Best Practices:** 

- Configure when: Preparing for audits or when undertaking a proactive review of security roles within your organization.
- Avoid when: Detailed role reporting is not a requirement, or if the additional column significantly impacts report performance or readability.