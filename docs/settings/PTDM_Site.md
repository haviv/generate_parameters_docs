# PTDM Site

**Technical Name:** PTDM_Site

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `PTDM_Site` parameter is designed to configure the primary URL or identifying location for the Pathlock GRC platform's integration points. This parameter is crucial for ensuring that the platform's services are correctly aligned with the organization's domain and network configurations.

**Business Impact:**

Correct configuration ensures seamless connectivity and interaction between the Pathlock GRC platform and other applications within the organization’s network. Misconfiguration could lead to accessibility issues, impacting the platform's efficiency and the organization's ability to maintain robust governance, risk management, and compliance processes.

**Technical Impact when configured:**

- Proper configuration enables accurate data exchange and reporting between the Pathlock platform and integrated systems.
- It ensures that notifications, alerts, and reports are correctly routed to the intended endpoints.

**Examples Scenario:**

A financial organization utilizes the Pathlock GRC platform for managing its compliance tasks. The `PTDM_Site` parameter is set to the organization’s specific network domain to ensure that the compliance reports generated are directly accessible from the organization's internal systems, facilitating timely audits and compliance checks.

**Related Settings:**

- PTDM_SmartQueryEntitiesPath

**Best Practices:** configure when setting up or changing the network environment of the Pathlock GRC platform; avoid when the current network setup is correctly configured and operating without issues.