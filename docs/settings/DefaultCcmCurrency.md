# Default CCM Currency

**Technical Name:** DefaultCcmCurrency

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter specifies the default currency setting used across various modules of the Pathlock Cloud GRC platform, affecting calculations and reportings related to financial data monitoring and compliance.

**Business Impact:** Proper configuration of this parameter ensures that all financial transactions and data are accurately monitored and reported in the organization's preferred currency. It influences compliance reporting, transaction monitoring, and financial data analysis, ensuring coherence and consistency across the platform, which is critical for enforcing financial controls and meeting regulatory requirements.

**Technical Impact when configured:**

- Ensures accurate currency conversion and financial data representation across the platform.
- Affects the calculation of statistics and monetary values within the transaction monitoring services. 
- Impacts the generation of events and daily email summaries related to financial data compliance and violations.

**Examples Scenario:** If an organization operates primarily in the Eurozone but receives transactions in various currencies, setting the default CCM currency to EUR ensures that all transaction values are automatically converted and reported in Euros. This simplifies financial reporting, compliance checks, and risk assessments.

**Related Settings:** 

- `DailyEmailHeader` and `DailyEmailSubject` for configurations related to daily summary emails regarding events and compliance violations.
- Parameters influencing event generation and reporting preferences.

**Best Practices:** 

- **Configure when** setting up the system for the first time or when there is a change in the primary operational currency of the organization.
- **Avoid when** the default setting aligns with the organization’s primary currency to minimize unnecessary system configurations and potential for data inconsistency.