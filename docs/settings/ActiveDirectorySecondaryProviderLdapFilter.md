**Technical Name:** ActiveDirectorySecondaryProviderLdapFilter

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The ActiveDirectorySecondaryProviderLdapFilter parameter is used to define custom filters for LDAP queries within the context of a secondary Active Directory provider. This parameter allows for the specification of additional conditions or attributes that must be met for objects (such as users or groups) to be included in the synchronization process from Active Directory to the Pathlock Cloud GRC platform.

**Business Impact:**

Configuring this parameter enables organizations to fine-tune which objects are synchronized with Pathlock Cloud GRC, improving security by ensuring only relevant users and groups are managed and audited. It supports compliance with internal policies and external regulations by enabling finer control over the scope of users and groups subjected to Pathlock's GRC processes.

**Technical Impact when configured:**

When configured, this filter affects how the Pathlock platform interacts with the Active Directory, specifically modifying the set of users and groups that are imported. This can impact performance, efficiency, and scope of compliance and security policies applied within the Pathlock platform.

**Examples Scenario:**

- **Filtering by Organization Unit (OU):** If an organization wants to synchronize users from a specific OU, the filter can be configured to include only users within that OU, for instance, `(ou=FinanceDepartment)`.
- **Excluding Specific Accounts:** To exclude service accounts or other non-human entities, the filter can be set to exclude objects based on certain attributes, e.g., `(userAccountControl:1.2.840.113556.1.4.803:=2)` to exclude disabled accounts.

**Related Settings:**

- ActiveDirectorySecondaryProviderCustomDomains
- ActiveDirectorySecondaryProviderAdditinalDomains

**Best Practices:** configure when you need to limit the scope of synchronized objects to meet specific security or compliance requirements; avoid when full synchronization of all Active Directory objects is required for comprehensive management and oversight.