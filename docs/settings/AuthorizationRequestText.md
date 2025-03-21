# Authorization Request Text

**Technical Name:** AuthorizationRequestText

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

This parameter defines the textual content displayed in authorization requests within the Pathlock Cloud Governance, Risk, and Compliance (GRC) platform. It is used to convey specific details or instructions related to the authorization process, helping streamline decision-making by providing contextual information.

**Business Impact:**

The content set for AuthorizationRequestText directly influences the effectiveness of the authorization process. Well-crafted text can reduce decision times, clarify the reasons behind requests, and decrease the likelihood of unauthorized access being granted due to misunderstanding or lack of information.

**Technical Impact when configured:**

Proper configuration ensures that authorization requests are accompanied by clear, concise, and relevant details. This can impact system security and compliance by ensuring decision-makers are fully informed, thereby facilitating more secure and compliant authorization decisions.

**Examples Scenario:**

A user initiates a request for access to sensitive financial reports. The AuthorizationRequestText is configured to include detailed information about the requested access, including the reports' sensitivity level and the reason for the request. This enables approvers to make more informed decisions, potentially highlighting risk areas or compliance requirements related to the access.

**Related Settings:**

- WorkflowApprovalGroup
- WorkflowInstanceSteps
- WorkflowApprovalGroupContents

**Best Practices:** configure when the workflow involves critical resources or sensitive access rights, avoid when general information is sufficient and additional text may clutter or slow down the approval process.