# Custom BUType Object Type

**Technical Name:** CustomBUTypeObjectType

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** The Custom BUType Object Type parameter is designed for fine-tuning the organization structure within the Pathlock Cloud GRC platform. It enables the customization of business unit types, addressing specific operational needs and compliance requirements.

**Business Impact:** By configuring the Custom BUType Object Type parameter, organizations can better align their GRC platform with internal structures and processes. This enhances the platform’s ability to manage security, risk, and compliance more effectively by reflecting the actual organizational hierarchy and roles accurately.

**Technical Impact when configured:** When the Custom BUType Object Type parameter is configured, it impacts how business units are classified and interacted with within the platform. This can affect reporting, user management, and the execution of compliance and governance controls, making the system more adaptable to unique organizational needs.

**Examples Scenario:** If an organization has a unique business unit that doesn't fit traditional models (e.g., a hybrid department that oversees both IT and Finance), configuring this parameter allows them to define and manage access and controls for this unit in a way that reflects its unique nature.

**Related Settings:** 

- `CommonSettings.Default.ActiveEmployeesReadDaysAhead`: References the setting that allows for future-dated changes in the organizational structure, indicating potential integration points.
- `CUASystemId`: Although not directly referenced, it demonstrates the system’s ability to customize settings for unique administration needs.

**Best Practices:** 
- **Configure when:** You have unique organizational structures that do not align with standard business unit classifications provided by Pathlock.
- **Avoid when:** Default classifications adequately reflect your organizational structure, or if changes might complicate compliance and governance processes unnecessarily.