**Technical Name: RestOrganizationStructureProvider_RunInCloud**

**Category: Configuration**

**Default Value:**

**Impact Level: Medium**

**Description:**

Determines if the organization's structure provider should fetch data from a cloud-based source when the traditional, possibly on-premises, data sources are unavailable or not configured.

**Business Impact:**

Enables seamless integration and synchronization of organizational structure data from cloud-based sources, ensuring that governance, risk management, and compliance data are up-to-date and reflective of current organizational hierarchies and structures.

**Technical Impact when configured:**

When this parameter is configured, it allows the system to default to a secondary, cloud-based source for organizational data if the primary data source is inaccessible or not specified. This ensures continuity in data flow and availability, particularly important for dynamic organizations relying on up-to-the-minute data for decision-making.

**Examples Scenario:**

In a scenario where the primary organizational structure data source is temporarily unavailable due to server maintenance or an unexpected outage, configuring this parameter to utilize cloud-based data ensures there is no interruption in fetching the necessary organizational structure data needed for compliance and risk management operations.

**Related Settings:**

- `CommonSettings.Default.HRDataSourceForExternalTableName`
- `CommonSettings.Default.OrganizationStructureProvider_Secondary`
- `CommonSettings.Default.ExternalDatabaseEmployeesSelectQuery`

**Best Practices:** 

- **Configure when:** You have a reliable cloud-based source for organizational structure data, ensuring business continuity in case of primary source unavailability.
- **Avoid when:** The cloud-based data source is not regularly updated or does not reflect the current state of your organization's structure accurately.