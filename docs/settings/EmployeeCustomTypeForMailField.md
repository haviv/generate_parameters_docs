# Employee Custom Type For Mail Field

**Technical Name:** EmployeeCustomTypeForMailField

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The EmployeeCustomTypeForMailField parameter is designed to specify the custom field mapping for employee mail fields within the Pathlock Cloud GRC platform. It enables organizations to tailor how employee email addresses are integrated and managed within their GRC environment.

**Business Impact:**

Configuring the EmployeeCustomTypeForMailField parameter correctly ensures that communications, alerts, and notifications are accurately directed to the intended recipients within the organization. This enhances both the efficiency and reliability of internal processes related to Governance, Risk Management, and Compliance (GRC).

**Technical Impact when configured:**

Proper configuration of this parameter ensures the seamless integration of employee mail fields from external systems (such as HR systems or directories) into the Pathlock Cloud GRC platform. This integration is crucial for automating workflow notifications and ensuring that risk management processes are aligned with the organization's communication protocols.

**Examples Scenario:**

- An organization wants to ensure that automated compliance notifications are sent to the correct employee emails, which are managed in a separate HR system. By configuring the EmployeeCustomTypeForMailField parameter, the Pathlock Cloud GRC platform can accurately map these email fields, ensuring effective communication.
  
**Related Settings:**

- `ActiveEmployeesReadDaysAhead`
- `CustomBUInfoTypeTable`
- `CustomBUInfoTypeFields`

**Best Practices:** configure when the default email field mapping does not align with your organization's HR system or directory structure; avoid when the default configuration meets organizational needs.