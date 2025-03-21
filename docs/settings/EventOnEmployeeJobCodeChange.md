# Event On Employee Job Code Change

**Technical Name:** EventOnEmployeeJobCodeChange

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

Monitors and triggers workflows based on changes to employee job codes within the Pathlock Cloud GRC platform. This ensures that any significant job code alterations are captured and appropriately responded to, maintaining the integrity of access permissions and compliance statuses.

**Business Impact:**

Effective monitoring of employee job code changes is crucial for maintaining compliance with internal policies and external regulations. This parameter helps in automatically updating access permissions, roles, and responsibilities, minimizing the risk of unauthorized access or insufficient execution of duties.

**Technical Impact when configured:**

When activated, this configuration option enables the Pathlock platform to detect changes in employee job codes and execute predefined workflows. This may include notifications to managers, security teams, or compliance officers, automated adjustment of access levels, or initiation of compliance review processes.

**Examples Scenario:**

- An employee is promoted, and their job code changes from a regular employee to a managerial position. The system triggers a workflow to review and update the employee's access permissions accordingly.
- A departmental reorganization leads to several job code changes. The platform automatically initiates workflows to reassess access permissions and compliance with the new organizational structure.

**Related Settings:**

- EnableHRStaticAuthorization
- EnableRichTextCommentInWorkflowApproval

**Best Practices:** configure when significant job code changes occur within the organization, avoid when minimal changes in job codes do not impact security, access, or compliance requirements.