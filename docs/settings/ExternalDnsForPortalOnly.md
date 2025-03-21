# External Dns For Portal Only

**Technical Name:** ExternalDnsForPortalOnly

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** 

This parameter allows the configuration of an external DNS specifically for portal access. It is designed to streamline the process of accessing the Pathlock Cloud GRC platform's portal over the internet, ensuring that the access is secure and complies with the organization's external access policies.

**Business Impact:**

Proper configuration of this parameter ensures that external users can access the portal securely and efficiently, without compromising internal network security. It is particularly beneficial for organizations that require a clear separation between internal and external network traffic for audit and compliance reasons.

**Technical Impact when configured:**

When this parameter is configured, the platform will enforce the use of the specified external DNS for all portal access requests. This can enhance security by ensuring that all external access to the portal is routed through a predefined, secure path, potentially incorporating additional security measures such as SSL encryption.

**Examples Scenario:**

- An organization needs to provide access to its GRC portal for external auditors. By configuring `ExternalDnsForPortalOnly`, they can ensure that the auditors access the portal through a secure, designated path that does not expose the internal network.

**Related Settings:** 

**Applicable Workflows Actions:** 

**Best Practices:** configure when external access to the Pathlock Cloud GRC portal needs to be secured and monitored. Avoid configuring this setting without first ensuring that the specified DNS can handle the expected traffic securely and efficiently.