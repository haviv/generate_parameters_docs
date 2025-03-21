# Workflow Actions Disabled Color

**Technical Name:** WorkflowActionsDisabledColor

**Category:** Configuration

**Default Value:**

**Impact Level:** Low

**Description:**

This parameter defines the color code that will be used to display disabled workflow actions within the Pathlock Cloud GRC platform. It allows for visual differentiation between active and inactive (or non-applicable) workflow actions, improving user interface clarity and user experience.

**Business Impact:**

Choosing an appropriate color for disabled workflow actions can help users to quickly identify which actions are not currently available, reducing confusion and improving efficiency in managing security, risk, and compliance workflows.

**Technical Impact when configured:**

When configured, this parameter directly affects the visual presentation of the workforce action buttons or links within the Pathlock Cloud GRC platform. It does not affect the functionality of these actions but plays a significant role in user interface accessibility and usability.

**Examples Scenario:**

- **Preventing User Error:** In a scenario where certain actions are not available due to compliance reasons, the WorkflowActionsDisabledColor setting can visually indicate these are not selectable, preventing unintentional errors.
- **Visual Cue for Required Actions:** During a risk assessment workflow, actions that are yet to be completed can be active, and completed or non-applicable actions can be visually differentiated using this color cue, guiding the assessor through the required steps more efficiently.

**Related Settings:**

- VerifyWorkflowActionsNotDoneText: This setting might be used in conjunction to display a message when an action can't be verified, which could relate to the reasons why certain actions are disabled.

**Best Practices:** Configure when you need to provide a clear visual hierarchy and distinction between actionable and non-actionable items within workflow processes. Avoid using colors that are too similar to the enabled actions to prevent confusion.