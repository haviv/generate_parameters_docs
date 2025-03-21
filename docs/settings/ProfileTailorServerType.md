**Pathlock Server Type**

**Technical Name:** ProfileTailorServerType

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:**
The `ProfileTailorServerType` parameter is used to specify the type of server Pathlock is operating on, which can drastically affect how data exchanges, security checks, and file transfers are handled within the Pathlock GRC platform.

**Business Impact:**
Choosing the correct server type is crucial for ensuring that Pathlock operates efficiently and securely within an organization's IT infrastructure. It affects the platform's ability to correctly perform critical GRC functions, such as risk monitoring, compliance checks, and security management.

**Technical Impact when configured:**
When properly configured, this parameter ensures that Pathlock optimally interacts with other systems and services, leveraging the correct protocols and settings for data encryption, file transfers, and system queries. Misconfiguration could lead to data leakage, security vulnerabilities, or performance issues.

**Examples Scenario:**
- A financial institution using Pathlock for compliance management needs to transfer sensitive compliance reports securely. Setting the `ProfileTailorServerType` appropriately ensures that the data is encrypted and sent through secure channels, adhering to financial regulatory standards.
- An IT company employing Pathlock for security management might need to adjust the server type to integrate with its cloud infrastructure, enabling seamless data queries and automated risk assessments without compromising on security or performance.

**Related Settings:**
- `CommonSettings.Default.EnableModernStyle`

**Applicable Workflows Actions:** 

**Best Practices:** 
- **Configure when:** setting up Pathlock for the first time on your server or migrating Pathlock to a new server type. It's also wise to revisit this setting after major infrastructure changes within your organization.
- **Avoid when:** Uncertain about your server's specifications or infrastructure. Incorrect configuration could impair Pathlock's functionality or your organization's security posture.