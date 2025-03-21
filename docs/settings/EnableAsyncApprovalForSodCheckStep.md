# Enable Async Approval For SoD Check Step

**Technical Name:** EnableAsyncApprovalForSodCheckStep

**Category:** Workflow

**Default Value:** True

**Impact Level:** Medium

**Description:** This setting enables asynchronous approval during the Separation of Duties (SoD) check step within workflow processes. When enabled, it allows the SoD check step to proceed without waiting for immediate approval, facilitating smoother workflow progression and efficiency.

**Business Impact:** Enabling this feature can significantly enhance the efficiency and speed of workflow processes involving SoD checks by reducing wait times for approvals. This can be particularly beneficial in environments where prompt decision-making and action are crucial to maintain compliance and mitigate risks effectively.

**Technical Impact when configured:** When this parameter is configured to be active, SoD check steps within workflows will not require synchronous (real-time) approval. This can lead to faster workflow execution and reduced bottlenecks associated with waiting for approvals.

**Examples Scenario:**
- **Before Enabling:** A workflow involving SoD checks halts at the SoD check step, waiting for manual approval before proceeding, which can delay the overall process, especially outside of business hours.
- **After Enabling:** The same workflow now continues past the SoD check step without waiting for real-time approval, allowing subsequent steps to be initiated, thereby minimizing delays and enhancing overall process efficiency.

**Related Settings:** N/A

**Applicable Workflows Actions:** N/A

**Best Practices:** 
- **Configure when:** Immediate feedback on the SoD check is not crucial, or the potential delay in manual approval might impact the efficiency of business processes adversely.
- **Avoid when:** The SoD check requires real-time decision-making and approval is essential to prevent security or compliance risks immediately.