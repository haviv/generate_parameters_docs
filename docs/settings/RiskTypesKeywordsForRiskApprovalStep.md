# Risk Types Keywords For Risk Approval Step

**Technical Name:** RiskTypesKeywordsForRiskApprovalStep

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines specific risk types or keywords that are used to filter or identify risks during the Risk Approval Step in workflow processes. It guides the workflow engine in determining which risks should be presented for approval based on the configured keywords or risk types.

**Business Impact:**

Configuring this parameter with relevant risk types or keywords ensures that only specific risks that match the criteria are escalated for approval, streamlining the risk management process. This precision helps in focusing efforts on significant risks, thus enhancing the efficiency of risk mitigation strategies within an organization.

**Technical Impact when configured:**

When configured, this parameter influences the workflow engine's behavior by filtering risks that appear during the Risk Approval Step. It directly affects the subset of risks that require approval, ensuring that the workflow process is aligned with organizational risk management policies and priorities.

**Examples Scenario:**

For instance, if an organization wants to prioritize risks related to 'Financial Fraud' and 'Data Breach', these keywords can be set as values for the RiskTypesKeywordsForRiskApprovalStep. Consequently, during the Risk Approval Step, only risks tagged with 'Financial Fraud' and 'Data Breach' will be brought forward for approval, allowing the organization to focus on these critical areas.

**Related Settings:**

**Applicable Workflows Actions:**

- RisksApprovalStep

**Best Practices:** 

- **Configure when:** There is a need to focus on specific types of risks during the approval process. Identifying and prioritizing critical risk types or areas ensures that key risks are managed effectively.
  
- **Avoid when:** If the organization's risk management approach is holistic and does not require prioritization or filtering of risks based on types or keywords during the approval step.