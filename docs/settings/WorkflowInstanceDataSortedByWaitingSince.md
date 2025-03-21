# Workflow Instance Data Sorted By Waiting Since

**Technical Name:** WorkflowInstanceDataSortedByWaitingSince

**Category:** Workflow

**Default Value:** Not applicable

**Impact Level:** Medium

**Description:**

This parameter configures the sorting of workflow instances based on the duration they have been waiting for approval in the Pathlock Cloud GRC platform. It is designed to help organizations manage their workflows more efficiently by prioritizing tasks that have been pending for longer periods.

**Business Impact:**

By enabling better visibility into workflows that require attention, organizations can reduce bottlenecks, improve response times for approval processes, and enhance overall workflow efficiency. This has a direct positive impact on compliance with internal policies and regulatory requirements by ensuring timely processing of approvals.

**Technical Impact when configured:**

When configured, this parameter influences how items in the approval queue are presented to users, prioritizing older requests. This can lead to faster processing of items that have been waiting the longest, helping ensure tasks critical to compliance and risk mitigation are addressed promptly.

**Example Scenario:**

A company uses the Pathlock Cloud GRC platform to manage approval processes for access rights requests. By configuring the `WorkflowInstanceDataSortedByWaitingSince` parameter, the IT department ensures that requests pending approval for the longest time appear at the top of the queue. This helps in identifying and prioritizing requests that might otherwise be overlooked, thereby enhancing the efficiency of the approval process and ensuring timely access rights management.

**Related Settings:** Not applicable

**Applicable Workflows Actions:** Not applicable

**Best Practices:** 

Configure when you have workflows that are critical to compliance and regulatory requirements to ensure they are addressed in a timely manner. Avoid configuring this parameter in ways that might inadvertently prioritize less critical tasks over more urgent ones, which could lead to inefficiencies and potential compliance issues. Prioritize the review and approval of workflows based on their impact and urgency.