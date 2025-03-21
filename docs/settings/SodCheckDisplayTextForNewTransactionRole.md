# SoD Check Display Text For New Transaction Role

**Technical Name:** SodCheckDisplayTextForNewTransactionRole

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the display text associated with checks for new transaction roles within the Pathlock Cloud GRC platform. It aims to enhance clarity and understanding of Separation of Duties (SoD) conflicts that may arise with the assignment of new transaction roles.

**Business Impact:**

Improper configuration may lead to a lack of clear guidance for users when SoD conflicts are identified, potentially resulting in unauthorized access or the assignment of conflicting roles. Accurate configuration ensures that users are adequately informed about the implications of new transaction roles on SoD policies.

**Technical Impact when configured:**

Ensures that users and administrators receive clear, actionable information regarding SoD conflicts with new transaction roles, facilitating better security and compliance decisions.

**Example Scenario:**

When a new transaction role is proposed for a user, the system checks for potential SoD conflicts. The message defined by `SodCheckDisplayTextForNewTransactionRole` is displayed, informing the decision-maker of the specific SoD conflict and its implications, enabling a more informed decision regarding the role assignment.

**Related Settings:**

- `SodDetailsShowRoleBasedSummary`

**Best Practices:** Configure when defining new transaction roles or updating existing ones to ensure that all stakeholders understand the implications of SoD conflicts. Avoid generic messages that do not provide actionable insights into the nature of the SoD conflict.