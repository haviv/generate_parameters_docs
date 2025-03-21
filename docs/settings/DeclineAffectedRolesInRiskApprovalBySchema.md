# Decline Affected Roles In Risk Approval By Schema

**Technical Name:** DeclineAffectedRolesInRiskApprovalBySchema

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter enables more granular control over the risk approval process within Pathlock's Cloud GRC platform. Specifically, it allows for the declining of affected roles during the risk approval step based on the schema.

**Business Impact:**

Implementing this parameter can significantly streamline the risk approval process by enabling decision-makers to focus on relevant roles within specific schemas. This can lead to more accurate and efficient risk management decisions, potentially reducing the overall risk exposure of the organization.

**Technical Impact when configured:**

Configuring this parameter can aid in the customization of the risk approval workflow, especially in environments with complex user roles and permissions. It helps in refining the workflow to only include roles relevant to the specific schema under consideration, leading to a more focused review process.

**Examples Scenario:**

Consider a scenario where an organization operates across different regulatory environments, each with its unique set of roles and compliance requirements. By configuring this parameter, the risk approval process can be tailored to only include or exclude specific roles pertinent to the regulatory schema in focus, ensuring compliance while optimizing the approval workflow.

**Related Settings:**

- HideRolesInSearchWindowByAttribute10Values

**Best Practices:** configure when the risk approval process involves multiple schemas with distinct sets of roles; avoid when all roles across schemas require review without discrimination.