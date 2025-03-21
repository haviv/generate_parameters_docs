# Rebuild User Catalog Cloud Version

**Technical Name:** RebuildUserCatalogCloudVersion

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

The RebuildUserCatalogCloudVersion parameter is designed to control the synchronization process of user tables from SAP systems into the Pathlock Cloud GRC platform. This process is critical for ensuring that user data within the Pathlock environment is up-to-date and accurately reflects the user's current permissions and roles as defined in the SAP system. 

**Business Impact:**

A correctly configured RebuildUserCatalogCloudVersion ensures that the security and compliance posture is accurately reported and managed within the Pathlock platform. It aids in maintaining the integrity of the user data across the organization's IT ecosystem, directly impacting regulatory compliance, security policies, and risk management processes.

**Technical Impact when configured:**

When configured, this parameter initiates the synchronization process, updating the Pathlock user catalogue with the latest user information from the connected SAP systems. This ensures that risk analyses, compliance checks, and security audits are performed against the most current user data, significantly enhancing the accuracy of the GRC processes.

**Examples Scenario:**

Imagine an organization with dynamic user roles and permissions that frequently change due to project realignments or staff movement. By configuring the RebuildUserCatalogCloudVersion, the organization can automate the periodic synchronization of user roles and permissions from SAP, ensuring that these changes are reflected in the Pathlock platform in a timely manner. This capability is critical for maintaining compliance with Sarbanes-Oxley (SOX) controls that require up-to-date access information for audit purposes.

**Related Settings:**

- CustomReportWasntFoundErrorMessage

**Best Practices:** 

- Configure when: There are frequent changes to user roles and permissions in the SAP system, or after any significant batch updates to user data in SAP to reflect these changes immediately in the Pathlock platform.
- Avoid when: If the organization's user roles and permissions are static, or if the SAP system is not a primary source of truth for user management.