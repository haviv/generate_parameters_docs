# Authorization Review For Position Change Enable

**Technical Name:** AuthorizationReviewForPositionChangeEnable

**Category:** Workflow

**Default Value:** True

**Impact Level:** High

**Description:** Enables a review process for authorization changes due to position changes within an organization. When enabled, it ensures that any position change triggers a review of the permissions associated with the old and new positions to maintain security and compliance.

**Business Impact:** Ensuring that employees’ access rights are accurate and correspond to their current position is essential for maintaining internal security protocols and compliance with external regulations. Misalignment between access rights and job responsibilities can lead to potential security breaches or compliance violations.

**Technical Impact when configured:** Activation of this parameter enforces a mandatory review of access rights whenever there are changes in an employee's position. It helps in identifying and preventing inappropriate access rights, thus reducing the risks of fraud, data breaches, and non-compliance penalties.

**Examples Scenario:** An employee is promoted from a junior to a senior position. Upon this change, the system triggers an authorization review to adjust the employee’s access rights according to the new position, ensuring that access is granted to additional systems or data as needed while revoking unnecessary permissions that were relevant to the previous position.

**Related Settings:** EnableDeleteAction

**Best Practices:** Configure when implementing role-based access controls and when organizational structure changes frequently; avoid when the organization has a flat structure with minimal position changes or when continuous manual adjustments to access rights are feasible and preferred.