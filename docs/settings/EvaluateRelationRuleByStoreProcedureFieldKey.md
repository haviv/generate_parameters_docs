**Evaluate Relation Rule By Store Procedure Field Key**

**Technical Name:** EvaluateRelationRuleByStoreProcedureFieldKey

**Category:** Workflow

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

This parameter controls how the Pathlock Cloud GRC platform evaluates relation rules by utilizing a stored procedure's field key. It is designed to customize and streamline the process of managing change documents, specifically in the context of recording and analyzing changes to critical business documents.

**Business Impact:**

Proper configuration of this parameter aids in strengthening the organization's change management processes by ensuring that changes to documents are evaluated systematically against predefined rules. This contributes significantly to maintaining integrity and compliance standards.

**Technical Impact when configured:**

When properly set, this parameter enables the system to automatically invoke a specific stored procedure that assesses change records against a set of conditions. This capability ensures that all changes are compliant with internal controls and regulatory requirements, thereby reducing the risk of non-compliance.

**Examples Scenario:**

Suppose a financial institution implements a new policy requiring all changes to financial reports to be automatically reviewed for compliance with new financial regulatory standards. By configuring this parameter to evaluate changes against the relevant stored procedure, the institution can automate the compliance checks of document changes, thereby enhancing efficiency and reducing the likelihood of non-compliance.

**Related Settings:** Not Specified

**Applicable Workflows Actions:** Not Applicable

**Best Practices:** 

- **Configure when:** you need to automate compliance and integrity checks of document changes, especially in environments where changes are frequent and subject to strict regulatory standards.
  
- **Avoid when:** the evaluation of document changes does not significantly impact your organization's compliance posture, or when the overhead of setting up and maintaining custom stored procedures outweighs the benefits.