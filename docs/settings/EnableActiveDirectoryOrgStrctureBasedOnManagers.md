# Enable Active Directory Org Structure Based On Managers

**Technical Name:** EnableActiveDirectoryOrgStrctureBasedOnManagers

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter allows organizations to structure their users in the Pathlock platform based on hierarchical manager relationships as defined within Active Directory. When enabled, the platform will organize and present users according to their manager-subordinate relationships, facilitating an accurate reflection of the organizational chart within the Pathlock environment.

**Business Impact:**

Enabling this parameter ensures that the organizational structure within Pathlock mirrors the actual hierarchy of the organization as defined in Active Directory. This alignment enhances visibility into direct and indirect reporting lines, thereby improving governance, risk management, and compliance (GRC) processes. It aids in better access control decisions, streamlined user management, and more targeted compliance reporting.

**Technical Impact: when configured**

When this parameter is configured, Pathlock dynamically adjusts the representation of the organizational structure to match Active Directory. This includes automatic updates whenever changes occur in Active Directory, such as a user changing departments, new hires, or when employees leave the organization. This real-time synchronization ensures that GRC processes are always aligned with the current organizational structure.

**Examples Scenario:**

A company wants to ensure that access rights and permissions in their financial system are directly aligned with their current managerial hierarchy. By enabling this parameter, when an employee receives a promotion and becomes a manager, their new direct reports are automatically aligned under them in the Pathlock platform. This ensures that the employee can approve access requests and review compliance reports for their direct reports, enhancing the efficiency of access management and compliance audits.

**Related Settings:**

- ActiveDirectoryAccountExpirationDateAddAddiotnalDay

**Best Practices:** 

- **Configure when:** You have a dynamically changing organizational structure and wish to maintain an accurate representation of managerial hierarchies within Pathlock.
- **Avoid when:** Your organization does not use Active Directory to manage user accounts or when the organizational structure in Active Directory does not reflect the actual managerial reporting lines.