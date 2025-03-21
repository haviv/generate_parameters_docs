# PTDM Host

**Technical Name:** PTDM_Host

**Category:** Configuration

**Default Value:** (not provided in the code references)

**Impact Level:** High

**Description:** The `PTDM_Host` parameter specifies the hostname or IP address of the Pathlock GRC platform's Profile Tailor Deployment Manager (PTDM). This setting is critical for integrating and managing application pools within Microsoft's Internet Information Services (IIS) 6.0 through the Pathlock GRC platform.

**Business Impact:** Proper configuration of the PTDM_Host parameter ensures seamless communication between the Pathlock GRC platform and the IIS 6.0 server, enabling efficient management of IIS application pools. Incorrect configuration can lead to inability to manage application pools, impacting the deployment and overall security posture of web applications.

**Technical Impact when configured:** When properly configured, the `PTDM_Host` allows the Pathlock GRC platform's Profile Tailor Deployment Manager to accurately locate and interact with the IIS server for the purposes of retrieving and managing application pool information. This integration is vital for automating and streamlining deployment processes and managing web application infrastructure.

**Examples Scenario:** An organization utilizing the Pathlock GRC platform needs to manage multiple application pools for its web applications deployed on an IIS 6.0 server. By configuring the `PTDM_Host` parameter with the correct hostname of the IIS server, the organization can efficiently monitor and manage these application pools directly from the Pathlock GRC platform.

**Related Settings:** 

- `APIResource.DirectoryEntry` (utilized in conjunction with `PTDM_Host` for establishing the directory entry for IIS management tasks)

**Best Practices:** 
- **configure when** setting up or updating the Pathlock GRC platform to ensure it can communicate with IIS 6.0 for application pool management.
- **avoid when** the information is ambiguous or the host is not yet verified to prevent misconfiguration that could lead to management disruptions.