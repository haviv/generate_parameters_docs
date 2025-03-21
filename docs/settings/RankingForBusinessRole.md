# Ranking For Business Role

**Technical Name:** RankingForBusinessRole

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `RankingForBusinessRole` parameter is designed to prioritize and sequence business roles within Pathlock's automated workflows. This parameter influences the order in which business roles are processed, ensuring that roles with higher rankings are addressed first. This is particularly useful in scenarios where certain roles demand prompt attention due to their critical nature or impact on business operations.

**Business Impact:**

Adjusting the `RankingForBusinessRole` can streamline compliance and authorization processes by prioritizing roles critical to business functions. Properly configuring this parameter contributes to efficient risk management, ensures timely compliance reviews, and supports the organizational hierarchy's integrity.

**Technical Impact when configured:**

When configured, `RankingForBusinessRole` directly affects the execution order of workflow actions related to business roles. This ensures that roles of higher significance are processed and reviewed ahead of others, optimizing the workflow for efficiency and compliance.

**Examples Scenario:**

Consider an organization where certain roles, such as 'Financial Manager', have a higher compliance and security requirement than others. By setting a higher ranking for the 'Financial Manager' role, the system ensures that any changes, reviews, or updates related to this role are processed as a priority, safeguarding the organization's financial integrity.

**Related Settings:**

- `RankingForWorkflowType`

**Best Practices:** Configure the `RankingForBusinessRole` for roles pivotal to your organization's operational, compliance, or security needs to ensure they are processed preferentially. Avoid setting arbitrary rankings without considering the organizational impact and workflow dependencies.