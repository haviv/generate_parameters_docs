# Step Extension Max Requests

**Technical Name:** StepExtensionMaxRequests

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `StepExtensionMaxRequests` parameter controls the maximum number of requests that can be extended for a particular step in the workflow. It ensures that each workflow step has a limit on how many times it can be extended, maintaining an efficient process flow and preventing indefinite delays.

**Business Impact:**

Setting a limit on step extensions helps in ensuring timely completion of workflows, thereby improving the organization's agility in responding to compliance, security, or risk management requirements. It prevents bottleneck situations where a single step could potentially hold up the entire workflow process.

**Technical Impact when configured:**

Configuring `StepExtensionMaxRequests` impacts the workflow by enforcing a limit on the number of times a step can be extended. This ensures that the workflow progresses within a reasonable timeframe, thereby supporting timely decision-making and adherence to compliance and risk management schedules.

**Examples Scenario:**

Imagine a scenario where a particular step in the access review process is repeatedly being extended, causing delays in the overall process. Implementing `StepExtensionMaxRequests` would limit the number of times this step could be extended, encouraging faster resolution and progression to subsequent steps.

**Related Settings:** 

- `YouExtendedRequest`

**Best Practices:** configure when a workflow step is critical and should not be delayed indefinitely, avoid when flexibility in process flow timing is necessary without strict limits.