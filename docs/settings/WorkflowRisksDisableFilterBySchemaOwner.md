# Workflow Risks Disable Filter By Schema Owner

**Technical Name:** WorkflowRisksDisableFilterBySchemaOwner

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:** Determines whether the schema owner filter is disabled in the workflow risks interface. When disabled, users cannot filter workflow risks based on the schema owner, providing a broader, less granular view of workflow risks.

**Business Impact:** Disabling the filter by schema owner can speed up risk identification processes by broadening the search results. However, it may also lead to an overwhelming amount of data for users to sift through, potentially obscuring specific, high-risk issues associated with particular schema owners.

**Technical Impact when configured:** Configuring this parameter to disable filtering by schema owner affects the usability of the WorkFlow Risks control by altering how users can narrow down or expand their search for risks within workflows. It directly impacts the display of workflow-related risks, making the process either more streamlined by removing granularity or more general for a broader risk assessment.

**Examples Scenario:** If an organization finds that its users spend a considerable amount of time filtering through schema owners without gaining actionable insights, they may choose to disable this filter. Consequently, users might identify high-risk areas more quickly without being bogged down by details, improving the efficiency of the risk management process.

**Related Settings:** NA

**Best Practices:** 
- **Configure when:** The detailed filtering by schema owner significantly slows down the risk identification process or does not contribute actionable insights.
- **Avoid when:** Granular filtering by schema owner is crucial for identifying specific workflow risks associated with particular schemas, and such detail is necessary for your organization's risk management practices.