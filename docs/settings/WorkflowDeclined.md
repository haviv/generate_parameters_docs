# Workflow Declined

**Technical Name:** WorkflowDeclined

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter indicates the status of a workflow once it has been declined. It plays a critical role in managing the lifecycle of workflow instances within the Pathlock Cloud GRC platform, specifically focusing on governance, risk management, and compliance (GRC) operational workflows.

**Business Impact:**

A declined workflow affects operational processes by halting forward progress on tasks that require approval. It can signal potential issues in the business process or policy adherence, requiring immediate attention or re-evaluation of the task at hand. Monitoring and managing declined workflows efficiently can help organizations maintain compliance, mitigate risks, and ensure that business operations run smoothly and securely.

**Technical Impact when configured:**

Once set, this parameter triggers specific actions within the system, such as sending notifications to relevant stakeholders, updating the workflow instance's status, and potentially initiating a review process to address the reasons for decline. It can be used to enhance audit trails by providing clear evidence of decision-making processes and ensuring accountability.

**Examples Scenario:**

- **Compliance Review:** In a scenario where a compliance review workflow is declined, it might indicate non-compliance with internal policies or external regulations. This could trigger a re-evaluation of practices or require additional documentation to ensure compliance.
  
- **Access Request:** When an access request workflow is declined, it triggers notifications to the requester and the security team to review the reasons behind the decline, ensuring that access control policies are appropriately enforced.

**Related Settings:**

- ApplyWorkflowMitigationsOnEmployeeLevel
- WorkflowAdditinalParameterKey

**Best Practices:** Configure notifications and alerts for declined workflows to ensure immediate attention by relevant stakeholders. Avoid over-relying on manual checks by automating the review process for declined workflows to streamline operations and reduce response times.