# Authorization Review For Position Change Template

**Technical Name:** AuthorizationReviewForPositionChangeTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

The `AuthorizationReviewForPositionChangeTemplateId` parameter is used to define the template ID for authorization reviews related to position changes within an organization. This parameter ensures that any position change undergoes a thorough review process, aligning with the organization's compliance and governance standards.

**Business Impact:**

Improper management of position changes can lead to unauthorized access or escalation of privileges, potentially resulting in data breaches, non-compliance incidents, and financial loss. By utilizing a predefined template for authorization reviews, organizations can standardize and streamline the review process, mitigating risks associated with position changes.

**Technical Impact when configured:**

When configured, the `AuthorizationReviewForPositionChangeTemplateId` parameter triggers a specific workflow for reviewing authorization changes related to position alterations. This ensures a systematic and consistent approach to evaluating and approving changes, reducing manual errors and oversight.

**Examples Scenario:**

A company implements the `AuthorizationReviewForPositionChangeTemplateId` to manage a position change from a regular employee to a finance manager. The template ensures that the promotion is reviewed to confirm that the new role's access levels are appropriate and do not violate segregation of duties (SoD) policies.

**Related Settings:**

- `AuthorizationReviewDisableWideApproval`

**Best Practices:** 

- Configure when: Implementing or updating a position within the organization where access and authorization levels need review.
- Avoid when: The position change does not impact access levels or when the organization does not have a clear authorization review process.