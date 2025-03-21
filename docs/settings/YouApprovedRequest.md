# You Approved Request

**Technical Name:** YouApprovedRequest

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `YouApprovedRequest` parameter is designed to be used within the Pathlock Cloud GRC platform, specifically as part of the Workflow Approval Group Steps. This parameter plays a critical role in the workflow actions that require an approval process, ensuring that requests go through the necessary review and approval stages.

**Business Impact:**

Implementing the `YouApprovedRequest` parameter effectively can streamline the approval processes within an organization, reduce the time taken for request approvals, and enhance compliance with internal and external audit requirements. It ensures that only authorized and reviewed requests are approved, maintaining the integrity of the system and preventing unauthorized actions.

**Technical Impact when configured:**

When the `YouApprovedRequest` parameter is configured, it affects how approval workflow steps are processed. It ensures that requests are only moved forward in the workflow if they meet the defined criteria for approval, preventing any unauthorized or incorrect requests from bypassing the necessary governance checks.

**Examples Scenario:**

Consider a scenario where an organization has implemented a multi-step approval process for financial transactions. The `YouApprovedRequest` parameter could be employed to ensure that each transaction is reviewed and approved by the appropriate personnel before it is executed. This not only ensures compliance with financial regulations but also adds an extra layer of security to prevent fraud.

**Related Settings:** 

- `FieldForAuthorizationReviewOnly`

**Applicable Workflows Actions:** 

- WorkFlowApprovalGroupStep

**Best Practices:** 

- **Configure when:** You have processes or workflows that require strict compliance with authorization protocols, ensuring that each step is approved by the correct authority.
  
- **Avoid when:** Quick, non-critical workflow steps do not necessitate a thorough approval process, to prevent unnecessary delays in workflow processing.