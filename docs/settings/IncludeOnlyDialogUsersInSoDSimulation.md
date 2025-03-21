# Include Only Dialog Users In SoD Simulation

**Technical Name:** IncludeOnlyDialogUsersInSoDSimulation

**Category:** Security

**Default Value:** False

**Impact Level:** Medium

**Description:**

This setting controls whether the Separation of Duties (SoD) simulation includes only dialog users in the analysis. Dialog users are interactive users who log on to the system interface, as opposed to non-dialog users, such as service accounts or batch users, which perform automated tasks without a graphical interface.

**Business Impact:**

Enabling this filter ensures that SoD simulations focus on users with the potential to perform conflicting tasks through the UI, thereby refining the analysis to where real segregation conflicts may arise, enhancing the accuracy of compliance reporting and risk assessment.

**Technical Impact when configured:**

When this parameter is set to true, SoD simulations will exclude non-dialog users (service and background task accounts), potentially reducing the number of violations reported and focusing on risks posed by interactive users. This refinement aids in targeting remediation efforts more effectively and can improve compliance posture by focusing on actual interactive user conflicts.

**Examples Scenario:**

- Before an internal audit, an organization wants to ensure that only relevant SoD conflicts (involving interactive, dialog users) are presented in the simulation report. By enabling `IncludeOnlyDialogUsersInSoDSimulation`, the organization can filter out noise from automated or system accounts that might skew the risk analysis.

**Related Settings:** N/A

**Best Practices:** Configure this parameter to `true` when you aim to streamline SoD simulations, focusing exclusively on potential conflicts among interactive users. Avoid using this setting if your risk management strategy requires comprehensive coverage that includes both dialog and non-dialog users.