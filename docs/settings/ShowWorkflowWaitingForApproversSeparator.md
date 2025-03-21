**Show Workflow Waiting For Approvers Separator**

**Technical Name:** ShowWorkflowWaitingForApproversSeparator

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:** This setting determines if a visual separator is shown for workflows that are waiting on approvers. When enabled, users can easily distinguish between workflows pending approval and those that are not, directly enhancing user interface clarity in the workflow management section.

**Business Impact:** Enabling this feature can significantly streamline the workflow approval process by providing clear visual cues. This can lead to more efficient decision-making, as approvers can quickly identify which workflows require their attention, ultimately speeding up the time-to-decision for critical compliance and risk management actions.

**Technical Impact when configured:** When configured, this setting adds a visual separator in the user interface, specifically in sections where workflows are listed and are pending approval. This visual guide helps in prioritizing and managing approvals more effectively within the Pathlock GRC platform.

**Example Scenario:** An organization has implemented several workflows that require multiple levels of approval for access changes in critical systems. By enabling this parameter, approvers can quickly identify all pending workflows that need their attention, ensuring that compliance requirements are met promptly without unnecessary delays.

**Related Settings:** Not specified due to lack of direct reference in the provided code segments.

**Best Practices:** Configure this setting to "True" in environments where workflow approvals are a regular occurrence and quick identification of pending approvals is necessary. Avoid enabling this feature if your organization does not utilize multi-tier approval workflows, as it could add unnecessary visual elements to the interface.