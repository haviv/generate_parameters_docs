# Import Managers To Workflow Based On Direct Manager Field

**Technical Name:** ImportManagersToWFBasedOnDirectManagerField

**Category:** Workflow Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls if managers are automatically imported into a workflow based on their role as direct managers of other employees. When enabled, the system will dynamically include managers in relevant workflow processes, such as approvals, based on the direct manager field defined within employee profiles.

**Business Impact:**

Enabling this setting streamlines the workflow process by auto-populating workflow participants, reducing manual configuration and oversight needed to ensure all relevant managers are included in workflow actions. This can significantly improve the efficiency of processing approvals, task assignments, and any compliance-related workflow activities.

**Technical Impact when configured:**

Upon configuration, the system will automatically analyze and include managers in workflows based on the employee-manager relationship defined in user profiles. This decreases the need for manual setup and ensures that approval processes and task assignments are routed to the correct managerial level, aligning with organizational hierarchy and governance policies.

**Examples Scenario:**

An organization implements a new policy requiring managerial approval for access to critical systems. By enabling this parameter, the system will automatically include direct managers in the approval workflow, ensuring compliance with the policy without the need for manual configuration of each manager within the system.

**Related Settings:**

- AuthorizationReviewShowSubmitOnlyHandledItems

**Best Practices:** Configure this parameter in environments where the organizational structure is stable and where managerial relationships accurately reflect the approval hierarchy. Avoid in settings where direct managers may not serve as the best approvers due to, for example, job function misalignment or excessively broad spans of control.