# Additional Domains Only

**Technical Name:** AdditinalDomainsOnly

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `Additional Domains Only` parameter is used to specify if the Pathlock Cloud GRC platform should only consider additional domains beyond the primary domain configured in the system for certain operations related to the organization's Active Directory (AD) structure. This includes but is not limited to synchronization tasks, user authentication, and the application of security policies to users from specified additional domains.

**Business Impact:**

Configuring this parameter enables organizations to finely tailor their GRC platform's interaction with their IT ecosystem, specifically in multi-domain environments. It can significantly impact how security, compliance, and risk management policies are applied and enforced across different subdivisions, departments, or geographic locations within the same organization.

**Technical Impact when configured:**

- When enabled, this setting directs the system to ignore the primary domain's users and objects and instead focus on those within the specified additional domains.
- It affects user authentication processes, security policy assignments, and how the system interacts with the Active Directory structure for fetching and synchronizing data.

**Example Scenario:**

An organization with a global presence has separate AD domains for each country it operates in. The primary domain is used for corporate headquarters, while additional domains are designated for each country. By enabling `Additional Domains Only`, the company can ensure that GRC policies specific to regulatory requirements of each country are applied only to the users and objects within those respective domains, without affecting the corporate domain.

**Related Settings:**
- AdditinalDomainsCustomPassword
- AdditinalDomainsCustomUser

**Best Practices:** 
- Configure `Additional Domains Only` in complex AD environments where there is a clear distinction between the primary domain and additional domains requiring separate management and policy enforcement.
- Avoid configuring this setting in single-domain environments or when uniform policy application across all domains is required.