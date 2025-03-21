# Create New Doctor Add Dash To

**Technical Name:** CreateNewDoctorAddDashToID

**Category:** Configuration

**Default Value:**

**Impact Level:** Low

**Description:** 

This parameter controls the formatting of newly created doctor IDs within the Pathlock Cloud GRC platform, specifically adding a dash to their ID for certain configurations.

**Business Impact:** 

Ensures that doctor IDs adhere to specific formatting requirements, potentially aligning with legal or organizational standards. Correct ID formatting can facilitate easier management and identification of doctor profiles within systems, enhancing operational efficiency and data integrity.

**Technical Impact when configured:** 

When activated, this parameter modifies the default behavior of ID assignment to new doctor profiles, adding a dash to the ID. This might affect how IDs are stored, displayed, or utilized across the platform and integrated systems.

**Examples Scenario:**

- **Scenario 1:** In a healthcare institution using the Pathlock platform, there is a requirement to format all internal IDs with a dash for easier readability and to match with external systems' formatting rules. Activating this parameter ensures all newly created doctor IDs comply with this requirement.

**Related Settings:** 

- `MaxAttemptsToAssignPosition`: This setting, while not directly related, indicates the system's flexibility in adjusting critical configurations affecting user profiles.

**Best Practices:** 

- **Configure when:** There is a specific requirement for ID formatting that includes the use of dashes. This might be due to legal, operational, or organizational preferences.
  
- **Avoid when:** There is no clear benefit to changing the default ID format. Keeping IDs in a consistent, system-friendly format without special characters can simplify system design and integration.