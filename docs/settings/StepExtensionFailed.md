# Step Extension Failed

**Technical Name:** StepExtensionFailed

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The StepExtensionFailed parameter is designed to handle scenarios where an attempt to extend a workflow step within the Pathlock Cloud GRC platform does not succeed. This parameter could be critical in managing workflow steps that require extension due to various operational needs.

**Business Impact:**

Improper handling of step extensions can lead to delays in workflow processes, impacting the overall efficiency and effectiveness of governance, risk management, and compliance (GRC) tasks. It ensures that there is a mechanism to identify and address failed step extension attempts, minimizing operational disruptions.

**Technical Impact when configured:**

Configuring the StepExtensionFailed parameter may lead to more rigorous monitoring and management of workflow step extensions, ensuring that failures are promptly identified and remediated. It allows for smoother operation of the GRC processes by reducing the likelihood of unaddressed workflow step extension issues.

**Example Scenario:**

An auditor initiates a step extension for a compliance review workflow due to unforeseen circumstances requiring additional review time. The extension attempt fails due to system limitations or configuration issues. The StepExtensionFailed parameter triggers an alert to the workflow administrator for immediate action, ensuring that the review process is not unduly delayed.

**Related Settings:**

- StepExtensionMaxRequests

**Best Practices:** 

- **Configure when:** Immediate notification of failed step extension attempts is critical for the timely management of GRC workflows.
- **Avoid when:** Workflow processes do not involve or require extension functionalities.