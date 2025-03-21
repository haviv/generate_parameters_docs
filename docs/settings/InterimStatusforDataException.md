# Data Exception Interim Status

**Technical Name:** InterimStatusforDataException

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used within the Pathlock Cloud GRC platform to manage the interim status of data exceptions identified during transaction monitoring processes. It is instrumental in the workflow management for handling exceptions, enabling administrators to set an intermediary status for data exceptions until they are reviewed and resolved.

**Business Impact:**

Having an interim status helps in categorizing and prioritizing data exceptions efficiently. This ensures that high-risk exceptions are addressed promptly while awaiting further investigation or resolution, thus mitigating potential risks and ensuring compliance with internal and external audit requirements.

**Technical Impact when configured:**

When configured, this parameter triggers the closing of workflow instances associated with the data exceptions in the transaction monitoring service. This action is crucial for managing the lifecycle of exceptions by marking their transition from identification to an intermediate state awaiting further action.

**Examples Scenario:**

- An organization uses the interim status to temporarily close exceptions that require additional investigation by a specific department. This allows the security team to focus on new exceptions without losing track of ongoing issues.

**Related Settings:**

- Data Exception Initial Status

**Best Practices:** configure when exceptions need to be categorized for further investigation, avoid when all exceptions are to be immediately resolved or require no interim review process.