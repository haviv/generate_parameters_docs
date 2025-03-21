# Custom Authentication Provider Url

**Technical Name:** CustomAuthenticationProviderUrl

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The Custom Authentication Provider Url parameter specifies the endpoint URL of a custom authentication service to be used for validating user credentials in the Pathlock Cloud GRC platform. This parameter is part of the security settings, allowing for the integration of third-party authentication providers beyond the default system.

**Business Impact:**

Setting up a custom authentication provider enhances the security posture of an organization by allowing the use of specialized authentication mechanisms that may include multifactor authentication, biometric verification, or other advanced authentication protocols. It ensures that access to the Pathlock Cloud GRC platform is securely controlled and is compliant with organizational security policies.

**Technical Impact when configured:**

When the Custom Authentication Provider Url is configured, the Pathlock Cloud GRC platform redirects authentication requests to the specified URL. This allows for the use of custom logic and security measures in the authentication process, providing an additional layer of security and flexibility in managing user access.

**Examples Scenario:**

- **Enhanced Security:** An organization requires all applications to use two-factor authentication with a specific authentication provider. By setting the Custom Authentication Provider Url to this provider, they ensure all access to the Pathlock Cloud GRC platform is compliant with their security policy.
  
- **Compliance Requirements:** A financial institution needs to adhere to stringent regulatory requirements for user authentication. They can integrate a custom authentication provider specialized in compliance-focused security measures by configuring this parameter.

**Related Settings:**

- `LoginMethod` (hardcoded as "Custom" when this parameter is in use)

**Best Practices:** 

- **Configure when:** Your organization's security requirements mandate the use of authentication methods not supported by default in the Pathlock Cloud GRC platform, or you need to comply with specific regulatory standards.
  
- **Avoid when:** The default authentication methods provided by Pathlock Cloud GRC platform meet your organization's security and compliance requirements. Using a custom provider may introduce unnecessary complexity and maintenance overhead.