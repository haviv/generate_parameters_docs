# Additional Domains Custom Password

**Technical Name:** AdditinalDomainsCustomPassword

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter allows for the configuration of custom passwords for accessing additional Active Directory domains beyond the primary domain configured in Pathlock GRC's organizational structure providers. This feature is particularly useful in complex environments where users, roles, or resources span multiple domains with distinct security requirements.

**Business Impact:**

Implementing custom passwords for additional domains enhances the security posture by allowing for unique authentication credentials across different domains. This reduces the risk of lateral movement attacks within an organization's network. Moreover, it supports compliance with security policies that mandate separate credentials for access to differentiated resources or environments.

**Technical Impact when configured:**

Upon configuration, Pathlock GRC will use the specified custom passwords instead of default or single-domain credentials to authenticate users or synchronize data across the specified additional Active Directory domains. This ensures that authentication processes are aligned with specific domain requirements and security policies.

**Examples Scenario:**

- An organization has multiple domains for different business units, e.g., "finance.company.com" and "operations.company.com". By specifying custom passwords for each domain, the finance and operations teams can have their unique credentials, enhancing domain-specific security.

**Related Settings:**

- `AddCompanyCode`
- `AdditinalDomains`

**Best Practices:** 

- **Configure when:** multiple Active Directory domains are in use, and there is a need for distinct authentication credentials to meet security or operational requirements.
- **Avoid when:** there is only a single Active Directory domain, or if unified credentials across domains meet the organization's security policies and operational needs.