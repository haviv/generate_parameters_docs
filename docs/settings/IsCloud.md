**Is Cloud**

**Technical Name:** IsCloud

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** Determines if the current Pathlock GRC environment is configured for cloud-based operations.

**Business Impact:** Affects how certain system-wide settings and operations are performed, leaning towards either cloud-centric procedures or on-premises ones. This can influence the overall security, scalability, and accessibility of the GRC platform.

**Technical Impact when configured:** When enabled, the system adopts configurations and operational pathways suited for a cloud environment. This may include, but is not limited to, enhanced remote access capabilities, cloud-specific security measures, and integrations with other cloud services.

**Examples Scenario:** If an organization decides to transition its GRC operations to a cloud-based infrastructure to benefit from scalable resources, setting `IsCloud` to true would adapt the system's operations to better align with cloud architecture principles, optimizing performance and security in a cloud environment.

**Related Settings:** `CommonSettings.Default.IsCloud`, `CommonSettings.Default.SystemWideSystemId`

**Best Practices:** configure when transitioning to or operating in a cloud-based environment; avoid when the infrastructure relies solely on on-premises solutions.