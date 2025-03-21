**Technical Name:** ActiveDirectorySecondaryProviderAdditinalDomains

**Category:** Configuration

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter specifies additional domain names that can be used by the Pathlock Cloud GRC platform when configuring Active Directory (AD) for secondary provider scenarios. It allows the platform to recognize and manage user and group information across multiple AD domains that are not the primary domain configured in the system.

**Business Impact:**

Configuring additional domains expands the platform's ability to manage users and permissions across different parts of an organization that may be spread across multiple domains. This can be particularly useful in complex corporate structures where users need to have access to resources or need to be monitored across different AD domains.

**Technical Impact when configured:**

When this parameter is configured, the Pathlock Cloud GRC platform will be able to query, recognize, and import user and group details from the specified additional domains. This ensures comprehensive coverage and control over access rights, compliance checks, and risk assessments carried out by the platform across an organization's IT environment.

**Examples Scenario:**

A multinational corporation with entities in multiple countries operates different AD domains for each country. By configuring this parameter, the corporation's IT department can manage access rights, monitor compliance, and perform risk assessments seamlessly across all international branches from a single Pathlock Cloud GRC platform instance.

**Related Settings:**

- ActiveDirectoryProviderTestAllProperties

**Best Practices:** 

- Configure when your organization operates across multiple AD domains to ensure comprehensive management and oversight.
- Avoid configuration without proper validation of domain names to prevent potential security risks or mismanagement of user and group details.