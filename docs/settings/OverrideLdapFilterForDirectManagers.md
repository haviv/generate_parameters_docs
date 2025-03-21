# Override Ldap Filter For Direct Managers

**Technical Name:** OverrideLdapFilterForDirectManagers

**Category:** User Management

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The `OverrideLdapFilterForDirectManagers` parameter is designed to customize the LDAP filter used for identifying direct managers within the organization's Active Directory structure. This is particularly useful for organizations with complex hierarchies or those that require a customized definition of what constitutes a direct manager in their LDAP queries.

**Business Impact:**

Configuring this parameter ensures that the organization's reporting structure is accurately reflected within the Pathlock Cloud GRC platform. It allows organizations to maintain compliance with internal policies and external regulations by accurately mapping employee-manager relationships, which is critical for processes such as access approvals, segregation of duties (SOD) analysis, and audit trails.

**Technical Impact when configured:**

When this parameter is configured, the system overrides the default LDAP filter for fetching direct manager data, allowing for customized queries that align with the organization's unique structure and requirements. This may affect the speed and accuracy of data retrieval related to direct manager information, depending on the complexity and efficiency of the customized filter.

**Examples Scenario:**

An organization with a complex structure where the direct manager is not located in the immediate next level of hierarchy but is determined based on a combination of factors such as department, location, and project assignment, may use this parameter to accurately define direct managers for all employees in the system.

**Related Settings:** Not specified due to lack of direct references in the provided code.

**Applicable Workflows Actions:** Not applicable.

**Best Practices:** 

- Configure when: The default LDAP query does not accurately reflect direct manager-employee relationships in your organization, affecting compliance and reporting accuracy.
  
- Avoid when: The default settings adequately reflect your organizational structure, or if the custom LDAP queries could lead to performance issues without providing significant benefits.