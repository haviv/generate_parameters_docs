# Sap HR Custom Org Assigment Table

**Technical Name:** SAP_HR_CustomOrgAssigmentTable

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `SAP_HR_CustomOrgAssigmentTable` parameter allows for the configuration of a custom organizational assignment table in the Pathlock GRC's integration with SAP HR systems. This ensures that employee data regarding positions, job codes, and job titles can be accurately and uniquely identified, even when they do not follow the standard SAP HR module's organizational structure.

**Business Impact:**

Ensuring correct configuration of this parameter aids in the accurate mapping and maintenance of organizational structures, job roles, and employee assignments within the enterprise. This, in turn, supports effective management of security, risk, and compliance by enabling precise control over access permissions and segregation of duties (SoD). Incorrect configurations can lead to misidentification of roles and responsibilities, impacting SoD checks and potentially leading to unauthorized access or compliance violations.

**Technical Impact when configured:**

- Accurate representation of the organization's unique structure within Pathlock GRC.
- Enhanced ability to detect and manage risks associated with incorrect job titles and roles assignment.
- Improved compliance through better enforcement of SoD policies.
- Ensured consistency and reliability in reporting and audit activities related to organizational assignments.

**Example Scenario:**

An organization customizes its SAP HR module by creating unique job codes and titles that are not standard in SAP. By configuring `SAP_HR_CustomOrgAssigmentTable` to reflect this custom table, Pathlock GRC can accurately understand these unique organizational roles and assignments, enabling better risk analysis and SoD control.

**Related Settings:**

- `AuthorizationReviewSystemDetailsLinkUrl`
- `AuthorizationReviewSystemDetailsLinkVisible`

**Best Practices:** 

- **Configure when:** You have custom modifications to your SAP HR organizational structure that do not align with SAP's standard organizational management tables.
  
- **Avoid when:** Your organization uses SAP's standard HR module structure without any customizations, to prevent unnecessary complexity and potential misconfigurations.