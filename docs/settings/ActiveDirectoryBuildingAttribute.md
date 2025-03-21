# Active Directory Building Attribute

**Technical Name:** ActiveDirectoryBuildingAttribute

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** 

This parameter specifies the attribute within Active Directory (AD) that represents the building associated with user accounts. It is utilized to granularly manage and assign security, compliance, and access controls based on users’ physical locations within an organization.

**Business Impact:**

Configuring this parameter correctly helps ensure that user access rights and restrictions are accurately implemented according to their physical location within the organization. This is particularly important for organizations with complex structures or multiple buildings, where access needs vary significantly by location.

**Technical Impact when configured:**

When this attribute is configured, the Pathlock Cloud GRC platform can use the building information of users from Active Directory to enforce location-specific security policies. It allows for the designation of access rights, monitoring, and compliance controls based on the user's building attribute, enhancing the specificity and relevance of GRC measures.

**Examples Scenario:**

- **Scenario:** An organization wants to restrict access to a sensitive system only to users located in the main headquarters building.
  - **Without Configuration:** Users across all buildings have similar access rights, making it hard to enforce location-based security policies.
  - **With Configuration:** By setting the Active Directory Building Attribute, Pathlock Cloud GRC can filter users based on their building attribute and enforce access controls appropriately, enhancing security and regulatory compliance.

**Related Settings:** 

- `ActiveDirectoryDisableEmployeeIDField`

**Best Practices:** 

- **Configure when:** You have multiple buildings and need to enforce location-specific access controls and compliance policies.
- **Avoid when:** Your organization operates from a single location, or there are no location-based distinctions in access requirements.