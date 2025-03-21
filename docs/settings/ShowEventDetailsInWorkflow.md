# Show Event Details In Workflow

**Technical Name:** ShowEventDetailsInWorkflow

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter controls the visibility of event details within workflows in the Pathlock Cloud GRC platform. Enabling this feature allows users to see detailed event information directly in workflow contexts, enhancing the decision-making process.

**Business Impact:**

Enabling this feature improves the transparency of security, risk, and compliance events by providing detailed context. This aids in quicker, more informed decision-making and enhances the oversight capabilities of GRC processes. 

**Technical Impact when configured:**

When enabled, detailed event information is displayed within applicable workflow actions, providing immediate context and insights. It helps in identifying and addressing discrepancies or anomalies directly from the workflow interface, streamlining operations and reducing response times.

**Example Scenario:**

A user is reviewing an authorization request within a workflow. With ShowEventDetailsInWorkflow enabled, the user can see detailed context such as who requested access, for what reason, and any potential security or compliance implications directly within the workflow. This allows for a quicker and more informed authorization decision.

**Related Settings:**

- `ServerDiscrepancyNotInSystem`
- `ServerDiscrepancyNotInPTD`

**Best Practices:** 

- **Configure when:** You require greater transparency and detail within workflow processes for better decision-making.
- **Avoid when:** Minimalist workflow views are preferred, or in scenarios where detailed event visibility could overwhelm the users.