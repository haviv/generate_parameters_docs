# Lanman Server Path

**Technical Name:** LanmanServerPath

**Category:** Configuration

**Default Value:** None

**Impact Level:** High

**Description:** The LanmanServerPath parameter configures the network path for server share names and their corresponding monitored directories. It is critical for ensuring that the Pathlock Cloud GRC platform correctly monitors and manages file access and changes within specified network shares.

**Business Impact:** Proper configuration of the LanmanServerPath ensures that the organization's file access and modification activities are monitored, thereby safeguarding sensitive information and assisting in compliance with various regulatory requirements. Misconfiguration could lead to a lack of visibility into file activities, potentially resulting in undetected security breaches or compliance issues.

**Technical Impact when configured:** When correctly configured, the LanmanServerPath allows the Pathlock Cloud GRC platform to accurately map and monitor designated network shares and directories. This enables the platform to track access and modifications, facilitating audit trails, security monitoring, and compliance reporting.

**Examples Scenario:** An organization needs to monitor access to a network share containing sensitive financial documents. By configuring the LanmanServerPath parameter to include this network share, Pathlock will be able to monitor and log any access or changes to the documents, enhancing the organization's security and audit capabilities.

**Related Settings:** None

**Best Practices:** 
- Configure the LanmanServerPath parameter as soon as network shares are identified for monitoring to ensure comprehensive visibility.
- Avoid using default or nonspecific paths to prevent excessive resource usage or incomplete monitoring coverage.