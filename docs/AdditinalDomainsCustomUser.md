# Additional Domains Custom User

**Technical Name:** AdditinalDomainsCustomUser

**Category:** User Management

**Default Value:** None

**Impact Level:** High

**Description:**

A configuration parameter designed to enable the integration of multiple Active Directory domains within the Pathlock Cloud GRC platform. This parameter is critical for organizations operating across various domains who need to manage access, compliance, and security across all user accounts seamlessly.

**Business Impact:**

The correct configuration of this parameter ensures that user accounts across different Active Directory domains are properly identified and managed, supporting compliance and security policies. It enables the organization to extend its GRC capabilities across all operational domains, enhancing visibility and control over user access and activities.

**Technical Impact when configured:**

- Enables the Active Directory provider within Pathlock to iterate over multiple domains.
- Facilitates the addition of users from additional domains not primarily configured in the Pathlock system.
- Ensures comprehensive coverage and control of user access and activities across multiple domains.

**Examples Scenario:**

An organization operates across three different domains – North America, Europe, and Asia. Each domain has its own set of user accounts managed under separate Active Directory instances. By configuring the `AdditinalDomainsCustomUser` parameter, the organization can manage GRC policies across all user accounts from a centralized platform, ensuring compliance and security standards are uniformly applied.

**Related Settings:**

- `AdditinalDomains`
- `AdditinalDomainsCustomPassword`

**Best Practices:** 

- **Configure when:** You are managing a multi-domain environment and need centralized GRC management across all user accounts.
- **Avoid when:** Your organization operates under a single domain or does not require integration of multiple Active Directory instances.