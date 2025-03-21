# Sync Organization Structure Maximum Employee Number Length

**Technical Name:** SyncOrganizationStructureMaximumEmployeeNumberLength

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter specifies the maximum length of the employee number that is allowed when synchronizing organizational structures within the Pathlock Cloud GRC platform. It ensures that the employee ID length complies with the platform's limitations and prevents errors during synchronization.

**Business Impact:**

Setting the appropriate maximum employee number length is crucial for maintaining data integrity across the organization's HR and IT systems. It helps in avoiding synchronization failures that could lead to incomplete or inaccurate organizational structures within the GRC platform. This in turn supports effective governance, compliance, and risk management processes.

**Technical Impact when configured:**

When configured, this parameter actively controls and validates the length of employee IDs being synchronized to the platform. If an employee ID exceeds the specified length, the synchronization of that specific record will fail, thereby ensuring that only compliant data is updated or added to the system.

**Examples Scenario:**

A company's HR system assigns a unique 10-digit employee ID to each employee. The Pathlock Cloud GRC platform, however, is configured to accept a maximum employee number length of 8 digits. Without adjusting this parameter to accommodate 10-digit IDs, any attempt to synchronize employee details from the HR system to the GRC platform will result in an error for those records with IDs exceeding the maximum length.

**Related Settings:**

- No directly related settings were identified from the provided code references.

**Best Practices:** configure when you are integrating or synchronizing with external systems that have predetermined employee ID lengths to ensure seamless data synchronization. Avoid configuring this parameter without validating the max length requirement of employee IDs in connected systems.