# Show Transaction Attribute10

**Technical Name:** ShowTransactionAttribute10

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables or disables the display of the tenth custom transaction attribute within various reports and matrices across the Pathlock GRC platform. This setting is utilized in filtering and identifying specific transactional data based on custom-defined parameters.

**Business Impact:**

Configuring this parameter allows organizations to tailor their reporting and oversight capabilities in line with specific internal or external compliance requirements, enabling more granular control over the data displayed and analyzed. It can impact how effectively an organization can monitor, report, and act upon their GRC-related data.

**Technical Impact when configured:**

When activated, this parameter will display the tenth transaction attribute in reports and matrices, providing users with additional context or categorization that can be critical for detailed analysis or compliance needs. Depending on its usage, it can help in highlighting specific, potentially critical transactional activities or categorizations that require attention.

**Examples Scenario:**

For instance, if Transaction Attribute10 is configured to represent a "Confidentiality Level", enabling this attribute in reports can help compliance officers to easily filter and identify transactions that pertain to high confidentiality items, thereby streamlining audit and compliance review processes.

**Related Settings:**

- `ShowTransactionAttribute2`
- `ShowTransactionAttribute3`
- `ShowHighRiskColumnTransaction`

**Best Practices:** 

- **Configure when:** There is a need for enhanced reporting capabilities that require the inclusion of specific transaction attributes not covered by the default settings. It is particularly useful for tracking customized or nuanced data points critical for organizational compliance, security, or risk management processes.
  
- **Avoid when:** The inclusion of additional transaction attributes may lead to information overload or when the attribute does not significantly contribute to the analysis, reporting, or decision-making processes.