# Custom Domains

**Technical Name:** CustomDomains

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CustomDomains` parameter allows for the configuration of custom domain names within the Pathlock platform. This is specifically relevant for integrating Pathlock with an organization's Active Directory (AD) setup, enabling tailored authentication mechanisms and streamlined user access based on the organization's domain naming conventions.

**Business Impact:**

Implementing custom domains enhances the alignment of Pathlock GRC platform with an organization's internal domain structures, simplifying user management and authentication processes. It ensures that employees can access the GRC platform using the same credential sets they use within the rest of the organization's IT ecosystem, improving security posture and user experience.

**Technical Impact when configured:**

Configuring the `CustomDomains` parameter impacts how authentication requests are handled, directing them through the specified custom domains. This can affect login processes, Active Directory synchronizations, and potentially the routing of authentication tokens, depending on the organization's specific infrastructure.

**Example Scenario:**

An organization wishes to streamline access to the Pathlock GRC platform for its users, leveraging the same login credentials and domain structure used across its internal systems. By configuring `CustomDomains` to match the organization's primary AD domain, users can authenticate directly with their standard company credentials, eliminating the need for separate logins or credential sets for accessing the GRC platform.

**Related Settings:**

- ActiveDirectoryProvider
- CompanyEmployees

**Best Practices:** 

- Configure **when**: Establishing Pathlock GRC within an organization's IT landscape to leverage existing Active Directory infrastructures for authentication purposes.
- Avoid **when**: The organization does not use Active Directory or has a policy against custom domain configuration for third-party platforms.