# Performed By System

**Technical Name:** PerformedBySystem

**Category:** Workflow

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The `PerformedBySystem` parameter is used within Pathlock Cloud GRC's platform to indicate actions that are automatically performed by the system rather than manual interventions by the users. This parameter plays a crucial role in automating routine tasks and decisions within workflows, ensuring efficiency and consistency in operations.

**Business Impact:**

Automating actions within the GRC processes minimizes human error, speeds up response times, and ensures compliance with established policies and procedures. Automated tasks, marked by `PerformedBySystem`, allow organizations to maintain a high level of security, risk management, and compliance without extensive manual oversight.

**Technical Impact: when configured**

When the `PerformedBySystem` parameter is configured, it allows specific workflows to execute without manual intervention. This not only streamlines the operations but also ensures that certain critical tasks are performed precisely and timely, based on the predefined logic and conditions within Pathlock's GRC workflows.

**Examples Scenario:**

- **Automating User Creation:** When a new employee joins the organization, the system can automatically initiate and complete the user creation process, assigning roles and permissions based on predefined rules without the need for manual processing.
- **Mass Data Upload:** For bulk updates or data uploads, such as policy acknowledgments or compliance evidence, the `PerformedBySystem` parameter can ensure these are processed automatically, recording the actions without manual file handling.
- **Workflow Forking:** In complex decision-making workflows where actions need to diverge based on certain conditions, the parameter can automate the forking process, ensuring the correct path is followed without manual decision-making.

**Related Settings:** 

- WorkflowManager.Instance
- WorkflowActions

**Best Practices:** configure when automating routine and repetitive tasks to ensure efficiency and accuracy; avoid when tasks require manual verification or decision-making that cannot be predefined.