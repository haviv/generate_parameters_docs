**Build Departments By Custom Info Type Mapping**

**Technical Name:** BuildDepartmentsByCustomInfoTypeMapping

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The BuildDepartmentsByCustomInfoTypeMapping parameter is designed to dynamically construct organizational department structures based on custom information type mappings. This setting enables the Pathlock Cloud GRC platform to create a more tailored and accurate depiction of an organization's hierarchy, taking into consideration specific custom fields defined within business units (BU).

**Business Impact:**

Configuring this parameter can significantly impact data governance and access control policies by ensuring departmental structures within the GRC platform accurately reflect the real-world organizational chart. This, in turn, enhances reporting, risk management, and compliance auditing by aligning them more precisely with the company's actual operational structure.

**Technical Impact when configured:**

Upon activation, this parameter instructs the GRC system to reference custom BU info type fields when building or updating the departmental hierarchy. It affects how employee roles and responsibilities are mapped within the platform, influencing access control algorithms and department-level risk assessments.

**Examples Scenario:**

An organization customizes their Business Unit's information by adding fields that denote specific sub-departmental codes or identifiers which are not standard within the Pathlock GRC platform. By enabling and configuring the BuildDepartmentsByCustomInfoTypeMapping parameter, these custom indicators are used to automatically generate detailed departmental structures within the GRC platform, ensuring that access rights, risk assessments, and compliance checks are conducted with an understanding of these nuances. 

**Related Settings:** CustomBUInfoTypeFields

**Best Practices:** 

- **Configure when:** your organization has complex departmental structures not easily mapped by standard fields, or when custom fields hold critical information for delineating department boundaries.
  
- **Avoid when:** the default organizational structure within Pathlock suffices, or when custom fields have not been consistently applied across business units, as this can result in inaccurate department mapping.