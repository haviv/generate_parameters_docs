# SoD Simulate For High Risk Roles

**Technical Name:** SoDSimulateForHighRiskRoles

**Category:** SOD

**Default Value:** True

**Impact Level:** High

**Description:** Enables the simulation of Separation of Duties (SoD) checks for users with high-risk roles, assessing potential SoD violations without affecting current role mappings.

**Business Impact:** Ensures that high-risk role assignments are scrutinized for SoD violations, mitigating risks of fraud and unauthorized access. Helps maintain regulatory compliance by proactively identifying and addressing potential SoD conflicts.

**Technical Impact when configured:** When enabled, the system simulates SoD checks for specified high-risk roles, using existing user authorizations to identify forbidden role combinations without altering current configurations. 

**Examples Scenario:** When a user is being considered for assignment to a critical role that potentially conflicts with their existing roles, enabling this feature allows administrators to simulate the assignment and assess any SoD violations, thereby preventing unauthorized access combinations before they occur.

**Related Settings:** EnableSimulationOfRoleFromDev

**Best Practices:** Configure when assessing new role assignments for high-risk roles to preemptively identify SoD violations. Avoid enabling this feature for low-risk roles to reduce unnecessary processing and overhead.