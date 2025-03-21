# Custom Field Technical Name For Employee Id In ERP 2004 S

**Technical Name:** CustomFieldTechncalNameForEmployeeIdInERP_2004S

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CustomFieldTechncalNameForEmployeeIdInERP_2004S` parameter specifies the technical name of the custom field used to store employee IDs in the ERP (Enterprise Resource Planning) system for the 2004 S version. This setting is crucial for correctly mapping employee information between Pathlock Cloud GRC and the organization's ERP system.

**Business Impact:**

Proper configuration of this parameter ensures accurate synchronization of employee identifiers, facilitating effective governance, risk, and compliance (GRC) activities within the Pathlock platform. Incorrect or missing configuration may lead to data integrity issues, affecting compliance reporting and risk assessments.

**Technical Impact when configured:**

When correctly configured, this parameter enables the Pathlock Cloud GRC platform to correctly identify and associate employee-specific data from ERP 2004 S with the corresponding records in Pathlock. This association is critical for executing compliance checks, access control reviews, and any functionality relying on accurate employee identification.

**Examples Scenario:**

A GRC manager needs to ensure that the employee IDs from their organization's SAP ERP system are correctly mapped to the employee profiles managed in Pathlock Cloud GRC for compliance and risk assessment purposes. By setting the `CustomFieldTechncalNameForEmployeeIdInERP_2004S` to the technical name of the custom field used in their ERP for employee IDs, they can assure accurate data mapping and integrity.

**Related Settings:**

- EscalationEmailTemplatePostFix

**Best Practices:** 

- Configure when: You are integrating Pathlock Cloud GRC with an ERP 2004 S system and need to ensure the accurate mapping and management of employee IDs.
  
- Avoid when: Your organization does not use custom fields for employee IDs in the ERP system, or if using a version of the ERP system other than 2004 S. In such cases, consult with Pathlock support for the correct parameter configuration.