**Employees Source File Delimiter**

**Technical Name:** EmployeesSourceFileDelimieter

**Category:** Configuration

**Default Value:** N/A

**Impact Level:** High

**Description:** The parameter specifies the delimiter used in the flat file that contains the organization's employee structure data. It determines how the data is split into distinct fields when imported into the Pathlock Cloud GRC platform.

**Business Impact:** Correct configuration of this parameter ensures accurate parsing and integration of employee data. This affects areas such as access control, compliance reporting, and risk assessment within the organization.

**Technical Impact when configured:** Proper configuration ensures the seamless import and accurate structuring of employee data from flat files into the Pathlock Cloud GRC system. Misconfiguration may lead to incorrect data parsing, resulting in data integrity issues or impacts on system performance.

**Examples Scenario:** If the organization’s employee data file is comma-separated, this parameter should be set to “,”. For a tab-separated file, it would be set to “\t”. Correct setting would ensure that each field, such as employee ID, name, department, etc., is correctly identified and imported.

**Related Settings:** N/A

**Best Practices:** configure when initializing or updating the source of employee data to ensure compatibility with the file format. Avoid misconfiguration by confirming the file delimiter before setting and performing a test import when possible.