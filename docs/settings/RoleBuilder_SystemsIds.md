# Role Builder Systems Ids

**Technical Name:** RoleBuilder_SystemsIds

**Category:** Authorization Review

**Default Value:**

**Impact Level:** High

**Description:**

The Role Builder Systems Ids parameter is used to specify the unique identifiers of systems within the Pathlock Cloud GRC platform for which roles are being constructed or modified. This parameter is essential in the process of defining and tailoring roles across various systems, ensuring they match the organization's security, compliance, and operational needs.

**Business Impact:**

By accurately configuring Role Builder Systems Ids, organizations can streamline their access management processes, enhance oversight, and improve compliance posture. It enables organizations to define roles that are precisely aligned with employee responsibilities and access requirements, thereby reducing the risk of unauthorized access and potential security breaches.

**Technical Impact when configured:**

When configured, this parameter aids in segregating and refining the access control mechanisms within the organization. It ensures that role definitions and access rights are appropriately assigned across different systems, supporting both security and operational efficiency. Misconfiguration, on the other hand, may lead to incorrect role assignments, potentially causing operational disruptions or compliance issues.

**Examples Scenario:**

For instance, if an organization wants to create a new role within its ERP system that grants access to financial records and inventory management modules, the Role Builder Systems Ids would be configured to include the specific identifiers of the ERP system. This ensures that the new role is associated only with the intended systems, providing employees with the necessary access rights without compromising the organization’s security policies.

**Related Settings:**

- Authorization Review Setting
- Risk Chart - Display Data

**Best Practices:** configure when setting up new roles or modifying existing roles within specific systems to ensure access controls are in place and effective. Avoid configuration without proper validation to prevent unintentional access rights assignments.