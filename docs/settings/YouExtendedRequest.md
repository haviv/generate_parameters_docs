**Technical Name:** YouExtendedRequest **

**Category:** Workflow

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The YouExtendedRequest parameter is designed to enhance the workflow process by potentially influencing conditions around approval checks and comment management during the request submission phase. It focuses on streamlining the user experience in extending requests within the Pathlock GRC platform, primarily through its impact on workflow customization and security enhancements.

**Business Impact:**

Implementing YouExtendedRequest can significantly streamline the decision-making process during request submissions, making it crucial for organizations that require efficient workflow management. It can also impact the organization's ability to comply with internal or external regulations by ensuring that approval processes are appropriately adhered to, without unnecessary delays or bypasses.

**Technical Impact when configured:**

When configured, YouExtendedRequest can disable automatic approval checks performed by the request submitter, which could enforce a more rigorous review process by ensuring only designated approvers can validate requests. This configuration might also extend to Comment management within workflows, potentially affecting how users interact with the request submission process.

**Examples Scenario:**

A company wants to ensure that all requests for access to financial records go through a mandatory review process by a senior manager, without an automatic approval option available to lower-level employees. By configuring YouExtendedRequest, they can ensure that the approval process is strictly adhered to, aligning with the company's internal controls and audit requirements.

**Related Settings:**

- DisableDeleteCommentFromWorkflow
- DisableApprovalCheckByRequestSubmitter

**Best Practices:** 

- Configure YouExtendedRequest when you wish to strengthen the control over your approval processes and ensure compliance with stringent workflow regulations.
- Avoid configuring this parameter if your organization benefits from a more flexible, quick-turnaround request process where the request submitter can also approve requests for efficiency.