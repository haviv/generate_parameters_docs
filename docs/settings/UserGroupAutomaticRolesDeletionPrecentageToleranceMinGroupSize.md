# User Group Automatic Roles Deletion Percentage Tolerance Min Group Size

**Technical Name:** UserGroupAutomaticRolesDeletionPrecentageToleranceMinGroupSize

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines the minimum group size threshold for which the automatic roles deletion percentage tolerance applies when recalculating user roles within group assignments. It is designed to provide flexibility in managing role assignments based on group sizes, ensuring that automatic deletions of roles due to fluctuations in group composition are controlled.

**Business Impact:**

Choosing the right value for this parameter helps in maintaining the balance between security and operational efficiency. It prevents large-scale role reassignments for minor changes in group sizes, which could otherwise disrupt user access and lead to potential security vulnerabilities or administrative overhead.

**Technical Impact when configured:**

When set, this parameter acts as a safeguard against unexpected or automated removal of user roles that might occur due to the variability in the size of user groups. It specifically impacts how the system decides when to apply automatic role deletions during the user group recalibration process.

**Examples Scenario:**

- A user group initially has 100 members with specific roles assigned. Due to this parameter being configured with a specific minimum group size, if the group's size slightly decreases or fluctuates around this threshold, it prevents the automatic deletion of roles that would normally occur due to the change in group size, ensuring stability in role assignments.

**Related Settings:**

- UserGroupAutomaticRolesDeletionFixedTolerance

**Best Practices:** 

- Configure this parameter to a value that reflects the typical size of user groups within your organization to prevent unnecessary role recalculations.
- Avoid setting this parameter without considering the normal fluctuation range of your user groups to prevent inadvertent role retention or deletions.