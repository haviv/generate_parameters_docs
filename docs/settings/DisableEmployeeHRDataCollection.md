# Disable Employee HR Data Collection

**Technical Name:** DisableEmployeeHRDataCollection

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:**

The DisableEmployeeHRDataCollection parameter controls whether the system collects HR data related to employees. When enabled, it prevents the automatic collection and processing of employee data from connected HR systems.

**Business Impact:**

Disabling HR data collection affects data-driven HR insights, compliance reporting, and risk analysis by omitting employee-related data. It may limit the ability to perform thorough audits and compliance checks related to HR activities and personnel information within the Pathlock Cloud GRC platform.

**Technical Impact when configured:**

Once this parameter is configured to disable data collection, any associated processes or functionalities relying on employee HR data will not receive updates, potentially affecting security, risk management, and compliance monitoring capabilities. Further automation and reporting that depend on this data will need to be adjusted or will operate with outdated information.

**Examples Scenario:**

An organization subject to strict privacy regulations decides to disable the collection of specific HR data to comply with legal requirements, preventing the accumulation of sensitive employee details that are not essential for its GRC objectives.

**Related Settings:** 

- EmployeeCustomSubtypeForMailField

**Best Practices:** configure when privacy and data minimization principles outweigh the benefits of collecting expansive employee data; avoid when comprehensive HR insights and compliance reporting are critical for business operations.