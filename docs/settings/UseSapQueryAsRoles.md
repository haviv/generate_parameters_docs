# Use Sap Query As Roles

**Technical Name:** UseSapQueryAsRoles

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The UseSapQueryAsRoles parameter allows integration with SAP systems to dynamically interpret SAP queries as roles within the Pathlock Cloud GRC platform. This functionality bridges the gap between SAP's complex authorization mechanism and the simplified role-based access control model in Pathlock, enhancing visibility and management of access controls and compliance.

**Business Impact:**

Implementing this parameter can significantly streamline the management of user roles and permissions, reducing manual effort and the risk of errors. It enables a more granular and accurate representation of SAP access rights within Pathlock, aligning SAP access control with organizational policies and compliance requirements.

**Technical Impact when configured:**

- Dynamically maps SAP queries to roles within Pathlock, improving the precision of access controls.
- Facilitates automated role assignment based on SAP query results, enhancing access management efficiency.
- Aids in the compliance audits by providing a clear, accountable mapping of SAP queries to organizational roles.

**Example Scenario:**

An organization wants to ensure that its SAP users' access rights are managed efficiently and comply with industry regulations. By enabling UseSapQueryAsRoles, the GRC team can automatically map SAP query outputs to roles in Pathlock, making it easier to audit, manage, and report on access controls and compliance.

**Related Settings:**

- SoDSimulateForHighRiskActivities

**Best Practices:** 

- Configure when: You require a dynamic and automated way to manage SAP access controls within Pathlock.
- Avoid when: Your organization does not utilize SAP queries for managing user roles or when static role definitions are preferred.