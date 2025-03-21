# Enable Digital Sign For Workflow

**Technical Name:** EnableDigitalSignForWorkflow

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

Enables digital signature verification for processes within the workflow. When enabled, users must provide a digital signature for selected actions within the workflow, increasing the security and traceability of critical operations.

**Business Impact:**

Ensures that actions within critical workflows are executed by authorized individuals and provides an audit trail for compliance purposes. It adds an additional layer of security, reducing the risk of unauthorized access and modification.

**Technical Impact when configured:**

- Requires users to digitally sign off on actions within specified workflows.
- Increases the security and audit capabilities by tracing who approved what action and when.
- May slightly increase the time required to complete actions in the workflow due to the additional verification step.

**Examples Scenario:**

Consider a scenario where a high-level access role needs to be assigned within an organization. With `EnableDigitalSignForWorkflow` configured, the assignment process requires a digital signature from an authorized approver. This measure prevents unauthorized role assignment and ensures that only approved personnel can authorize changes, providing a clear, auditable trail.

**Related Settings:**

- `CommonSettings.Default.LoginMethod`: relates to how users authenticate before they can issue a digital signature.

**Best Practices:** configure when,
- Any workflow action involves sensitive data or critical system changes.
- Compliance with internal or external audit requirements necessitates clear accountability and non-repudiation.

avoid when,
- Workflows are for non-critical actions where the added security and complexity of digital signatures do not justify their implementation.