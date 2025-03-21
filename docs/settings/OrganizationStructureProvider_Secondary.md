# Organization Structure Provider Secondary

**Technical Name:** OrganizationStructureProvider_Secondary

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The Organization Structure Provider Secondary parameter is used to determine the level of detail returned for an organization's structure within the Pathlock Cloud GRC platform. It specifies the depth of departmental or organizational detail to be retrieved from the organization's structure data.

**Business Impact:**

Configuring the Organization Structure Provider Secondary parameter correctly is crucial for ensuring that governance, risk, and compliance (GRC) reports and analyses accurately reflect the organization's hierarchy. Incorrect settings can lead to incomplete reporting data, which might affect decision-making and risk management processes.

**Technical Impact when configured:**

When configured, this parameter dictates the granularity of organizational data fetched by the system. Depending on the specified level, the system will return data up to the specified organizational depth, affecting the scope and detail of GRC activities like segregation of duties (SOD) analysis, compliance reporting, and risk assessments.

**Examples Scenario:**

An organization might set the Organization Structure Provider Secondary to "3" to include up to third-level departmental details in their GRC reporting. This would ensure that GRC processes such as risk assessments are conducted with an understanding of the organization that includes sub-departments or teams within larger departments, making the analysis more fine-grained and accurate.

**Related Settings:**

- SodResolverConfig_ExcludedRolesPrefix

**Best Practices:** configure when the organization requires detailed GRC reporting and analysis that reflects its hierarchical structure. Avoid over-specifying the level, which may lead to unnecessary complexity and data processing overheads.