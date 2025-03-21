**Technical Name:** TechnicalNameForCountry **

**Category:** Configuration

**Default Value:** None

**Impact Level:** Medium

**Description:**

The `TechnicalNameForCountry` parameter is used to filter roles based on a specified country code. This configuration is essential for organizations operating in multiple geographical locations, allowing for a more tailored and region-specific role management within the Pathlock GRC platform.

**Business Impact:**

Configuring the `TechnicalNameForCountry` parameter correctly ensures that role assignments and accesses are compliant with regional regulatory requirements and business practices. It helps in enforcing data segregation policies and managing permission levels effectively across different territories, contributing to the overall governance, risk, and compliance (GRC) strategy.

**Technical Impact when configured:**

Once configured, the system will filter and display only those SAP roles relevant to the specified country code. This parameter acts as a critical filter in workflows related to role selection and assignment, enhancing the precision of access controls and reducing the risk of non-compliance with regional regulations.

**Examples Scenario:**

For instance, a multinational corporation can use the `TechnicalNameForCountry` parameter to specify 'US' for its United States operations. As a result, when managers or GRC administrators in the U.S. assign SAP roles to users through the Pathlock GRC platform, only roles assigned with the U.S. metadata will be available for selection, ensuring compliance with U.S.-specific regulations.

**Related Settings:** UseBusinessRolesAsCompositeRoles

**Best Practices:** configure when operating in multiple countries to ensure compliance and effective role management; avoid when a universal role configuration suffices for the organization's operation.