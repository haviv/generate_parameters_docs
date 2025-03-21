# Custom Authentication Provider Allow Fallback 

**Technical Name:** CustomAuthenticationProviderAllowFallback

**Category:** Security 

**Default Value:** (No explicit default value provided in the code. Typically, this would default to either enabling or disabling the functionality, based on best practices and security posture desired by the organization.)

**Impact Level:** Medium 

**Description:** 

This setting controls whether the Pathlock Cloud GRC platform's authentication mechanism will fallback to an alternative authentication method if the custom authentication provider fails to authenticate a user. 

**Business Impact:** 

Enabling this option ensures that there is a backup authentication method available, thus preventing potential lockout from the system and ensuring business continuity. However, it also introduces the possibility of bypassing the primary authentication mechanism if not properly configured, thereby affecting the security posture.

**Technical Impact: when configured**

When configured to allow fallback, the system attempts to authenticate a user with the custom provider first. If this fails, it then tries to authenticate the user with the default or another specified fallback authentication provider. 

**Examples Scenario:**

An organization implements a custom authentication provider for enhanced security measures. If the custom provider service is temporarily unavailable due to maintenance or unexpected outages, the system can be configured to fall back to a standard authentication method. This ensures users are still able to authenticate and access the platform, maintaining productivity without compromising security by using a pre-approved alternative.

**Related Settings:** 

- CustomAuthenticationProviderAdditionalParameter

**Best Practices:** 

- **configure when** you have a robust secondary authentication method available that complies with your organization's security requirements.
- **avoid when** your secondary authentication method significantly lowers the security standards compared to your primary custom authentication provider.