# Display Workflow Form Viewer

**Technical Name:** DisplayWorkflowFormViewer

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the display of a Workflow Form Viewer, facilitating users to view forms associated with specific workflows within the Pathlock Cloud GRC platform. This feature enhances the transparency and accessibility of form-based data in workflow processes.

**Business Impact:**

Improving the visibility of workflow forms through the Workflow Form Viewer can streamline the review and processing of critical information. It supports better decision-making by ensuring that relevant form data is readily available to authorized users. This can lead to more efficient workflow management, reduced errors, and improved compliance with internal and external governance requirements.

**Technical Impact when configured:**

When enabled, the Display Workflow Form Viewer parameter allows for dynamic viewing of forms within the designated workflows. This can affect system performance depending on the complexity and size of the forms being accessed. Proper configuration is essential to balance functionality with system resource utilization.

**Examples Scenario:**

For instance, in a workflow designed for Emergency Access management, enabling the Display Workflow Form Viewer can provide auditors and compliance teams with immediate access to all request forms and approval documents directly within the workflow. This facilitates a quicker review process, ensuring that emergency access rights are granted and revoked in a compliant manner.

**Related Settings:**

- `DisplayLoggedChangesDrillDown`
- `DisableValidityCheckForHRData`

**Applicable Workflows Actions:** 

**Best Practices:** 

- Configure when: You require enhanced visibility and direct access to forms within specific workflows, particularly in scenarios involving compliance, audit trails, and emergency access management.
- Avoid when: System performance or resource utilization is a concern, or if the forms contain sensitive information that should not be broadly accessible.