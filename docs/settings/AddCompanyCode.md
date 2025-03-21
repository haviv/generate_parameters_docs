# Assign employee company codes

**Technical Name:** AddCompanyCode

**Category:** User Management

**Default Value:** None

**Impact Level:** Medium

**Description:**

The `AddCompanyCode` parameter is responsible for assigning specific company codes to employees within the Pathlock Cloud GRC platform. This parameter enables the granular control of user access based on their organizational structure and facilitates the management of security, compliance, and risk by aligning employee access rights with their respective business units or areas.

**Business Impact:**

Proper configuration of this parameter ensures that employees have access only to the necessary data and systems relevant to their company code, thereby reducing the risk of unauthorized access to sensitive information. It supports regulatory compliance efforts by enforcing the principle of least privilege and aids in audit trails by clearly defining access boundaries within the organization's structure.

**Technical Impact when configured:**

- Enhances data security by restricting user access based on company codes.
- Supports compliance with internal policies and external regulations by enforcing access controls.
- Facilitates easier management of user permissions and roles within complex organizational structures.

**Examples Scenario:**

- An organization wants to ensure that employees can only access data and perform actions relevant to their particular business unit. By configuring the `AddCompanyCode` parameter, the organization can assign specific company codes to each employee, thereby limiting access to information and systems based on those assignments.

**Related Settings:** None

**Best Practices:** 

- **Configure when:** You need to enforce access controls based on organizational structure and business units.
- **Avoid when:** Employees require wide access that spans multiple company codes, unless necessary for their role. In such cases, review and monitor configurations regularly to mitigate potential security risks.