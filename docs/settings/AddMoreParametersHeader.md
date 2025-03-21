# Add More Parameters Header

**Technical Name:** AddMoreParametersHeader

**Category:** User Management

**Default Value:** (No default value specified)

**Impact Level:** Medium

**Description:**

The 'Add More Parameters Header' parameter is designed to enhance the management and customization of user settings, particularly in the context of integrating additional Microsoft Active Directory (MS AD) domains. This parameter allows for the extension of the existing domain list by adding custom domains, which in turn supports the customization of user access management, permissions, and security settings across multiple domains.

**Business Impact:**

Utilizing the 'Add More Parameters Header' can significantly streamline the process of managing user access across multiple MS Active Directory domains. It enables organizations to consolidate and simplify their user management processes, ensuring that users have the appropriate access rights based on their roles, irrespective of the domain. This is especially critical in large or complex IT environments where users may need to access resources across several domains.

**Technical Impact when configured:**

Configuring this parameter allows for the customization and expansion of domain-based user management settings within the Pathlock GRC platform. It facilitates the addition of custom MS AD domains to the existing pre-configured list, enabling administrators to specify unique settings and permissions for each added domain. This enhances the platform's flexibility in managing broader user access policies and compliance requirements.

**Examples Scenario:**

An organization is using Pathlock GRC for their compliance and user access management needs across their multiple MS Active Directory domains. By setting the 'Add More Parameters Header' parameter, they can add new AD domains that were recently acquired during a merger. This ensures that the new domains are also under the purview of Pathlock's GRC platform, allowing centralized management of user access and compliance across all domains.

**Related Settings:**

- AdditinalDomains
- AddCharsToLastPatternSetField

**Best Practices:** 

- **configure when:** You are managing user permissions and security across multiple MS Active Directory domains, especially in scenarios involving mergers, acquisitions, or expansion.
  
- **avoid when:** The organization operates within a single domain, or there is no requirement for managing additional custom domains.
