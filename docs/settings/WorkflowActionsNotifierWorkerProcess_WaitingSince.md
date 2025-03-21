# Workflow Actions Notifier Worker Process Waiting Since

**Technical Name:** WorkflowActionsNotifierWorkerProcess_WaitingSince

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter tracks the time since a workflow action was initiated and waiting for the Notifier Worker Process to process it. It is crucial for understanding the efficiency and responsiveness of the workflow system within the Pathlock Cloud GRC platform.

**Business Impact:**

Ensuring workflow actions are processed in a timely manner is vital for maintaining operational efficiency and adherence to compliance requirements. Delays in processing can lead to bottlenecks in workflows, affecting user experience and potentially causing compliance issues.

**Technical Impact when configured:**

Proper configuration and monitoring of this parameter can help in identifying and addressing system performance issues early. It aids in optimizing the workflow processing time, thereby improving the overall system efficiency and user satisfaction.

**Examples Scenario:**

1. In a scenario where a user submits a request for access rights approval, the `WorkflowActionsNotifierWorkerProcess_WaitingSince` parameter can help in tracking how long the request has been waiting for the notifier worker to process it. This aids in ensuring that access rights are granted in a timely fashion, critical for maintaining business continuity.
2. For auditing purposes, tracking the time since notification workflows have been initiated and comparing it against predefined benchmarks can highlight inefficiencies or system issues.

**Related Settings:**

- `WorkflowActionsNotifierWorkerProcess_WorkflowInstanceId`
- `WorkflowActionsNotifierWorkerProcess_OpenOn`

**Best Practices:** configure when,

- There is a need to closely monitor and optimize workflow processing times.
- Adhering to strict compliance and audit requirements related to workflow timings.

avoid when,

- Minimal impact is expected from workflow processing delays.
- The system is not experiencing significant workflow processing backlogs.