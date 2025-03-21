# You Handled Request

**Technical Name:** YouHandledRequest

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter is used to track and manage approvals within the workflow process by updating the manager's decision in the system. It assists in maintaining the integrity and authorization within the workflow actions, particularly in approval steps.

**Business Impact:** Ensures that the approval process is conducted and logged properly within the Pathlock GRC platform. It plays a critical role in managing user permissions and access within the system, affecting security and compliance standings.

**Technical Impact when configured:** Helps in tracking the status of each approval step accurately, preventing unauthorized actions from proceeding within the workflow. It is vital for audit trails and compliance reporting, as it ensures each action taken within a workflow is authorized and recorded.

**Examples Scenario:** An administrator needs to approve a series of steps within a user role modification process. By configuring "YouHandledRequest," the system updates and logs each approval, ensuring that only authorized changes are made and properly recorded for audit purposes.

**Related Settings:** 

- EnableTransportsRead
- AuthorizationReviewForPositionChangeRunForAllOnlineSystems

**Best Practices:** Configure when setting up workflows that require approval steps to ensure accountability and traceability. Avoid when workflows do not include decision-making steps or if the process does not need formal approval.