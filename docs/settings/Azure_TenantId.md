# Azure Tenant

**Technical Name:** Azure_TenantId

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**

The Azure_TenantId parameter specifies the unique identifier for the Azure Active Directory (Azure AD) tenant that Pathlock Cloud GRC integrates with for authentication and authorization services.

**Business Impact:**

Correct configuration of the Azure_TenantId ensures that Pathlock Cloud GRC can securely manage access to its resources, leveraging Azure AD for single sign-on (SSO) and multi-factor authentication (MFA) capabilities. This integration enhances the security posture by controlling who can access the platform, thereby protecting sensitive compliance and governance data.

**Technical Impact when configured:**

When the Azure_TenantId is configured, Pathlock Cloud GRC leverages Azure AD for authenticating users. This setup enables the platform to use Azure AD's robust security features, including conditional access policies and compliance checks, providing an additional layer of security.

**Examples Scenario:**

- **Scenario 1:** An organization wants to ensure that only their employees can access Pathlock Cloud GRC. By configuring Azure_TenantId, they can restrict access to their Azure AD tenant members, leveraging Azure's security and governance controls.

**Related Settings:**

- Azure_ClientId

**Best Practices:** 

- **Configure when:** Setting up Pathlock Cloud GRC for the first time or integrating with Azure AD services for authentication.
- **Avoid when:** Non-Azure environments or when using alternative authentication methods not based on Azure AD.