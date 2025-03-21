# Disable Termination Event

**Technical Name:** DisableTerminationEvent

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

The `DisableTerminationEvent` parameter controls whether termination events within the organization's staff change workflow are enabled or not. When set to true, it prevents the triggering of automated processes associated with user terminations.

**Business Impact:**

Disabling termination events may impact how timely and effectively the system responds to changes in user status, potentially affecting security, compliance, and operational workflows. It could delay the removal of access rights for terminated employees, posing a security risk.

**Technical Impact when configured:**

When the `DisableTerminationEvent` parameter is set to true, it stops the execution of any automated tasks or workflows associated with user terminations. This includes the halting of recalculations for pre-defined rules or any dynamic adjustments to user groups based on termination events.

**Examples Scenario:**

- An organization may choose to disable termination events during a restructuring period to manually review and handle user terminations and reassignments, ensuring a high level of accuracy and oversight.

**Related Settings:** Not specified in the provided code references.

**Best Practices:** 

- **Configure when:** Manual oversight of user terminations is preferred, or during major organizational changes where automatic processing of terminations could lead to errors or security vulnerabilities.
  
- **Avoid when:** Immediate and automatic enforcement of security and compliance policies upon user termination is critical.