# Employee Custom Source Field For Mail Field

**Technical Name:** EmployeeCustomSourceFieldForMailField

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter allows for the customization of the source field used for employee mail fields within the Pathlock Cloud GRC platform. It enables organizations to specify a custom field from their organizational structure or user directory that should be used to populate the mail field for users within the system.

**Business Impact:**

Correctly setting this parameter ensures that communications, notifications, and any mail-related functionalities within the GRC platform are correctly mapped to the employee’s actual email address. It impacts how effectively the system can communicate with users, directly affecting compliance processes, security alerts, and workflow notifications.

**Technical Impact when configured:**

When this parameter is configured, the system overrides the default mapping and uses the specified custom field to fetch mail addresses for users. This can aid in aligning the system more closely with the organization's existing data structures and thereby improve data accuracy and the reliability of system-generated communications.

**Examples Scenario:**

An organization uses a custom field named 'CorporateEmail' in their HR system to store employee email addresses, which differs from the standard email field used by the Pathlock system. By setting the `EmployeeCustomSourceFieldForMailField` to 'CorporateEmail', the organization ensures that all system communications reach the correct email addresses of their employees.

**Related Settings:**

- `EmployeeCustomTypeForMailField`

**Best Practices:** configure when the default mail field in the system does not match the organization’s user directory or HR system field. Avoid when the default mail attribute configuration meets organizational needs to prevent unnecessary system complexity.